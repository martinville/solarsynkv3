
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
                
            
            print(ConsoleColor.OKGREEN + "Settings download complete" + ConsoleColor.ENDC)
        
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
        
    
    try:
        # Corrected to use GET request
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
        parsed_inverter_json = response.json()
        
        #print(str(parsed_inverter_json))
        #print(str(parsed_inverter_json['state']))
        EntSettings = str(parsed_inverter_json['state']).split(";")
        print("The following settings were found in: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)        
        
        LoopCount=0        
        for EntSetting in EntSettings: 
            FormatToJSON = "{" + str(EntSetting) + "}"
            FormatToJSON = json.loads(FormatToJSON)

            JSON_Key = list(FormatToJSON.keys())[0]
            JSON_Value = FormatToJSON[JSON_Key]
            print(JSON_Key  + "-->" + JSON_Value)
            print(ConsoleColor.WARNING + DetermineSettingCategory(JSON_Key) + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
        print(f"You probably did not create the settings entity. Manually create it for inverter with serial " + ConsoleColor.OKCYAN + Serial + ConsoleColor.ENDC + " In the HA GUI in menu [Settings] -> [Devices & Services] -> [Helpers] tab -> [+ CREATE HELPER]. Choose [Text] and name it: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Home Assistant API response." + ConsoleColor.ENDC)        
        
        
def DetermineSettingCategory(JSON_Search_Key):
    #Determine the type of setting that is intended to be updated
    if JSON_Search_Key in ("absorptionVolt","battMode","batteryCap","batteryEfficiency","batteryEmptyV","batteryImpedance","batteryLowCap","batteryLowVolt","batteryMaxCurrentCharge","batteryMaxCurrentDischarge","batteryOn","batteryRestartCap","batteryRestartVolt","batteryShutdownCap","batteryShutdownVolt","bmsErrStop","disableFloatCharge","equChargeCycle","equChargeTime","equVoltCharge","floatVolt","genChargeOn","genSignal","generatorBatteryCurrent","generatorForcedStart","generatorStartCap","generatorStartVolt","gridSignal","lithiumMode","lowNoiseMode","lowPowerMode","safetyType","sdBatteryCurrent","sdChargeOn","sdStartCap","sdStartVol","sdStartVolt","signalIslandModeEnable","sn","tempco"):
        

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
        #with open("svr_settings.json", "r") as file:
        #    content = file.read()
        #print(content)  
        return("Battery Setting --> " + JSON_Search_Key + " updated" )




def merge_json_settings(source_file, target_file, output_file):
    import json
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
    
    return target_data

