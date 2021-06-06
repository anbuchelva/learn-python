import datetime as dt
import pandas as pd
import random
import smtplib

FROM_EMAIL = "xyz@gmail.com"
PASSWORD = "1234567890"

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient='records')

for birthday_dict in birthday_list:
    birthday_person = birthday_dict["name"]
    birthday = (birthday_dict["month"], birthday_dict["day"])
    to_email = birthday_dict["email"]
    if today == birthday:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter:
            letter_content = letter.read()
            letter_content = letter_content.replace("[NAME]", birthday_person)
            # print(letter_content)
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=FROM_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=FROM_EMAIL,
                    to_addrs=to_email,
                    msg=f"Subject:Happy Birthday!\n\n{letter_content}"
                )
