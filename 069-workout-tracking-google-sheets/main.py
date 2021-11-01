import requests
import datetime

NUTRITIONIX_APP_ID = "<hidden>"
NUTRITIONIX_API_KEY = "<hidden>"
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "<hidden>"

exercise = input("what exercise you did today?\n")

params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 61,
    "height_cm": 169,
    "age": 36
}

nutrionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

response = requests.post(url=END_POINT, json=params, headers=nutrionix_headers)
# print(response.text)
exercises = response.json()["exercises"]
for exercise in exercises:
    activity_date = datetime.date.today().strftime("%d-%b-%Y")
    activity_time = datetime.datetime.now().strftime("%I:%M %p")
    activity_name = exercise["name"]
    activity_duration = float(exercise["duration_min"])
    activity_calories = float(exercise["nf_calories"])
    activity_json = {
        "workout": {
            "date": activity_date,
            "time": activity_time,
            "exercise": activity_name,
            "duration": activity_duration,
            "calories": activity_calories,
        }
    }
    # print(activity_json)
    update_sheet = requests.post(SHEETY_ENDPOINT, json=activity_json)
    # print(update_sheet.text)
