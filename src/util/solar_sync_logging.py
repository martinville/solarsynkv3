import logging

from src.config.logging import LOG_FILE_NAME

# Configure logging to file
def configure():
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")