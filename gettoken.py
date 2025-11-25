import time
from hashlib import md5


def get_nonce():
    return int(time.time() * 1000)


def gettoken():
    import base64
    import json
    import requests
    import hashlib
    from io import StringIO
    from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
    from cryptography.hazmat.primitives.serialization import load_pem_public_key

    BearerToken = ""

    class ConsoleColor:
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"

    with open('/data/options.json') as options_file:
       json_settings = json.load(options_file)

    # Determine source based on API server
    source = "elinter" if json_settings["API_Server"] == "pv.inteless.com" else "sunsynk"

    # Create a nonce for the public key request
    public_key_nonce = get_nonce()

    # Create a signature for the public key request
    public_key_signature_input = f"nonce={public_key_nonce}&source={source}POWER_VIEW"
    public_key_signature = hashlib.md5(public_key_signature_input.encode()).hexdigest()

    # Get public key to encode token with
    response = requests.get(
        f'https://{json_settings["API_Server"]}/anonymous/publicKey',
        params={
            'source': source,
            'nonce': public_key_nonce,
            'sign': public_key_signature
        }
    )

    public_key_string = response.json()['data']

    # Write public key file
    public_key_file = StringIO()
    public_key_file.writelines(
        [
            '-----BEGIN PUBLIC KEY-----',
            public_key_string,
            '-----END PUBLIC KEY-----'
        ]
    )
    public_key_file.seek(0)

    # Load public key
    public_key = load_pem_public_key(
        bytes(public_key_file.read(), encoding='utf-8'),
    )

    encrypted_password = base64.b64encode(public_key.encrypt(
        json_settings['sunsynk_pass'].encode('utf-8'),
        padding=PKCS1v15()
    )).decode('utf-8')

    token_nonce = get_nonce()
    token_sign_string = f'nonce={token_nonce}&source=sunsynk{public_key_string[:10]}'
    token_sign = md5(token_sign_string.encode()).hexdigest()

    # API URL
    url = f'https://{json_settings["API_Server"]}/oauth/token/new'
    # Prepare request payload
    payload = {
        "client_id": "csp-web",
        "grant_type": "password",
        "password": encrypted_password,
        "source": source,
        "username": json_settings['sunsynk_user'],
        'nonce': token_nonce,
        'sign': token_sign
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
