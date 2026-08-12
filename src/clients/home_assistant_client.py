import json
import os
import re

import requests
from requests import Response

from src.configuration.configuration import Configuration


def sanitize_entity_id_part(value: str) -> str:
    """Convert a value into a valid Home Assistant entity id object_id part.

    Home Assistant only accepts lowercase letters, digits and underscores in an
    entity id. Serials such as ``VSN-1235SDFE1127-01`` contain uppercase letters
    and hyphens which cause the states API to return ``400 Bad Request``.
    """
    slug = re.sub(r'[^a-z0-9_]+', '_', str(value).lower())
    return re.sub(r'_+', '_', slug).strip('_')


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

