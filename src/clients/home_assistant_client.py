import json
import os

import requests
from requests import Response

from src.configuration.configuration import Configuration


class HomeAssistantClient:
    def __init__(self):
        options = Configuration()

        self.base_url = options.home_assistant_url()
        token = options.home_assistant_token()
        self.headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}

    def post(self, path: str, payload: dict) -> Response:
        return requests.post(self.base_url + path, json=payload, headers=self.headers, timeout=10, verify=False)

    def get(self, path: str) -> Response:
        return requests.get(self.base_url + path, headers=self.headers, timeout=10, verify=False)

