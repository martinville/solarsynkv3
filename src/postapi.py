import json
import os
import requests
import urllib3

from config.api import BASE_URL_HOME_ASSISTANT_CORE
from src.util import home_assistant_options
from src.util.console import ConsoleColor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get options
options = home_assistant_options.get()

# Get Home Assistant bearer token
home_assistant_bearer_token = os.getenv('SUPERVISOR_TOKEN')

def PostHAEntity(Serial,UOM,UOMLong,fName,sName,EntityVal):
    # API URL
    url = f"{BASE_URL_HOME_ASSISTANT_CORE}/states/sensor.solarsynkv3_" + Serial + '_' + sName

    if UOM == "kWh":
        payload = {"attributes": {"device_class": f"{UOMLong}", "state_class":"total_increasing", "last_reset":"None", "unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}
    else:
        payload = {"attributes": {"device_class": f"{UOMLong}", "state_class":"measurement", "unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}
        
    
    # Headers
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {home_assistant_bearer_token}"}
    try:
        # Send POST request with timeout (10s)
        response = requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        # Parse response
        parsed_login_json = response.json()
        #print(parsed_inverter_json)
        # Check login status
        if len(parsed_login_json['entity_id']) > 1:
            #print("Sunsynk Login: " + ConsoleColor.OKGREEN + parsed_login_json + ConsoleColor.ENDC)
            print("HA Entity: " + ConsoleColor.WARNING + parsed_login_json['entity_id'] +":" + ConsoleColor.OKCYAN + f" {EntityVal} {UOM}" + ConsoleColor.ENDC + ConsoleColor.OKGREEN + " OK" + ConsoleColor.ENDC )
            
            

        else:
            print(parsed_inverter_json)

    except requests.exceptions.Timeout:
            print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)
     

    except requests.exceptions.RequestException as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
     

    except json.JSONDecodeError:
            print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)    


def ConnectionTest(Serial,UOM,UOMLong,fName,sName,EntityVal):
    # API URL
    url = f"{BASE_URL_HOME_ASSISTANT_CORE}/states/sensor.solarsynkv3_" + Serial + '_' + sName

    payload = {"attributes": {"device_class": f"{UOMLong}", "state_class":"measurement", "unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}

    # Headers
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {home_assistant_bearer_token}"}
    try:
        # Send POST request with timeout (10s)
        response = requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        # Parse response
        parsed_login_json = response.json()

        # Check login status
        if len(parsed_login_json['entity_id']) > 1:
            print("HA Entity: " + ConsoleColor.WARNING + parsed_login_json['entity_id'] +":" + ConsoleColor.OKCYAN + f" {EntityVal} {UOM}" + ConsoleColor.ENDC + ConsoleColor.OKGREEN + " OK" + ConsoleColor.ENDC )
            return "Connection Success"
            

        else:
            print(parsed_inverter_json)

    except requests.exceptions.Timeout:
            print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)
            return "Connection Failed using URL: " + url

    except requests.exceptions.RequestException as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
            return "Connection Failed using URL: " + url
     

    except json.JSONDecodeError:
            print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC) 
            return "Connection Failed using URL: " + url
