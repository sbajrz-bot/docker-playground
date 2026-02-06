import logging
import time
from datetime import datetime

# Set up logging
log_directory = "/app/hostlogs"
log_file = "/app/hostlogs/apphost.log"
print(log_directory)
print(log_directory)
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
        logging.info("This is a log entry for host writable layer.")
        print("Log written ")
        time.sleep(30)  # Wait for 1 minute before writing next log

if __name__ == "__main__":
    write_log()