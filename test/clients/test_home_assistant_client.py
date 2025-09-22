from unittest import TestCase
from unittest.mock import MagicMock, patch

from responses import RequestsMock
from responses.matchers import header_matcher, json_params_matcher

import src
from src.clients.home_assistant_client import HomeAssistantClient


class TestHomeAssistantClient(TestCase):
    def setUp(self):
        self.configuration = MagicMock()
        self.configuration.home_assistant_url.return_value= 'https://home-assistant-base-url'
        self.configuration.home_assistant_token.return_value= 'the-token'

        with patch.object(src.clients.home_assistant_client, 'Configuration', return_value=self.configuration):
            self.home_assistant_client = HomeAssistantClient()

    def test_get(self):
        with RequestsMock() as rsps:
            rsps.add(
                rsps.GET,
                'https://home-assistant-base-url/the-path',
                json={
                    'the-key': 'the-value'
                },
                match=[
                    header_matcher(
                        {
                            "Authorization": "Bearer the-token"
                        }
                    )
                ],
            )

            response = self.home_assistant_client.get("/the-path")

            self.assertEqual(
                {
                    'the-key': 'the-value'
                },
                response.json()
            )

    def test_post(self):
        with RequestsMock() as rsps:
            rsps.add(
                rsps.POST,
                'https://home-assistant-base-url/the-path',
                match=[
                    header_matcher(
                        {
                            "Authorization": "Bearer the-token"
                        }
                    ),
                    json_params_matcher(
                        {
                            'the-key': 'the-value'
                        }
                    )
                ],
            )

            response = self.home_assistant_client.post("/the-path", {'the-key': 'the-value'})

            response.raise_for_status()
