import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.501690
MY_LNG = -73.567253
MARGIN = 5
TIMEZONE_DIFFERENCE = 5
MY_EMAIL = "ys.developer2020@gmail.com"
PASSWORD = "0202repoleved.sy"


def in_range(pos):
    upper_lat = MY_LAT + MARGIN
    lower_lat = MY_LAT - MARGIN
    upper_lng = MY_LNG + MARGIN
    lower_lng = MY_LNG - MARGIN
    if lower_lat < pos[0] < upper_lat and lower_lng < pos[1] < upper_lng:
        return True


def is_dark(hour, sunrise_hour, sunset_hour):
    if hour > sunset_hour or hour < sunrise_hour:
        return True


# Sunset and Sunrise API
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
_response.raise_for_status()
data = _response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

now = datetime.now()
current_hour = (now.hour + TIMEZONE_DIFFERENCE) % 24

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])

iss_position = (latitude, longitude)

while True:
    time.sleep(60)
    if in_range(iss_position) and is_dark(current_hour, sunrise, sunset):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject: Look Up\n\nISS is above you in the sky.")
