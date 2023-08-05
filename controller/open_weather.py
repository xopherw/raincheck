import requests as req, os
from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.openweathermap.org/data/2.5"
ow_key = os.getenv("OW_KEY")

def getWeatherNow(lat, lon, metric=True):
    path = "/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": ow_key,
        "units": "metric" if metric else "imperial"
    }
    r = req.get(base_url + path, params=params)
    data = r.json()
    weather = {
        "country" : data["sys"]["country"],
        "city": data["name"],
        "temp": data["main"]["temp"],
        "max" : data["main"]["temp_max"],
        "min" : data["main"]["temp_min"],
        "wind_speed": data["wind"]["speed"],
        "humidity": data["main"]["humidity"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["main"],
        "icon" : data["weather"][0]["icon"],
    }
    return weather

def getWeatherHourly(lat, lon, metric=True):
    path = "/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": ow_key,
        "units": "metric" if metric else "imperial"
    }
    r = req.get(base_url + path, params=params)
    data = r.json()
    weather_list = []
    # TODO:
    # Find a way to show only the future from date.now
    for i in data["list"]:
        meta_data ={
            "datetime" : i["dt_txt"],
            "temp" : i["main"]["temp"],
            "max" : i["main"]["temp_max"],
            "min" : i["main"]["temp_min"],
            "wind_speed": i["wind"]["speed"],
            "humidity": i["main"]["humidity"],
            "feels_like": i["main"]["feels_like"],
            "description": i["weather"][0]["main"],
            "icon" : i["weather"][0]["icon"]
        }
        weather_list.append(meta_data)

    weather = {
        "country" : data["city"]["country"],
        "city": data["city"]["name"],
        "list" : weather_list
    }
    return weather

def getWeatherDaily(lat, lon, metric=True):
    path = "/forecast/daily"
    params = {
        "lat": lat,
        "lon": lon,
        "cnt" : 10,
        "appid": ow_key,
        "units": "metric" if metric else "imperial"
    }
    r = req.get(base_url + path, params=params)
    data = r.json()
    weather_list = []
    for i in data["list"]:
        meta_data ={
            "datetime" : i["dt"],
            "day" : i["temp"]["day"],
            "night" : i["temp"]["night"],
            "max" : i["temp"]["max"],
            "min" : i["temp"]["min"],
            "wind_speed": i["speed"],
            "humidity": i["humidity"],
            "description": i["weather"][0]["main"],
            "icon" : i["weather"][0]["icon"]
        }
        weather_list.append(meta_data)
    weather = {
        "country" : data["city"]["country"],
        "city": data["city"]["name"],
        "list" : weather_list
    }
    return weather