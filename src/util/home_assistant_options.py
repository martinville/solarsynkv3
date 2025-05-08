import json
import os
import logging

from console import ConsoleColor


def get():
    # Load settings from home assistant
    config_path = os.getenv('CONFIG_PATH')
    try:
        with open(config_path) as options_file:
            json_settings = json.load(options_file)
    except Exception as e:
        logging.error(f"Failed to load options: {e}")
        print(
            ConsoleColor.FAIL + f"Error loading {config_path}. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
        exit()

    return json_settings
