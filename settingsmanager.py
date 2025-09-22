import postapi

#################################################################################################################################################
## NOTES on the workflow
## Steps
## 1.  Dump all existing inverter settings from server to file --> svr_settings.json
## 2.  Start the process to get settings from HA set by user
## 3a. Build Battery settings template and merge existing server settings into the template *This is just prep, settings from user not yet populated" 
## 3b. Build System mode settings template and merge existing server settings into the template *This is just prep, settings from user not yet populated" 
## 4.  Fetch user settings from HA Entity --> /api/states/input_text.solarsynkv3 and iterate through each user provided setting.
## 5.  Check each setting provided by user and determine in which category the setting is from and pass both the setting and value I.E Battery, System mode
## 6.  Open the previously merged setting file and then populate the setting if found in the settings category.
#################################################################################################################################################

#Get server provider settings and save to file settings_serial.json
import json
import requests
from datetime import datetime
import urllib3

from src.clients.home_assistant_client import HomeAssistantClient
from src.settings.converter.settings_converter import SettingsConverter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load settings from JSON file
try:
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
        api_server = json_settings['API_Server']
except Exception as e:
    logging.error(f"Failed to load settings: {e}")
    print(ConsoleColor.FAIL + "Error loading settings.json. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
    exit()
    
class ConsoleColor:    
    OKBLUE = "\033[34m"
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"        
    MAGENTA = "\033[35m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m" 
        
        
def DownloadProviderSettings(Token,Serial):
    global api_server
    inverter_url = f"https://{api_server}/api/v1/common/setting/{Serial}/read"
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
        #print(parsed_inverter_json)

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Settings fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(str(parsed_inverter_json))
            with open("svr_settings.json", "w") as file:
                json.dump(parsed_inverter_json, file, indent=4)
                
            
            print(ConsoleColor.OKGREEN + "Settings download from provider complete" + ConsoleColor.ENDC)
        
        else:
            print("Settings fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse provider API response." + ConsoleColor.ENDC) 
        
def GetNewSettingsFromHAEntity(SunSynkToken,Serial):
    global api_server

    home_assistant_client = HomeAssistantClient()

    #Build Local Settings Templates (Later we will inject settings from the HA entity)
    print(ConsoleColor.WARNING +  BuildLocalBatterySettings() + ConsoleColor.ENDC)
    print(ConsoleColor.WARNING +  BuildLocalSystemModeSettings() + ConsoleColor.ENDC)

    try:
        # GET HA Settings from entity
        response = home_assistant_client.get("/states/input_text.solarsynkv3_" + Serial + '_settings')
        response.raise_for_status()
        parsed_inverter_json = response.json()
        
        #print(str(parsed_inverter_json))
        #print(str(parsed_inverter_json['state']))

        RawSettings = str(parsed_inverter_json['state'])

        # change to enable short settings
        RawSettings = SettingsConverter().convert(RawSettings)

        EntSettings = RawSettings.split(";")

        #print("The following settings were found in: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)
        LoopCount=0 
        LastSettingsType=""
        for EntSetting in EntSettings: 
            #LoopCount=LoopCount+1
            #print(LoopCount)
            FormatToJSON = "{" + str(EntSetting) + "}"
            if FormatToJSON != "{}":
                FormatToJSON = json.loads(FormatToJSON)
    
                JSON_Key = list(FormatToJSON.keys())[0]
                JSON_Value = FormatToJSON[JSON_Key]

                #Determine setting type and edit JSON after downloading an populating with existing settings
                LastSettingsType = DetermineSettingCategory(JSON_Key,JSON_Value)
            else:
                print("No settings to process")
            
        if LastSettingsType ==  "Valid Battery Setting":
            PostSettingToSunSynk(SunSynkToken,Serial,"Battery Settings")
        if LastSettingsType ==  "Valid SystemMode Setting":
            PostSettingToSunSynk(SunSynkToken,Serial,"SystemMode Settings")            
        
        
    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Home Assistant API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant API. {e}" + ConsoleColor.ENDC)
        print(f"You probably did not create the settings entity. Manually create it for inverter with serial " + ConsoleColor.OKCYAN + Serial + ConsoleColor.ENDC + " In the HA GUI in menu [Settings] -> [Devices & Services] -> [Helpers] tab -> [+ CREATE HELPER]. Choose [Text] and name it: " + ConsoleColor.OKCYAN  +  "solarsynkv3_" + Serial + "_settings" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.MAGENTA + "Notice: Invalid or no settings found to post back to sunsynk. This is not a critical error, it just means that the settings you provided in the settings entity (/api/states/input_text.solarsynkv3_" + Serial + "_settings) is invalid or blank. If this is intentional just ignore." + ConsoleColor.ENDC)                
        
def DetermineSettingCategory(JSON_Search_Key,JSON_Search_Key_val):    
    global api_server
    #Determine the type of setting that is intended to be updated and inject the value into the merged json file previously created.
    #Example Setting: "batteryCap":"97"
    
    #Battery Settings
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
            
        #Fix file by replacing "true" with true
        ReplaceTRUE('merged_systemmode_settings.json')            
        return("Valid Battery Setting")
        exit()
    
    #System Mode Settings
    if JSON_Search_Key in ("sn","safetyType","battMode","solarSell","pvMaxLimit","energyMode","peakAndVallery","sysWorkMode","sellTime1","sellTime2","sellTime3","sellTime4","sellTime5","sellTime6","sellTime1Pac","sellTime2Pac","sellTime3Pac","sellTime4Pac","sellTime5Pac","sellTime6Pac","cap1","cap2","cap3","cap4","cap5","cap6","sellTime1Volt","sellTime2Volt","sellTime3Volt","sellTime4Volt","sellTime5Volt","sellTime6Volt","zeroExportPower","solarMaxSellPower","mondayOn","tuesdayOn","wednesdayOn","thursdayOn","fridayOn","saturdayOn","sundayOn","time1on","time2on","time3on","time4on","time5on","time6on","genTime1on","genTime2on","genTime3on","genTime4on","genTime5on","genTime6on"):
        
        print("System Mode Setting update request detected for: " + JSON_Search_Key + "-->" + JSON_Search_Key_val)
        # Load the JSON data from a file
        with open('merged_systemmode_settings.json', 'r') as file:
            data = json.load(file)
    
        
        #Update Object           
        data[JSON_Search_Key] = JSON_Search_Key_val
       
        # Save the modified data back to the JSON file
        with open('merged_systemmode_settings.json', 'w') as file:
            json.dump(data, file, indent=2)  # 'indent' for pretty-printing        
        
        #Fix file by replacing "true" with true
        ReplaceTRUE('merged_systemmode_settings.json')
        
        #DEBUG Read contents of newlybuilt systemmode_settings file
        #with open('merged_systemmode_settings.json', "r") as file:
        #    content = file.read()
        #    print(content)           
        return("Valid SystemMode Setting")      
        exit()        
    
def PostSettingToSunSynk(Token,Serial,SettingsType):
    print("Posting Settings to Inverter")
    global api_server    
    if SettingsType == "Battery Settings":        
        inverter_url = f"https://{api_server}/api/v1/common/setting/{Serial}/set"
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

    if SettingsType == "SystemMode Settings":        
        inverter_url = f"https://{api_server}/api/v1/common/setting/{Serial}/set"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Token}"
        }
        try:
            with open("merged_systemmode_settings.json", "r") as file:
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
    global api_server

    home_assistant_client = HomeAssistantClient()

    path = "/states/input_text.solarsynkv3_" + Serial + '_settings'
    payload = {"attributes": {"unit_of_measurement": ""}, "state": ""}

    #BOF CHECK IF SETTINGS HELPER EXIST
    #try:
    #    response = requests.get(path, timeout=5)
    #    if response.status_code == 404:
    #        print(ConsoleColor.FAIL + f"Error: Failed to connect to Home Assistant Settings via API. {e} settings will not be flushed out." + ConsoleColor.ENDC)
    #    else:
    #        print(f"URL exists (Status code: {response.status_code}) Settings may be flushed.")            
    #        SettingsExist=True
    #except requests.RequestException as e:
    #    print(ConsoleColor.OKGREEN + f"Error connecting: {e}" + ConsoleColor.ENDC)    
    #EOF CHECK IF SETTINGS HELPER EXIST    
    
    try:
        # Send POST request with timeout (10s)
        response = home_assistant_client.post(path, payload)

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
    global api_server
    #Build Local copy of settings template
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
    #with open(output_file, "r") as file:
    #    content = file.read()
    #    print(content)         
    
    #return target_data          
    return("File: merged_battery_settings.json built successfully." )    

def BuildLocalSystemModeSettings():
    global api_server
    #Build Local copy of settings template
    BuildSystemModeSettingJSON="{"
    ArrsySystemMode_settings = ["sn","safetyType","battMode","solarSell","pvMaxLimit","energyMode","peakAndVallery","sysWorkMode","sellTime1","sellTime2","sellTime3","sellTime4","sellTime5","sellTime6","sellTime1Pac","sellTime2Pac","sellTime3Pac","sellTime4Pac","sellTime5Pac","sellTime6Pac","cap1","cap2","cap3","cap4","cap5","cap6","sellTime1Volt","sellTime2Volt","sellTime3Volt","sellTime4Volt","sellTime5Volt","sellTime6Volt","zeroExportPower","solarMaxSellPower","mondayOn","tuesdayOn","wednesdayOn","thursdayOn","fridayOn","saturdayOn","sundayOn","time1on","time2on","time3on","time4on","time5on","time6on","genTime1on","genTime2on","genTime3on","genTime4on","genTime5on","genTime6on"]
    for Item_SystemMode_setting in ArrsySystemMode_settings:
        #print(Item_SystemMode_setting)
        BuildSystemModeSettingJSON=BuildSystemModeSettingJSON + '"' + Item_SystemMode_setting + '" : "",'
                
    BuildSystemModeSettingJSON = BuildSystemModeSettingJSON[:-1]
    BuildSystemModeSettingJSON = BuildSystemModeSettingJSON + "}"
    
        #print(BuildSystemModeSettingJSON)
    # Open file systemmode_settings. in write mode ("w" overwrites existing content)
    with open("systemmode_settings.json", "w") as file:
        file.write(BuildSystemModeSettingJSON)           

    #DEBUG Read contents of newlybuilt systemmode_settings file
    #with open("systemmode_settings.json", "r") as file:
    #    content = file.read()
    #    print(content)  
    
    ####################################################################################################
    #### Merge server settings with local settings file.    
    ####################################################################################################
    source_file = "svr_settings.json"
    target_file = "systemmode_settings.json"
    output_file = "merged_systemmode_settings.json"    
    
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
    #DEBUG Read contents of newlybuilt systemmode_settings file
    #with open(output_file, "r") as file:
    #    content = file.read()
    #    print(content)         
    
    #return target_data          
    return("File: merged_systemmode_settings.json built successfully." ) 


def ReplaceTRUE(fileName):
    # Open and read the JSON file
    with open('merged_systemmode_settings.json', 'r') as file:
        data = json.load(file)

    # Replace all "true" strings with boolean true
    data = replace_string_true_with_boolean(data)

    # Write the updated JSON back to the file
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=2)

#Replace "true" with true    
def replace_string_true_with_boolean(obj):
    if isinstance(obj, dict):
        return {k: replace_string_true_with_boolean(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_string_true_with_boolean(item) for item in obj]
    elif obj == "true":
        return True
    else:
        return obj


