from fastapi import FastAPI
import open_weather as ow, openroute_service as ors

app = FastAPI()

@app.get("/")
def root():
    return {"message": "root of raincheck"}

@app.get("/location")
def getCity(city : str):
    return ors.getLocationAutoComplete(city)

@app.get("/weather")
async def getWeather(lat : float = 12, lon : float = 10):
    weather = ow.getWeatherNow(lon, lat)
    return weather

@app.get("/weather/hourly")
async def getWeatherHourly(lat : float = 12, lon : float = 10):
    weather = ow.getWeatherHourly(lon, lat)
    return weather

@app.get("/weather/daily")
async def getWeatherDaily(lat : float = 12, lon : float = 10):
    weather = ow.getWeatherDaily(lon, lat)
    return weather

