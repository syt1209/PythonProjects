import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OMW_API_KEY")
my_lat = 45.5088
my_lon = -73.5878

account_sid = os.environ.get("ACCOUNT_ID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    'lat': my_lat,
    'lon': my_lon,
    'exclude': "current,minutely,daily",
    'appid': API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()

twelve_hour_weather = weather_data["hourly"][:12]

for hour_weather in twelve_hour_weather:
    weather_id = hour_weather["weather"][0]["id"]
    if int(weather_id) > 700:
        client = Client(account_sid, auth_token)
        print(weather_id)
        message = client.messages.create(body="Snow", from_="phone", to="phone")
        break
    else:
        continue
