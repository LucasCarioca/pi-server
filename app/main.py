import uvicorn
from typing import Optional
from sensors.humidity_temperature import get_humidity_and_temperature
from fastapi import FastAPI
import json

config_file = open("./config.json")
config = json.load(config_file)
app = FastAPI()
config_file.close()

@app.get("/")
def read_root():
    #humidity, temperature = get_humidity_and_temperature()
    return {"server": config["name"], "room": config["room"]}

@app.get("/climate")
def read_climate():
    temp, humidity = get_humidity_and_temperature()
    return {"temp": temp, "humidity": humidity}

@app.get("/config")
def read_config():
    return config

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
