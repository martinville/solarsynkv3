import gettoken
import getapi
import postapi
import settingsmanager
import os


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

#Get Date Time
from datetime import datetime
VarCurrentDate = datetime.now()
# Load options from JSON file
with open('/data/options.json') as options_file:
   json_settings = json.load(options_file)
    
#Get Inverter serials to iterate through
inverterserials = str(json_settings['sunsynk_serial']).split(";")
for serialitem in inverterserials:    
    print("------------------------------------------------------------------------------")
    print("-- " + ConsoleColor.MAGENTA + f"SolarSynkV3 - Getting {serialitem} @ {VarCurrentDate}" + ConsoleColor.ENDC)
    print("------------------------------------------------------------------------------")    
    print("Script refresh rate set to: " + ConsoleColor.OKCYAN + str(json_settings['Refresh_rate']) + ConsoleColor.ENDC + " milliseconds")
    BearerToken=gettoken.gettoken()
    
    if BearerToken != "" :
        print("Cleaning cache...")        
        #os.remove("settings.json")
        #print(BearerToken)            
        

        
        print("--------------------------------------")
        print("--" + ConsoleColor.WARNING + "Getting Inverter Information")
        print("--------------------------------------")
        getapi.GetInverterInfo(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" + ConsoleColor.WARNING + "Getting PV Information")
        print("--------------------------------------")
        getapi.GetPvData(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" +  ConsoleColor.WARNING + "Getting GRID Information")
        print("--------------------------------------")
        getapi.GetGridData(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" +  ConsoleColor.WARNING + "Getting BATTERY Information")
        print("--------------------------------------")
        getapi.GetBatteryData(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" +  ConsoleColor.WARNING + "Getting LOAD Information")
        print("--------------------------------------")
        getapi.GetLoadData(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" +  ConsoleColor.WARNING + "Getting OUTPUT Information")
        print("--------------------------------------")
        getapi.GetOutputData(BearerToken,str(serialitem))
        print("--------------------------------------")
        print("--" +  ConsoleColor.WARNING + "Getting DC & AC Temperature  Information")
        print("--------------------------------------")
        getapi.GetDCACTemp(BearerToken,str(serialitem))
        
        #getapi.GetInverterSerials(BearerToken,str(serialitem))
        #settingsmanager.DownloadSunSynkSettings(BearerToken,str(serialitem))  
        #settingsmanager.GetNewSettingsFromHAEntity(BearerToken,str(serialitem)) 

        #source_file = "svr_settings.json"
        #target_file = "battery_settings.json"
        #output_file = "merged_battery_settings.json"        
        #settingsmanager.merge_json_settings(source_file, target_file, output_file)
        #DEBUG Read contents of newlybuilt battery_settings file
        #with open("merged_battery_settings.json", "r") as file:
        #    content = file.read()
        #print(content)          
        
        
        
        VarCurrentDate = datetime.now()
        print(f"Script completion time: {ConsoleColor.OKBLUE} {VarCurrentDate} {ConsoleColor.ENDC}") 
        
    else:
        print(f"Something went wrong for inverter serial: {serialitem}")






