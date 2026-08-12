import threading
from datetime import datetime

from src.clients.home_assistant_client import sanitize_entity_id_part
from src.configuration.configuration import Configuration

try:
    import paho.mqtt.client as mqtt
except ImportError:  # paho-mqtt is optional; MQTT features are inert without it.
    mqtt = None


class ConsoleColor:
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"


# HA sensor device classes this add-on emits, mapped to the units they accept.
# A device_class whose unit does not match is dropped so Home Assistant does not
# reject the discovery config (e.g. GetDCACTemp sends device_class "power" with °C).
_DEVICE_CLASS_UNITS = {
    "energy": {"Wh", "kWh", "MWh"},
    "power": {"W", "kW", "VA"},
    "voltage": {"V", "mV"},
    "current": {"A", "mA"},
    "temperature": {"°C", "℃", "°F", "K"},
    "frequency": {"Hz", "kHz"},
    "battery": {"%"},
}

_TIMESTAMP_FORMATS = (
    "%Y/%m/%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y-%m-%d %H:%M",
)


def _to_iso8601(value):
    """Convert a provider datetime string to a timezone-aware ISO 8601 string.

    Returns None when the value is empty or cannot be parsed, so the caller can
    skip publishing an invalid timestamp state.
    """
    text = str(value).strip()
    if not text:
        return None

    parsed = None
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        for fmt in _TIMESTAMP_FORMATS:
            try:
                parsed = datetime.strptime(text, fmt)
                break
            except ValueError:
                continue

    if parsed is None:
        return None
    if parsed.tzinfo is None:
        # Provider timestamps are naive local time; attach the container's local zone.
        parsed = parsed.astimezone()
    return parsed.isoformat()


def _discovery_fields(uom, uom_long):
    """Return validated (device_class, unit, state_class) for a discovery config."""
    unit = uom or None
    device_class = uom_long or None

    if device_class == "timestamp":
        return "timestamp", None, None

    if device_class in _DEVICE_CLASS_UNITS:
        allowed = _DEVICE_CLASS_UNITS[device_class]
        if unit not in allowed:
            device_class = None
    else:
        device_class = None

    if uom == "kWh":
        state_class = "total_increasing"
    elif device_class is not None or unit is not None:
        state_class = "measurement"
    else:
        state_class = None

    return device_class, unit, state_class


class MqttClient:
    def __init__(self):
        options = Configuration()
        self._enabled = options.mqtt_enabled()
        self._host = options.mqtt_host()
        self._port = options.mqtt_port()
        self._username = options.mqtt_username()
        self._password = options.mqtt_password()
        self._discovery_prefix = options.mqtt_discovery_prefix()
        self._base_topic = options.mqtt_base_topic()
        self._client = None
        self._connected = False

    @property
    def enabled(self):
        return self._enabled

    def availability_topic(self):
        return f"{self._base_topic}/status"

    def connect(self):
        if not self._enabled:
            return False
        if self._connected:
            return True
        if mqtt is None:
            print(ConsoleColor.FAIL + "Error: paho-mqtt is not installed; cannot use MQTT." + ConsoleColor.ENDC)
            return False
        if not self._host:
            print(ConsoleColor.FAIL + "Error: MQTT is enabled but no broker host is configured or provided by the Supervisor." + ConsoleColor.ENDC)
            return False

        try:
            client = mqtt.Client()
            if self._username:
                client.username_pw_set(self._username, self._password)
            client.will_set(self.availability_topic(), "offline", qos=1, retain=True)
            client.connect(self._host, self._port, keepalive=60)
            client.loop_start()
            self._client = client
            self._connected = True
            self.publish_availability("online")
            print(ConsoleColor.OKGREEN + f"MQTT broker connection: OK ({self._host}:{self._port})" + ConsoleColor.ENDC)
            return True
        except Exception as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to MQTT broker {self._host}:{self._port}. {e}" + ConsoleColor.ENDC)
            self._client = None
            self._connected = False
            return False

    def publish_availability(self, state):
        if not self._connected or self._client is None:
            return
        self._client.publish(self.availability_topic(), state, qos=1, retain=True)

    def publish_sensor(self, serial, s_name, friendly_name, uom, uom_long, value):
        """Publish the discovery config (retained) and current state for one sensor."""
        if not self._connected or self._client is None:
            return False

        # Skip sensors whose value is unknown/missing (API returned None or empty).
        raw = str(value).strip()
        if value is None or raw in ("None", ""):
            return True

        node = sanitize_entity_id_part(serial)
        object_id = f"solarsynkv3_{node}_{s_name}"
        state_topic = f"{self._base_topic}/{node}/{s_name}"
        config_topic = f"{self._discovery_prefix}/sensor/solarsynkv3_{node}/{s_name}/config"

        device_class, unit, state_class = _discovery_fields(uom, uom_long)

        config = {
            "name": friendly_name,
            "unique_id": object_id,
            "object_id": object_id,
            "state_topic": state_topic,
            "availability_topic": self.availability_topic(),
            "device": {
                "identifiers": [f"solarsynkv3_{node}"],
                "name": f"SolarSynk {serial}",
                "manufacturer": "SolarSynk",
                "model": "SunSynk Inverter",
            },
        }
        if device_class is not None:
            config["device_class"] = device_class
        if unit is not None:
            config["unit_of_measurement"] = unit
        if state_class is not None:
            config["state_class"] = state_class

        import json
        self._client.publish(config_topic, json.dumps(config), qos=0, retain=True)

        state_value = str(value)
        if device_class == "timestamp":
            iso_value = _to_iso8601(value)
            if iso_value is None:
                # Empty/unparseable timestamp: keep the retained config but skip the invalid state.
                return True
            state_value = iso_value

        self._client.publish(state_topic, state_value, qos=0, retain=True)
        return True

    def disconnect(self):
        if self._client is None:
            return
        try:
            # Don't publish offline here: the LWT handles unexpected disconnects.
            # Publishing offline on a normal restart makes sensors unavailable during the sleep window.
            self._client.loop_stop()
            self._client.disconnect()
        except Exception:
            pass
        finally:
            self._client = None
            self._connected = False


_client_singleton = None
_lock = threading.Lock()


def get_client():
    global _client_singleton
    if _client_singleton is None:
        with _lock:
            if _client_singleton is None:
                _client_singleton = MqttClient()
    return _client_singleton


def close_client():
    global _client_singleton
    if _client_singleton is not None:
        _client_singleton.disconnect()
        _client_singleton = None
