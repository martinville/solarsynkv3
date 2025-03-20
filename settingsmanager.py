
def GetSettings(Token,Serial):
    import json
    import requests
    from datetime import datetime
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m" 
        
    inverter_url = f"https://api.sunsynk.net/api/v1/common/setting/{Serial}/read"
    # Headers (Fixed Bearer token format)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Settings fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(str(parsed_inverter_json))
            with open("settings.json", "w") as file:
                file.write(str(parsed_inverter_json))
                
            
            print(ConsoleColor.OKGREEN + "Settings download complete" + ConsoleColor.ENDC)
        
        else:
            print("Settings fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)         

def GetNewSettings(SunSynkToken,Serial):
    import json
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
    # solarsynkv3_ 2302246241_settings
    #CheckEntity=$(curl -s -k -X GET -H "Authorization: Bearer $HA_LongLiveToken" -H "Content-Type: application/json"  $HTTP_Connect_Type://$Home_Assistant_IP:$Home_Assistant_PORT/api/states/input_text.solarsynk_"$inverter_serial"_inverter_settings | jq -r '.message')

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
        HaToken = json_settings['HA_LongLiveToken']

        if json_settings['Enable_HTTPS']:
            httpurl_proto = "https"
        else:
            httpurl_proto = "http"

        headers = {"Content-Type": "application/json","Authorization": f"Bearer {HaToken}"}  
        url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(json_settings['Home_Assistant_PORT']) + "/api/states/input_text.solarsynkv3_" + Serial + '_settings'
        
        #print(str(url))
        #print(str(headers))
        
    
    try:
        # Corrected to use GET request
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        
        #print(str(parsed_inverter_json))
        #print(str(parsed_inverter_json['state']))
        EntSettings = str(parsed_inverter_json['state']).split(";")
        print("The following settings were found in: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)        
        for EntSetting in EntSettings: 
            print(str(EntSetting))
            EntSettingVals = str(EntSetting).split(":")
            for EntSettingVal in EntSettingVals:
                #Put repeating code here
                print(EntSettingVal)
                # Load the settings file to be modified data from a file
                with open('settings.json', 'r') as file:
                    data = json.load(file)
                # Modify the data (example: add a new key-value pair)
                data[EntSetting]['EntSettingVal'] = "00:00"            
                # Save the modified data back to file
                with open('settings.json', 'w') as file:
                    json.dump(data, file, indent=2)  # 'indent' for pretty-printing                

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
        print(f"You probably did not create the settings entity. Manually create it for inverter with serial " + ConsoleColor.OKCYAN + Serial + ConsoleColor.ENDC + " In the HA GUI in menu [Settings] -> [Devices & Services] -> [Helpers] tab -> [+ CREATE HELPER]. Choose [Text] and name it: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)        
        
        
