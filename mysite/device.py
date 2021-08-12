#!/usr/bin/env python
import psutil
import time
import requests


count = 0
while True:
    CPU = int(psutil.cpu_percent())
    ram_total = psutil.virtual_memory().total
    ram_percent = psutil.virtual_memory().percent
    ram_used = round(psutil.virtual_memory().used / 1073741824, 2)
    ram_total_GB = round(ram_total / 1073741824, 2)
    RAM = ram_total_GB
    data = {"proj_num": 25, "cpu": CPU, "ram_used": ram_used, "ram_percent": ram_percent, "is_active": True}
    # res = requests.post("http://127.0.0.1:8000/versions/api/test/", json={"id": 3, "CPU": CPU, "RAM":RAM, "RAM_USE": ram_used, "RAM_PER": ram_percent} )
    res = requests.post(f"http://127.0.0.1:8000/api/ds/", json=data )
    print(f"Count: {count}\n", res.json(),"\n")
    count += 1
    # print("CPU: ", CPU)
    # print("Ram total: ", str(round(ram_total_GB, 2)) + " GB")
    # print("Ram used: ", str(round(ram_used, 2)) + " GB")
    # print("Ram: ", str(round(ram_percent, 2)) + " %\n")

    time.sleep(3)
