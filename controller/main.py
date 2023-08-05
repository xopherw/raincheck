from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "root of Open Weather!"}

@app.get("/?city={city}")
def getCity(city : str):
    return {"city": city}

@app.get("/weather/")
def getWeather(lon : float = 12, lat : float = 10):
    return {"lon": lon, "lat": lat}