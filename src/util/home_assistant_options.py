import json
import logging

from .console import ConsoleColor
from ..config.home_assistant import OPTIONS_JSON_PATH_HOME_ASSISTANT


def get():
    # Load settings from home assistant
    try:
        with open(OPTIONS_JSON_PATH_HOME_ASSISTANT) as options_file:
            json_settings = json.load(options_file)
    except Exception as e:
        logging.error(f"Failed to load options: {e}")
        print(
            ConsoleColor.FAIL + f"Error loading {OPTIONS_JSON_PATH_HOME_ASSISTANT}. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
        exit()

    return json_settings
