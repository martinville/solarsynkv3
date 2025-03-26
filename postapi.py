import json
import requests
import urllib3
import logging

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(filename="ha_api.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Console Colors
class ConsoleColor:    
    OKBLUE = "\033[34m"
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"        
    MAGENTA = "\033[35m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m" 

# Load Home Assistant settings
def load_settings():
    try:
        with open('/data/options.json') as options_file:
            return json.load(options_file)
    except Exception as e:
        logging.error(f"Failed to load settings: {e}")
        print(ConsoleColor.FAIL + "Error loading options.json. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
        return None

# Unified function to post to Home Assistant API
def post_to_ha(Serial, UOM, UOMLong, fName, sName, EntityVal, test_mode=False):
    settings = load_settings()
    if not settings:
        return "Settings Load Failed"

    # Set up connection parameters
    protocol = "https" if settings['Enable_HTTPS'] else "http"
    ha_url = f"{protocol}://{settings['Home_Assistant_IP']}:{settings['Home_Assistant_PORT']}"
    entity_url = f"{ha_url}/api/states/sensor.solarsynkv3_{Serial}_{sName}"
    token = settings['HA_LongLiveToken']

    # Define payload
    state_class = "total_increasing" if UOM == "kWh" else "measurement"
    payload = {
        "attributes": {
            "device_class": UOMLong,
            "state_class": state_class,
            "unit_of_measurement": UOM,
            "friendly_name": fName
        },
        "state": EntityVal
    }

    # Headers
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    try:
        # Send POST request with a 10s timeout
        response = requests.post(entity_url, json=payload, headers=headers, timeout=10, verify=False)
        response.raise_for_status()  # Raise exception for HTTP errors

        parsed_response = response.json()

        # Check if response contains 'entity_id'
        if 'entity_id' in parsed_response:
            print(f"HA Entity: {ConsoleColor.WARNING}{parsed_response['entity_id']}:{ConsoleColor.OKCYAN} {EntityVal} {UOM}{ConsoleColor.ENDC} {ConsoleColor.OKGREEN}OK{ConsoleColor.ENDC}")
            logging.info(f"HA Entity Updated: {parsed_response['entity_id']} - {EntityVal} {UOM}")
            return "Connection Success" if test_mode else "Post Success"
        else:
            logging.warning(f"Unexpected response: {parsed_response}")
            return "Unexpected Response"

    except requests.exceptions.Timeout:
        logging.error(f"Timeout error while connecting to {entity_url}")
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)
        return f"Connection Failed using URL: {entity_url}"

    except requests.exceptions.RequestException as e:
        logging.error(f"Connection error: {e}")
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
        return f"Connection Failed using URL: {entity_url}"

    except json.JSONDecodeError:
        logging.error("Failed to parse Home Assistant API response")
        print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)
        return f"Connection Failed using URL: {entity_url}"

# Function for Connection Test
def ConnectionTest(Serial, UOM, UOMLong, fName, sName, EntityVal):
    return post_to_ha(Serial, UOM, UOMLong, fName, sName, EntityVal, test_mode=True)
