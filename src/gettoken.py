import json
import requests
from config.api import TOKEN_PATH
from util.console import ConsoleColor


def gettoken(base_url, username, password):
    BearerToken = ""

    # API URL
    url = f"{base_url}/{TOKEN_PATH}"
    # Prepare request payload
    payload = {
        "areaCode": "sunsynk",
        "client_id": "csp-web",
        "grant_type": "password",
        "password": password,
        "source": "sunsynk",
        "username": username,
    }
    # Headers
    headers = {"Content-Type": "application/json"}    
    try:
        # Send POST request with timeout (10s)
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse response
        parsed_login_json = response.json()

        # Check login status
        if parsed_login_json.get('msg') == "Success":
            print("Sunsynk Login: " + ConsoleColor.OKGREEN + parsed_login_json['msg'] + ConsoleColor.ENDC)
            BearerToken = parsed_login_json['data']['access_token']
            return BearerToken
        else:
            print("Sunsynk Login: " + ConsoleColor.FAIL + parsed_login_json['msg'] + ConsoleColor.ENDC)
            return BearerToken

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)
        return BearerToken

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)
        return BearerToken

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)
        return BearerToken