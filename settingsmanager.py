import postapi
def DownloadSunSynkSettings(Token,Serial):
    #Set sunsynk settings and save to file settings_serial.json
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
            with open("svr_settings.json", "w") as file:
                json.dump(parsed_inverter_json, file, indent=4)
                
            
            print(ConsoleColor.OKGREEN + "Settings download from synsynk complete" + ConsoleColor.ENDC)
        
        else:
            print("Settings fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC) 
        

def GetNewSettingsFromHAEntity(SunSynkToken,Serial):
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
      
    #Build Local Battery Settings 
    print(ConsoleColor.WARNING +  BuildLocalBatterySettings() + ConsoleColor.ENDC)
    
    try:
        # Corrected to use GET request
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        
        #print(str(parsed_inverter_json))
        #print(str(parsed_inverter_json['state']))
        
        EntSettings = str(parsed_inverter_json['state']).split(";")
        EntSettingsCount = len(EntSettings)
        print("The following settings were found in: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)                
        if EntSettingsCount > 0 :
            LoopCount=0        
            for EntSetting in EntSettings: 
                FormatToJSON = "{" + str(EntSetting) + "}"
                FormatToJSON = json.loads(FormatToJSON)
    
                JSON_Key = list(FormatToJSON.keys())[0]
                JSON_Value = FormatToJSON[JSON_Key]
                #print(JSON_Key  + "-->" + JSON_Value)
                #Determine setting type and edit JSON after downloading an populating with existing settings
                if DetermineSettingCategory(JSON_Key,JSON_Value) == "Valid Battery Setting":
                    PostSettingToSunSynk(SunSynkToken,Serial,"Battery Settings") 
                
        
        
    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
        print(f"You probably did not create the settings entity. Manually create it for inverter with serial " + ConsoleColor.OKCYAN + Serial + ConsoleColor.ENDC + " In the HA GUI in menu [Settings] -> [Devices & Services] -> [Helpers] tab -> [+ CREATE HELPER]. Choose [Text] and name it: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.MAGENTA + "Notice: Invalid or no settings found to post back to sunsynk. This is not a critical error, it just means that the settings you provided in the settings entity (/api/states/input_text.solarsynkv3_" + Serial + "_settings) is invalid or blank. If this is intentional just ignore." + ConsoleColor.ENDC)        
        
        
def DetermineSettingCategory(JSON_Search_Key,JSON_Search_Key_val):    
    import json
    #Determine the type of setting that is intended to be updated
    #Example Setting: "batteryCap":"97"
    if JSON_Search_Key in ("absorptionVolt","battMode","batteryCap","batteryEfficiency","batteryEmptyV","batteryImpedance","batteryLowCap","batteryLowVolt","batteryMaxCurrentCharge","batteryMaxCurrentDischarge","batteryOn","batteryRestartCap","batteryRestartVolt","batteryShutdownCap","batteryShutdownVolt","bmsErrStop","disableFloatCharge","equChargeCycle","equChargeTime","equVoltCharge","floatVolt","genChargeOn","genSignal","generatorBatteryCurrent","generatorForcedStart","generatorStartCap","generatorStartVolt","gridSignal","lithiumMode","lowNoiseMode","lowPowerMode","safetyType","sdBatteryCurrent","sdChargeOn","sdStartCap","sdStartVol","sdStartVolt","signalIslandModeEnable","sn","tempco"):
        
        print("Battery Setting update request detected for: " + JSON_Search_Key + "-->" + JSON_Search_Key_val)
        # Load the JSON data from a file
        with open('merged_battery_settings.json', 'r') as file:
            data = json.load(file)

        # Modify the data (example: add a new key-value pair)
        data[JSON_Search_Key] = JSON_Search_Key_val

        # Save the modified data back to the JSON file
        with open('merged_battery_settings.json', 'w') as file:
            json.dump(data, file, indent=2)  # 'indent' for pretty-printing        
        return("Valid Battery Setting")
    #DEBUG Read contents of newlybuilt battery_settings file
    #with open("merged_battery_settings.json", "r") as file:
    #    content = file.read()
    #    print(content)
    #print("Processed ")




def PostSettingToSunSynk(Token,Serial,SettingsType):
    import json
    import requests
    
    class ConsoleColor:    
        OKBLUE = "\033[34m"
        OKCYAN = "\033[36m"
        OKGREEN = "\033[32m"        
        MAGENTA = "\033[35m"
        WARNING = "\033[33m"
        FAIL = "\033[31m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        
    
    if SettingsType == "Battery Settings":
        #curl -s -k -X POST -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://api.sunsynk.net/api/v1/common/setting/$inverter_serial/set
        inverter_url = f"https://api.sunsynk.net/api/v1/common/setting/{Serial}/set"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Token}"
        }
        try:
            with open("merged_battery_settings.json", "r") as file:
                payload = json.load(file)  # Load JSON content as a Python dictionary

            # Send POST request
            response = requests.post(inverter_url, json=payload, headers=headers, timeout=10)
            parsed_json_response = response.json()
            if parsed_json_response.get('msg') == "Success":                    
                # Print response
                #print(ConsoleColor.OKGREEN + "Server Rsponse:" + response.text +  ConsoleColor.ENDC)
                print(SettingsType + " updated with SunkSynk server response: " + ConsoleColor.OKGREEN + parsed_json_response['msg'] + ConsoleColor.ENDC)
            else:
                print("Update failed with SunkSynk response: " + ConsoleColor.FAIL +  parsed_json_response['msg'] + ConsoleColor.ENDC)
            

        except requests.exceptions.Timeout:
            print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Sunsynk API." + ConsoleColor.ENDC)

        except requests.exceptions.RequestException as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to Sunsynk API. {e}" + ConsoleColor.ENDC)

        except json.JSONDecodeError:
            print(ConsoleColor.FAIL + "Error: Failed to parse Sunsynk API response." + ConsoleColor.ENDC)  







def ResetSettingsEntity(Serial):
    #curl -s -k -X POST -H "Authorization: Bearer $HA_LongLiveToken" -H "Content-Type: application/json" -d '{"attributes": {"unit_of_measurement": "", "friendly_name": "solarsynk_inverter_settings"}, "state": ""}' $HTTP_Connect_Type://$Home_Assistant_IP:$Home_Assistant_PORT/api/states/input_text.solarsynk_"$inverter_serial"_inverter_settings > /dev/null
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
    
    url = f"{httpurl_proto}://" + str(json_settings['Home_Assistant_IP']) + ":" + str(json_settings['Home_Assistant_PORT']) + "/api/states/input_text.solarsynkv3_" + Serial + '_settings'
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {HAToken}"}    
    payload = {"attributes": {"unit_of_measurement": ""}, "state": ""}
    
    try:
        # Send POST request with timeout (10s)
        response = requests.post(url, json=payload, headers=headers, timeout=10, verify=False)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        # Parse response
        parsed_login_json = response.json()  
    
    except requests.exceptions.Timeout:
            print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)
     

    except requests.exceptions.RequestException as e:
            print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
     

    except json.JSONDecodeError:
            print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)     



def BuildLocalBatterySettings():
    import json
    #Build Local copy of settings (But formated in a way that it's ready for posting to Sunsynk)
    BuildBatterySettingJSON="{"
    ArrBattery_settings = ["absorptionVolt","battMode","batteryCap","batteryEfficiency","batteryEmptyV","batteryImpedance","batteryLowCap","batteryLowVolt","batteryMaxCurrentCharge","batteryMaxCurrentDischarge","batteryOn","batteryRestartCap","batteryRestartVolt","batteryShutdownCap","batteryShutdownVolt","bmsErrStop","disableFloatCharge","equChargeCycle","equChargeTime","equVoltCharge","floatVolt","genChargeOn","genSignal","generatorBatteryCurrent","generatorForcedStart","generatorStartCap","generatorStartVolt","gridSignal","lithiumMode","lowNoiseMode","lowPowerMode","safetyType","sdBatteryCurrent","sdChargeOn","sdStartCap","sdStartVol","sdStartVolt","signalIslandModeEnable","sn","tempco"]
    for Item_Battery_setting in ArrBattery_settings:
        #print(Item_Battery_setting)
        BuildBatterySettingJSON=BuildBatterySettingJSON + '"' + Item_Battery_setting + '" : "",'
                
    BuildBatterySettingJSON = BuildBatterySettingJSON[:-1]
    BuildBatterySettingJSON = BuildBatterySettingJSON + "}"
        #print(BuildBatterySettingJSON)
    # Open file battery_settings. in write mode ("w" overwrites existing content)
    with open("battery_settings.json", "w") as file:
        file.write(BuildBatterySettingJSON)           

    #DEBUG Read contents of newlybuilt battery_settings file
    #with open("battery_settings.json", "r") as file:
    #    content = file.read()
    #    print(content)  
    
    ####################################################################################################
    #### Merge server settings with local settings file.    
    ####################################################################################################
    source_file = "svr_settings.json"
    target_file = "battery_settings.json"
    output_file = "merged_battery_settings.json"    
    
    # Load the source JSON file    
    with open(source_file, 'r') as src:
        source_data = json.load(src)
    
    # Load the target JSON file
    with open(target_file, 'r') as tgt:
        target_data = json.load(tgt)
    
    # Ensure we're working with the "data" section of the source
    source_settings = source_data.get("data", {})
    
    # Iterate over the target keys and update them with source values if available
    for key in target_data:
        if key in source_settings:
            target_data[key] = source_settings[key]
    
    # Save the merged data to the output file
    with open(output_file, 'w') as out:
        json.dump(target_data, out, indent=4)
    #DEBUG Read contents of newlybuilt battery_settings file
    #with open("merged_battery_settings.json", "r") as file:
    #    content = file.read()
    #    print(content)         
    
    #return target_data          
    return("File: merged_battery_settings.json built successfully." )    
