import json
import os

import requests
from requests import Response


class HomeAssistantClient:
    def __init__(self):
        with open('/data/options.json') as options_file:
            json_settings = json.load(options_file)

            if json_settings.get('use_internal_api', False):
                print("Using internal API")
                self.base_url = f"http://supervisor/core"
                token = os.environ['SUPERVISOR_TOKEN']
            else:
                print('Using API as specified in options.json')
                token = json_settings['HA_LongLiveToken']

                if json_settings['Enable_HTTPS']:
                    httpurl_proto = "https"
                else:
                    httpurl_proto = "http"

                # API URL
                self.base_url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(
                    json_settings['Home_Assistant_PORT'])

            self.headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}

    def post(self, path: str, payload: dict) -> Response:
        return requests.post(self.base_url + path, json=payload, headers=self.headers, timeout=10, verify=False)

    def get(self, path: str) -> Response:
        return requests.get(self.base_url + path, headers=self.headers, timeout=10, verify=False)

