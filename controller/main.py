from fastapi import FastAPI
import open_weather as ow

app = FastAPI()

@app.get("/")
def root():
    return {"message": "root of raincheck"}

@app.get("/?city={city}")
def getCity(city : str):
    return {"city": city}

@app.get("/weather")
async def getWeather(lat : float = 12, lon : float = 10):
    weather = ow.getWeatherNow(lon, lat)
    return weather

@app.get("/weather/hourly")
async def getWeatherHourly(lat : float = 12, lon : float = 10):
    weather = ow.getWeatherHourly(lon, lat)
    return weather

