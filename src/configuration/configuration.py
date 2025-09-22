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
        if self.get('use_internal_api', False):
            return 'http://supervisor/core'
        else:
            if self['Enable_HTTPS']:
                httpurl_proto = "https"
            else:
                httpurl_proto = "http"

            # API URL
            self.base_url = f"{httpurl_proto}://" + str(self['Home_Assistant_IP']) + ":" + str(
                self['Home_Assistant_PORT'])

        return self.base_url

    def home_assistant_token(self):
        if self.get('use_internal_api', False):
            return self.supervisor_token
        else:
            return self['HA_LongLiveToken']