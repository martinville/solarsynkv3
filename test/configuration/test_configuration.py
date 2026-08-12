import json
from tempfile import NamedTemporaryFile
from unittest import TestCase
from unittest.mock import patch

from src.configuration.configuration import Configuration


class TestOptions(TestCase):
    def setUp(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {'foo': 'bar'},
                temporary_file
            )
            temporary_file.flush()

            self.configuration = Configuration(temporary_file.name)

    def test_getitem_should_should_return_value_for_key(self):
        self.assertEqual('bar', self.configuration['foo'])

    def test_getitem_should_raise_key_error_when_key_is_not_found(self):
        with self.assertRaises(KeyError):
            self.configuration['bar']

    def test_get_should_return_value_for_key(self):
        self.assertEqual('bar', self.configuration.get('foo'))

    def test_get_should_return_default_value_when_key_is_not_found(self):
        self.assertEqual('default', self.configuration.get('bar', 'default'))

    def test_home_assistant_url_should_build_url_if_use_internal_api_is_false_for_enable_https_false(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {
                    'Enable_HTTPS': False,
                    'Home_Assistant_IP': 'the-host',
                    'Home_Assistant_PORT': 'the-port'
                },
                temporary_file
            )
            temporary_file.flush()

            self.configuration = Configuration(temporary_file.name)

            self.assertEqual(
                'http://the-host:the-port',
                self.configuration.home_assistant_url()
            )

    def test_home_assistant_url_should_build_url_if_use_internal_api_is_false_for_enable_https_true(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {
                    'Enable_HTTPS': True,
                    'Home_Assistant_IP': 'the-host',
                    'Home_Assistant_PORT': 'the-port'
                },
                temporary_file
            )
            temporary_file.flush()

            self.configuration = Configuration(temporary_file.name)

            self.assertEqual(
                'https://the-host:the-port',
                self.configuration.home_assistant_url()
            )

    def test_home_assistant_url_should_be_supervisor_if_use_internal_api_is_true(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {
                    'use_internal_api': True
                },
                temporary_file
            )
            temporary_file.flush()

            self.configuration = Configuration(temporary_file.name)

            self.assertEqual(
                'http://supervisor/core',
                self.configuration.home_assistant_url()
            )

    def test_home_assistant_token_should_load_token_if_use_internal_api_is_false(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {
                    'HA_LongLiveToken': 'the-token'
                },
                temporary_file
            )
            temporary_file.flush()

            self.configuration = Configuration(temporary_file.name)

            self.assertEqual(
                'the-token',
                self.configuration.home_assistant_token()
            )

    def test_home_assistant_token_should_return_supervisor_token_if_use_internal_api_is_false(self):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(
                {
                    'use_internal_api': True
                },
                temporary_file
            )
            temporary_file.flush()

            with patch.dict('os.environ', {'SUPERVISOR_TOKEN': 'the-supervisor-token'}):
                self.configuration = Configuration(temporary_file.name)

            self.assertEqual(
                'the-supervisor-token',
                self.configuration.home_assistant_token()
            )

    def _configuration_with(self, settings, environ=None):
        with NamedTemporaryFile('w') as temporary_file:
            json.dump(settings, temporary_file)
            temporary_file.flush()
            with patch.dict('os.environ', environ or {}, clear=True):
                return Configuration(temporary_file.name)

    def test_mqtt_enabled_defaults_to_false(self):
        configuration = self._configuration_with({})
        self.assertFalse(configuration.mqtt_enabled())

    def test_mqtt_enabled_reads_option(self):
        configuration = self._configuration_with({'mqtt_enabled': True})
        self.assertTrue(configuration.mqtt_enabled())

    def test_mqtt_host_prefers_option_over_env(self):
        configuration = self._configuration_with(
            {'mqtt_host': 'option-host'},
            {'MQTT_HOST': 'env-host'}
        )
        self.assertEqual('option-host', configuration.mqtt_host())

    def test_mqtt_host_falls_back_to_env(self):
        configuration = self._configuration_with(
            {'mqtt_host': ''},
            {'MQTT_HOST': 'env-host'}
        )
        self.assertEqual('env-host', configuration.mqtt_host())

    def test_mqtt_port_defaults_to_1883(self):
        configuration = self._configuration_with({})
        self.assertEqual(1883, configuration.mqtt_port())

    def test_mqtt_port_falls_back_to_env(self):
        configuration = self._configuration_with(
            {'mqtt_port': ''},
            {'MQTT_PORT': '8883'}
        )
        self.assertEqual(8883, configuration.mqtt_port())

    def test_mqtt_credentials_fall_back_to_env(self):
        configuration = self._configuration_with(
            {'mqtt_username': '', 'mqtt_password': ''},
            {'MQTT_USERNAME': 'env-user', 'MQTT_PASSWORD': 'env-pass'}
        )
        self.assertEqual('env-user', configuration.mqtt_username())
        self.assertEqual('env-pass', configuration.mqtt_password())

    def test_mqtt_discovery_prefix_and_base_topic_defaults(self):
        configuration = self._configuration_with({})
        self.assertEqual('homeassistant', configuration.mqtt_discovery_prefix())
        self.assertEqual('solarsynkv3', configuration.mqtt_base_topic())