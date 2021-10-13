import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "<hidden>"

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

will_rain_today = False

# take first 12 entries from the api output
for hour in weather_data[:12]:
    # hour is dictionary, weather is list, first item of weather is again list
    weather_code = hour["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain_today = True

if will_rain_today:
    token = "<hidden>"
    parameters = {
        "chat_id": "@Chennai_Alerts",
        "text": f"It is going to rain 🌧 today, Remember to bring an umbrella ☔",
        "parse_mode": "Markdown"
    }
    response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()
