import gettoken
import getapi
import postapi
import settingsmanager
import os
import requests
import threading
import logging
import traceback
from datetime import datetime

from config.api import SOLAR_BASE_URLS
from util import solar_sync_logging, home_assistant_options
from util.console import ConsoleColor

# Configure logging to
solar_sync_logging.configure()

# Get options
options = home_assistant_options.get()

# Determine base URL based on data source
data_source=options["data_source"]
base_url=SOLAR_BASE_URLS.get(data_source)

# Retrieve inverter serials
inverter_serials = str(options['sunsynk_serial']).split(";")

# Get Bearer Token
try:
    BearerToken = gettoken.gettoken(base_url, options['sunsynk_user'], options['sunsynk_pass'])
    if not BearerToken:
        raise ValueError("Failed to retrieve Bearer Token. Check credentials or server status.")
except Exception as e:
    logging.error(f"Token retrieval error: {e}")
    print(ConsoleColor.FAIL + "Error retrieving Bearer Token." + ConsoleColor.ENDC)
    print(traceback.format_exc())
    exit(1)

# Function to safely fetch data using threading
def fetch_data(api_function, base_url, BearerToken, serialitem, description):
    try:
        print(f"{ConsoleColor.WARNING}Fetching {description}...{ConsoleColor.ENDC}")
        api_function(base_url, BearerToken, str(serialitem))
    except Exception as e:
        logging.error(f"Error fetching {description}: {e}")
        print(ConsoleColor.FAIL + f"Error fetching {description}: {e}" + ConsoleColor.ENDC)
        print(traceback.format_exc())

# Iterate through all inverters
timestamp = datetime.now()
for serialitem in inverter_serials:
    print("------------------------------------------------------------------------------")
    print("-- " + ConsoleColor.MAGENTA + f"SolarSynkV3 - Getting {serialitem} @ {timestamp}" + ConsoleColor.ENDC)
    print("------------------------------------------------------------------------------")    
    print("Script refresh rate set to: " + ConsoleColor.OKCYAN + str(options['Refresh_rate']) + ConsoleColor.ENDC + " milliseconds")

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
            thread = threading.Thread(target=fetch_data, args=(api_function, base_url, BearerToken, serialitem, description))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(ConsoleColor.OKGREEN + "All API calls completed successfully!" + ConsoleColor.ENDC)

        # Download and process inverter settings
        settingsmanager.DownloadSunSynkSettings(base_url, BearerToken, str(serialitem))
        settingsmanager.GetNewSettingsFromHAEntity(base_url, BearerToken, str(serialitem))

        # Clear old settings to prevent re-sending
        print("Cleaning out previous settings...")
        settingsmanager.ResetSettingsEntity(serialitem)

    else:
        print(ConsoleColor.FAIL + varContest + ConsoleColor.ENDC)
        print(ConsoleColor.MAGENTA + "Ensure correct IP, port, and Home Assistant accessibility." + ConsoleColor.ENDC)

    # Script completion time
    timestamp = datetime.now()
    print(f"Script completion time: {ConsoleColor.OKBLUE} {timestamp} {ConsoleColor.ENDC}")

print(ConsoleColor.OKBLUE + "Script execution completed." + ConsoleColor.ENDC)
