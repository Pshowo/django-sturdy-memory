#!/usr/bin/env python
import psutil
import time
import requests
from requests.structures import CaseInsensitiveDict

def send():

# count = 0
# while True:
    CPU = int(psutil.cpu_percent())
    ram_total = psutil.virtual_memory().total
    ram_percent = psutil.virtual_memory().percent
    ram_used = round(psutil.virtual_memory().used / 1073741824, 2)
    ram_total_GB = round(ram_total / 1073741824, 2)
    RAM = ram_total_GB
    data = {"proj_num": 1, "cpu": CPU, "ram_used": ram_used, "ram_percent": ram_percent, "is_active": True}
    headers = CaseInsensitiveDict()
    headers["Authenticator"] = "Token 16d6a3d4-8926-4729-a225-de60cf31bca7"
    res = requests.post(f"http://127.0.0.1:8000/api/ds/", json=data, headers=headers )
    print("Count:\n", res.json(), "\n")
    print(res.status_code)

    time.sleep(3)
send()