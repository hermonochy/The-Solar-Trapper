# import json
# import matplotlib.pyplot as plt 
# import numpy as np

# DOCUMANTAION
# https://open-meteo.com/en/docs#latitude=51.7&longitude=-1.25&current=&minutely_15=&hourly=temperature_2m,cloud_cover&daily=&timezone=Europe%2FLondon&models=

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 51.7,
	"longitude": -1.25,
	"hourly": ["temperature_2m", "cloud_cover"],
	"timezone": "Europe/London"
}
responses = openmeteo.weather_api(url, params=params)

print(responses.Hourly())

# data = json.loads(open("data.json", "r").read())["hourly"]
#     
# xpoints = np.array(range(len(data["time"])))
# 
# ypoints1 = np.array(data["cloud_cover"])
# ypoints2 = np.array(data["temperature_2m"])
# 
# plt.plot(xpoints, ypoints1)
# plt.show()
# 
# plt.plot(xpoints, ypoints2)
# plt.show()
