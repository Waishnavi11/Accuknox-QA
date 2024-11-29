import requests
import logging
from datetime import datetime
import time


APP_URL = "https://www.google.co.in/"  
EXPECTED_STATUS_CODE = 200  


CHECK_INTERVAL = 60  

logging.basicConfig(
    filename='application_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_application():
    try:
        response = requests.get(APP_URL, timeout=10)
        if response.status_code == EXPECTED_STATUS_CODE:
            logging.info(f"Application is UP. Status Code: {response.status_code}")
            print(f"Application is UP. Status Code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status Code: {response.status_code}")
            print(f"Application is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {e}")
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    logging.info("Starting Application Health Checker")
    while True:
        check_application()
        time.sleep(CHECK_INTERVAL)
