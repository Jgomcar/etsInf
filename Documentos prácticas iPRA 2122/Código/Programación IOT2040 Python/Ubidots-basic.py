import time
import requests
import random

TOKEN = "BBFF-1XPBKOKLEBkJLD9bIk8FUdO2ZNEZi7"  # Put your TOKEN here
DEVICE_LABEL = "Demo"  # Put your device label here 
VARIABLE_LABEL_1 = "Demo"  # Put your first variable label here


def build_payload(variable_1):
    # Creates two random values for sending data
    value_1 = random.randint(1, 100)
    payload = {variable_1: value_1} 

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1)

    print("[INFO] Preparado para enviar datos.")
    post_request(payload)
    print("[INFO] FIN")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(5)