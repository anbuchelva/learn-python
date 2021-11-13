#! /usr/bin/python3
import requests
import json
from datetime import datetime, timedelta, time

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "<hidden>"
TELEGRAM_TOKEN = "<hidden>"

api_params = {
    "appid": API_KEY,
    "lat": 12.938790,
    "lon": 80.173500,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=api_params)
response.raise_for_status()
weather_data = response.json()["hourly"]  # get hourly data
# print(weather_data)

# icons_file = "/home/ubuntu/alerts/icons.json"
icons_file = "icons.json"

telegram_message = "☀ Weather Forecast ⛈\n\n"
with open(icons_file, 'r') as f:
    icons = json.load(f)
    i = 0
    for hour in weather_data[:12]:
        # print(hour)
        weather_code = hour["weather"][0]["id"]
        weather_temp = round(float(hour["temp"]) - 273.15, 1)
        weather_icon = hour["weather"][0]["icon"]
        weather_main = hour["weather"][0]["main"]
        weather_desc = hour["weather"][0]["description"].title()
        emoji_icon = icons[weather_icon]
        time_value = datetime.now() + timedelta(hours=i)
        formated_time = time_value.strftime("%H:%M")
        # print(f"{formated_time} {emoji_icon} {weather_main} - {weather_desc}")
        weather_text = f"`{formated_time} {emoji_icon} {weather_temp}'C` {weather_desc}\n"
        telegram_message = f"{telegram_message}{weather_text}"
        i += 1

if datetime.now().hour > 21:
    telegram_message = f"{telegram_message} \n\nThis is the last weather forecast of this day. " \
                       f"The next forecast will be sent by 6.00 AM tomorrow. Have a good night! 😴"
# will_rain_today = False
#
# # take first 12 entries from the api output
# for hour in weather_data[:12]:
#     # hour is dictionary, weather is list, first item of weather is again list
#     weather_code = hour["weather"][0]["id"]
#     if int(weather_code) < 700:
#         will_rain_today = True

# if will_rain_today:
# print(telegram_message)
if 22 > datetime.now().hour > 5:
    token = TELEGRAM_TOKEN
    parameters = {
        "chat_id": "@Chennai_Alerts",
        "text": telegram_message,
        "parse_mode": "Markdown"
    }
    response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()
