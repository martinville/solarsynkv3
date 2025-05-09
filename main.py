import gettoken
import getapi
import postapi
import settingsmanager
import os
import json
import requests
import threading
import logging
import traceback
from datetime import datetime

# Define console colors for readability
class ConsoleColor:    
    OKBLUE = "\033[34m"
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"        
    MAGENTA = "\033[35m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"    

# Configure logging
logging.basicConfig(filename="solar_script.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Get current date & time
VarCurrentDate = datetime.now()

# Load settings from JSON file
try:
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
except Exception as e:
    logging.error(f"Failed to load settings: {e}")
    print(ConsoleColor.FAIL + "Error loading settings.json. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
    exit()

# Retrieve inverter serials
inverterserials = str(json_settings['sunsynk_serial']).split(";")

# Function to safely fetch data using threading
def fetch_data(api_function, BearerToken, serialitem, description):
    try:
        print(f"{ConsoleColor.WARNING}Fetching {description}...{ConsoleColor.ENDC}")
        api_function(BearerToken, str(serialitem))
    except Exception as e:
        logging.error(f"Error fetching {description}: {e}")
        print(ConsoleColor.FAIL + f"Error fetching {description}: {e}" + ConsoleColor.ENDC)
        print(traceback.format_exc())

# Iterate through all inverters
for serialitem in inverterserials:
    print("------------------------------------------------------------------------------")
    print("-- " + ConsoleColor.MAGENTA + f"SolarSynkV3 - Getting {serialitem} @ {VarCurrentDate}" + ConsoleColor.ENDC)
    print("------------------------------------------------------------------------------")    
    print("Script refresh rate set to: " + ConsoleColor.OKCYAN + str(json_settings['Refresh_rate']) + ConsoleColor.ENDC + " milliseconds")

    # Get Bearer Token
    try:
        BearerToken = gettoken.gettoken()
        if not BearerToken:
            raise ValueError("Failed to retrieve Bearer Token. Check credentials or server status.")
    except Exception as e:
        logging.error(f"Token retrieval error: {e}")
        print(ConsoleColor.FAIL + "Error retrieving Bearer Token." + ConsoleColor.ENDC)
        print(traceback.format_exc())
        continue

    print("Cleaning cache...")
    settings_file = "settings.json"
    if os.path.exists(settings_file):
        os.remove(settings_file)
        print("Old settings.json file removed.")

    # Test API connection
    print(ConsoleColor.WARNING + "Testing HA API" + ConsoleColor.ENDC)
    varContest = postapi.ConnectionTest("TEST", "A", "current", "connection_test", "connection_test_current", "100")

    if varContest == "Connection Success":
        print(varContest)

        # Define API calls
        api_calls = [
            (getapi.GetInverterInfo, "Inverter Information"),
            (getapi.GetPvData, "PV Data"),
            (getapi.GetGridData, "Grid Data"),
            (getapi.GetBatteryData, "Battery Data"),
            (getapi.GetLoadData, "Load Data"),
            (getapi.GetOutputData, "Output Data"),
            (getapi.GetDCACTemp, "DC & AC Temperature Data")
        ]

        # Start threaded API calls
        threads = []
        for api_function, description in api_calls:
            thread = threading.Thread(target=fetch_data, args=(api_function, BearerToken, serialitem, description))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(ConsoleColor.OKGREEN + "All API calls completed successfully!" + ConsoleColor.ENDC)

        # Download and process inverter settings
        settingsmanager.DownloadSunSynkSettings(BearerToken, str(serialitem))
        settingsmanager.GetNewSettingsFromHAEntity(BearerToken, str(serialitem))

        # Clear old settings to prevent re-sending
        print("Cleaning out previous settings...")
        settingsmanager.ResetSettingsEntity(serialitem)

    else:
        print(ConsoleColor.FAIL + varContest + ConsoleColor.ENDC)
        print(ConsoleColor.MAGENTA + "Ensure correct IP, port, and Home Assistant accessibility." + ConsoleColor.ENDC)

    # Script completion time
    VarCurrentDate = datetime.now()
    print(f"Script completion time: {ConsoleColor.OKBLUE} {VarCurrentDate} {ConsoleColor.ENDC}") 

print(ConsoleColor.OKBLUE + "Script execution completed." + ConsoleColor.ENDC)
