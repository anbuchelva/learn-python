import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []

    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))

print(temperature)
