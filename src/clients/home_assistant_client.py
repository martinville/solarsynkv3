import json

import requests
from requests import Response


class HomeAssistantClient:
    def __init__(self):
        with open('/data/options.json') as options_file:
            json_settings = json.load(options_file)

            HAToken = json_settings['HA_LongLiveToken']

            if json_settings['Enable_HTTPS']:
                httpurl_proto = "https"
            else:
                httpurl_proto = "http"

                # print(json_settings['Enable_HTTPS'])
            # API URL
            self.base_url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(
                json_settings['Home_Assistant_PORT'])

            self.headers = {"Content-Type": "application/json","Authorization": f"Bearer {HAToken}"}

    def post(self, path: str, payload: dict) -> Response:
        return requests.post(self.base_url + path, json=payload, headers=self.headers, timeout=10, verify=False)

    def get(self, path: str) -> Response:
        return requests.get(self.base_url + path, headers=self.headers, timeout=10, verify=False)

