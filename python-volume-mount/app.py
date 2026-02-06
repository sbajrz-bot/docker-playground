import logging
import time
from datetime import datetime

# Set up logging
log_directory = "/app/mountpath/logs"
log_file = "/app/mountpath/logs/app.log"
print(log_directory)
print(log_file)
# Create logs directory if it doesn't exist
import os
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def write_log():
    while True:
        logging.info("This is a log entry for mountpth updated - test3")
        print("Log written ")
        time.sleep(30)  # Wait for 1 minute before writing next log

if __name__ == "__main__":
    write_log()