"""logging constructor!"""
import os
import sys
import logging

LOGGING_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
LOG_DIR = "logs"
LOG_FILE_PATH = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format = LOGGING_STR, 
    handlers = [
        logging.FileHandler(LOG_FILE_PATH), 
        logging.StreamHandler(sys.stdout)
        ]
)
logger = logging.getLogger("textSummarizerLogger")
