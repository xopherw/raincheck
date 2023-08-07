import requests as req, os
from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.openrouteservice.org"
os_key = os.getenv("OS_KEY")

def getLocationAutoComplete(location):
    path = "/geocode/autocomplete"
    params = {
        "api_key": os_key,
        "text" : location,
        "sources" : "gn"

    }
    r = req.get(base_url + path, params=params)
    data = r.json()
    lst = []
    for i in data["features"]:
        # Reduce replicate results
        # if("county" in i["properties"]):
        meta_data = {
            "name" : i["properties"]["name"],
            "country" : i["properties"]["country"],
            "label" : i["properties"]["label"],
            "lon" : i["geometry"]["coordinates"][0],
            "lat" : i["geometry"]["coordinates"][1],
        }
        lst.append(meta_data)
    
    return lst