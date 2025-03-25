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
    
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
        HAToken = json_settings['HA_LongLiveToken']

        if json_settings['Enable_HTTPS']:
            httpurl_proto = "https"
        else:
            httpurl_proto = "http"        

            
        #print(json_settings['Enable_HTTPS'])
        # API URL
        url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(json_settings['Home_Assistant_PORT']) + "/api/states/sensor.solarsynkv3_" + Serial + '_' + sName
        
        #print ("HAToken:" + HAToken)
        #payload = {"attributes": {"unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}        
        payload = {"attributes": {"last_reset": "None","device_class": f"{UOMLong}", "state_class":"measurement", "unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}
        #print(payload)
        
    
    # Headers
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {HAToken}"}
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
    
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
        HAToken = json_settings['HA_LongLiveToken']

        if json_settings['Enable_HTTPS']:
            httpurl_proto = "https"
        else:
            httpurl_proto = "http"        

            
        #print(json_settings['Enable_HTTPS'])
        # API URL
        url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(json_settings['Home_Assistant_PORT']) + "/api/states/sensor.solarsynkv3_" + Serial + '_' + sName
        
        #print ("HAToken:" + HAToken)
        #payload = {"attributes": {"unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}        
        payload = {"attributes": {"device_class": f"{UOMLong}", "state_class":"measurement", "unit_of_measurement": f"{UOM}", "friendly_name": f"{fName}"}, "state": f"{EntityVal}"}
        #print(payload)
        
    
    # Headers
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {HAToken}"}
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
