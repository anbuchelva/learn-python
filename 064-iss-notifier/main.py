#! /usr/bin/python3
import requests
from datetime import datetime

MY_LAT = 12.938790
MY_LNG = 80.173500


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    # print(data)
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5 :
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # split the output into date / time then hour / min and seconds
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)
    time_now = datetime.now().hour
    # print(time_now.hour)
    if time_now >= sunset or time_now <= sunrise:
        return True

# send a message to telegram channgel or group.
# create a bot using @botfather
# add the bot to a channel or group as admin give writes to post messages
# setup a crontab job based on the interval that you want to run

if is_iss_overhead() and is_night():
    token = "create a bot using @botfather and get a token"
    place = "Mention your city name, this will be included in the alert msg"
    parameters = {
            "chat_id": "chat group or channel like: @channel_name",
            "text": f"The *International Space Station* is above {place}; go to your roof top and look up!",
            "parse_mode": "Markdown"
        }

    response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()
