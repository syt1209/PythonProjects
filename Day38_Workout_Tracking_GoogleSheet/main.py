import requests
from datetime import datetime

NUTRI_ID = "1f73ae6c"
NUTRI_KEY = "4e5f895efde26e4e4f900aef13d616fb"

nutri_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1caf8ddc25f72670941e95ff5a659102/workoutTracking/sheet1"

headers = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
}

query = input("What exercise do you want to add?")

parameters = {
    "query": query,
    "gender": "female",
    "weight_kg": 57,
    "height_cm": 167,
    "age": 34
}

nutri_response = requests.post(url=nutri_exercise_endpoint, json=parameters, headers=headers)
results = nutri_response.json()["exercises"][0]
print(results)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": results["name"].title(),
        "duration": results["duration_min"],
        "calories": results["nf_calories"]
    }
}

sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)

print(sheet_response.text)

