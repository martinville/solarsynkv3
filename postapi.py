from src.clients.home_assistant_client import HomeAssistantClient


def PostHAEntity(Serial,UOM,UOMLong,fName,sName,EntityVal):
    import json
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"

    home_assistant_client = HomeAssistantClient()

    if UOM == "kWh":
        payload = {
            "attributes": {
                "device_class": f"{UOMLong}",
                "state_class": "total_increasing",
                "last_reset": "None",
                "unit_of_measurement": f"{UOM}",
                "friendly_name": f"{fName}"
            },
            "state": f"{EntityVal}"}
    else:
        payload = {
            "attributes": {
                "device_class": f"{UOMLong}",
                "state_class": "measurement",
                "unit_of_measurement": f"{UOM}",
                "friendly_name": f"{fName}"
            }, "state": f"{EntityVal}"
        }

    try:
        response = home_assistant_client.post("/api/states/sensor.solarsynkv3_" + Serial + '_' + sName, payload)

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
    import json
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"

    home_assistant_client = HomeAssistantClient()

    path = "/api/states/sensor.solarsynkv3_" + Serial + '_' + sName
    payload = {
        "attributes": {
            "device_class": f"{UOMLong}",
            "state_class": "measurement",
            "unit_of_measurement": f"{UOM}",
                       "friendly_name": f"{fName}"
        },
        "state": f"{EntityVal}"
    }

    try:
        response = home_assistant_client.post(path, payload)

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
            return "Connection Success"
        else:
            print(parsed_inverter_json)

    except requests.exceptions.Timeout:
            print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)
            return "Connection Failed using URL: " + path

    except requests.exceptions.RequestException as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
            return "Connection Failed using URL: " + path


    except json.JSONDecodeError:
            print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)
            return "Connection Failed using URL: " + path
