import uvicorn
from typing import Optional
from sensors.humidity_temperature import get_humidity_and_temperature
from fastapi import FastAPI
import json
import os

config_file = open("/home/pi/apps/server/app/config.json")
config = json.load(config_file)
app = FastAPI()
config_file.close()

@app.get("/")
def get_node_info():
    #humidity, temperature = get_humidity_and_temperature()
    return {"server": config["name"], "room": config["room"]}

@app.get("/climate")
def get_node_climate():
    temp, humidity = get_humidity_and_temperature()
    return {"temp": temp, "humidity": humidity}

@app.get("/config")
def get_node_config():
    return config

@app.get("/reboot")
def reboot_node():
    os.system("sudo reboot")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
