import requests as req

base_url = "https://api.openweathermap.org/data/2.5"

class OpenWeather():
    def __init__(self, city):
        self.city = city