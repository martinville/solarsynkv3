import json
from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

import src.clients.mqtt_client as mqtt_client_module
from src.clients.mqtt_client import MqttClient, _discovery_fields, _to_iso8601


def _configuration(**overrides):
    configuration = MagicMock()
    configuration.mqtt_enabled.return_value = overrides.get('mqtt_enabled', True)
    configuration.mqtt_host.return_value = overrides.get('mqtt_host', 'broker-host')
    configuration.mqtt_port.return_value = overrides.get('mqtt_port', 1883)
    configuration.mqtt_username.return_value = overrides.get('mqtt_username', 'user')
    configuration.mqtt_password.return_value = overrides.get('mqtt_password', 'pass')
    configuration.mqtt_discovery_prefix.return_value = overrides.get('mqtt_discovery_prefix', 'homeassistant')
    configuration.mqtt_base_topic.return_value = overrides.get('mqtt_base_topic', 'solarsynkv3')
    return configuration


class TestDiscoveryFields(TestCase):
    def test_kwh_is_total_increasing_energy(self):
        self.assertEqual(('energy', 'kWh', 'total_increasing'), _discovery_fields('kWh', 'energy'))

    def test_voltage_is_measurement(self):
        self.assertEqual(('voltage', 'V', 'measurement'), _discovery_fields('V', 'voltage'))

    def test_mismatched_device_class_is_dropped(self):
        # GetDCACTemp sends device_class "power" with a °C unit; the invalid class is dropped.
        self.assertEqual((None, '°C', 'measurement'), _discovery_fields('°C', 'power'))

    def test_plain_sensor_has_no_class_unit_or_state_class(self):
        self.assertEqual((None, None, None), _discovery_fields('', ''))

    def test_timestamp_keeps_device_class_without_unit_or_state_class(self):
        self.assertEqual(('timestamp', None, None), _discovery_fields('', 'timestamp'))

    def test_unknown_device_class_is_dropped_but_unit_kept(self):
        self.assertEqual((None, 'A', 'measurement'), _discovery_fields('A', 'not_a_class'))


class TestToIso8601(TestCase):
    def test_converts_slash_format_to_aware_iso(self):
        result = _to_iso8601('2026/08/12 20:18:50')
        parsed = datetime.fromisoformat(result)
        self.assertIsNotNone(parsed.tzinfo)
        self.assertEqual((2026, 8, 12, 20, 18, 50), (parsed.year, parsed.month, parsed.day, parsed.hour, parsed.minute, parsed.second))

    def test_converts_dash_format(self):
        result = _to_iso8601('2026-08-12 20:18:50')
        self.assertIsNotNone(datetime.fromisoformat(result).tzinfo)

    def test_empty_returns_none(self):
        self.assertIsNone(_to_iso8601(''))

    def test_unparseable_returns_none(self):
        self.assertIsNone(_to_iso8601('not a date'))


class TestMqttClient(TestCase):
    def setUp(self):
        self.paho_client = MagicMock()
        self.paho_module = MagicMock()
        self.paho_module.Client.return_value = self.paho_client

    def _build(self, **overrides):
        with patch.object(mqtt_client_module, 'Configuration', return_value=_configuration(**overrides)):
            client = MqttClient()
        return client

    def test_connect_returns_false_when_disabled(self):
        client = self._build(mqtt_enabled=False)
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            self.assertFalse(client.connect())
        self.paho_module.Client.assert_not_called()

    def test_connect_returns_false_when_no_host(self):
        client = self._build(mqtt_host='')
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            self.assertFalse(client.connect())

    def test_connect_returns_false_when_paho_missing(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', None):
            self.assertFalse(client.connect())

    def test_connect_publishes_online_and_sets_will(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            self.assertTrue(client.connect())

        self.paho_client.username_pw_set.assert_called_once_with('user', 'pass')
        self.paho_client.will_set.assert_called_once_with('solarsynkv3/status', 'offline', qos=1, retain=True)
        self.paho_client.connect.assert_called_once_with('broker-host', 1883, keepalive=60)
        self.paho_client.loop_start.assert_called_once()
        self.paho_client.publish.assert_any_call('solarsynkv3/status', 'online', qos=1, retain=True)

    def test_connect_is_idempotent(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            self.assertTrue(client.connect())
            self.assertTrue(client.connect())
        self.paho_module.Client.assert_called_once()

    def test_publish_sensor_publishes_config_and_state(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            result = client.publish_sensor('VSN-E47W23641127-01', 'battery_soc', 'Battery SOC', '%', 'battery', '56.0')

        self.assertTrue(result)

        config_call = self.paho_client.publish.call_args_list[0]
        state_call = self.paho_client.publish.call_args_list[1]

        self.assertEqual(
            'homeassistant/sensor/solarsynkv3_vsn_e47w23641127_01/battery_soc/config',
            config_call.args[0]
        )
        config = json.loads(config_call.args[1])
        self.assertEqual('solarsynkv3_vsn_e47w23641127_01_battery_soc', config['unique_id'])
        self.assertEqual('solarsynkv3_vsn_e47w23641127_01_battery_soc', config['object_id'])
        self.assertEqual('solarsynkv3/vsn_e47w23641127_01/battery_soc', config['state_topic'])
        self.assertEqual('battery', config['device_class'])
        self.assertEqual('%', config['unit_of_measurement'])
        self.assertEqual('measurement', config['state_class'])
        self.assertEqual(['solarsynkv3_vsn_e47w23641127_01'], config['device']['identifiers'])
        self.assertEqual('SolarSynk VSN-E47W23641127-01', config['device']['name'])
        self.assertTrue(config_call.kwargs['retain'])

        self.assertEqual('solarsynkv3/vsn_e47w23641127_01/battery_soc', state_call.args[0])
        self.assertEqual('56.0', state_call.args[1])

    def test_publish_sensor_returns_false_when_not_connected(self):
        client = self._build()
        self.assertFalse(client.publish_sensor('SER', 'sn', 'SN', '', '', 'x'))

    def test_publish_sensor_skips_none_value(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            result = client.publish_sensor('SER', 'acCoupleFreqUpper', 'AC Couple Freq Upper', '', '', None)
        self.assertTrue(result)
        self.paho_client.publish.assert_not_called()

    def test_publish_sensor_skips_string_none_value(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            result = client.publish_sensor('SER', 'acCoupleFreqUpper', 'AC Couple Freq Upper', '', '', 'None')
        self.assertTrue(result)
        self.paho_client.publish.assert_not_called()

    def test_publish_sensor_skips_empty_string_value(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            result = client.publish_sensor('SER', 'model', 'Model', '', '', '')
        self.assertTrue(result)
        self.paho_client.publish.assert_not_called()

    def test_publish_sensor_converts_timestamp_value_to_iso(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            client.publish_sensor('SER', 'solarsynk_last_updated', 'Last Updated', '', 'timestamp', '2026/08/12 20:18:50')

        config_call = self.paho_client.publish.call_args_list[0]
        state_call = self.paho_client.publish.call_args_list[1]

        config = json.loads(config_call.args[1])
        self.assertEqual('timestamp', config['device_class'])
        self.assertNotIn('state_class', config)
        self.assertNotIn('unit_of_measurement', config)

        published = datetime.fromisoformat(state_call.args[1])
        self.assertIsNotNone(published.tzinfo)
        self.assertEqual(20, published.hour)

    def test_publish_sensor_skips_state_for_empty_timestamp(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            result = client.publish_sensor('SER', 'solarsynk_last_updated', 'Last Updated', '', 'timestamp', '')

        self.assertTrue(result)
        # Empty value is caught by the None/empty guard before reaching timestamp conversion.
        self.paho_client.publish.assert_not_called()

    def test_disconnect_stops_loop_and_disconnects_without_publishing_offline(self):
        client = self._build()
        with patch.object(mqtt_client_module, 'mqtt', self.paho_module):
            client.connect()
            self.paho_client.publish.reset_mock()
            client.disconnect()

        # offline must NOT be published on a clean exit — LWT handles unexpected drops.
        published_topics = [call.args[0] for call in self.paho_client.publish.call_args_list]
        self.assertNotIn('solarsynkv3/status', published_topics)
        self.paho_client.loop_stop.assert_called_once()
        self.paho_client.disconnect.assert_called_once()
