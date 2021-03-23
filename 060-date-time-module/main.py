import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Weekday: {weekday}")

if year == 2020 or year == 2021:
    print("wear a mask and follow social distancing!")

date_of_birth = dt.datetime(year=2000, month=1, day=1, hour=1)
print(date_of_birth)
