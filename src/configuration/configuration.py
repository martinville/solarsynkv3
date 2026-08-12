import json
import os


class Configuration:
    def __init__(self, configuration_file_path='/data/options.json'):
        with open(configuration_file_path) as options_file:
            self._settings = json.load(options_file)

        self.supervisor_token = os.environ.get('SUPERVISOR_TOKEN')

    def __getitem__(self, key):
        return self._settings[key]

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def home_assistant_url(self):
        if self.get('use_internal_api', False) or not self.get('Home_Assistant_IP', ''):
            # No explicit IP means we're on the local HA OS instance; use the Supervisor API.
            return 'http://supervisor/core/api'

        httpurl_proto = "https" if self['Enable_HTTPS'] else "http"
        self.base_url = f"{httpurl_proto}://{self['Home_Assistant_IP']}:{self['Home_Assistant_PORT']}/api"
        return self.base_url

    def home_assistant_token(self):
        if self.get('use_internal_api', False) or not self.get('Home_Assistant_IP', ''):
            return self.supervisor_token
        return self['HA_LongLiveToken']

    def mqtt_enabled(self):
        return bool(self.get('mqtt_enabled', False))

    def mqtt_host(self):
        # Manual option wins, otherwise fall back to the Supervisor-provided MQTT service.
        return self.get('mqtt_host') or os.environ.get('MQTT_HOST') or ''

    def mqtt_port(self):
        port = self.get('mqtt_port') or os.environ.get('MQTT_PORT')
        return int(port) if port else 1883

    def mqtt_username(self):
        return self.get('mqtt_username') or os.environ.get('MQTT_USERNAME') or ''

    def mqtt_password(self):
        return self.get('mqtt_password') or os.environ.get('MQTT_PASSWORD') or ''

    def mqtt_discovery_prefix(self):
        return self.get('mqtt_discovery_prefix') or 'homeassistant'

    def mqtt_base_topic(self):
        return self.get('mqtt_base_topic') or 'solarsynkv3'