import random as rand
import datetime as dt
import smtplib as smtp_library

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()


def send_email():
    my_email = "xyz@gmail.com"
    my_password = "a strong password!"
    random_quote = rand.choice(quotes)
    with smtp_library.SMTP(host="smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs="abc@gmail.com",
            msg=f"Subject:Monday Morning Quote\n\n{random_quote}")


now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    send_email()
