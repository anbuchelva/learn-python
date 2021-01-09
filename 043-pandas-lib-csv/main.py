# ==============================================================================
#  import csv
#
#  with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#  print(temperature)
# ==============================================================================

import pandas

# import csv file to pandas framework
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# convert csv file to dictionary
data_dict = data.to_dict()
# print(data_dict)

# find average temperature
# method 1
# temp_list = data["temp"].to_list()
# average_temp = round(sum(temp_list) / len(temp_list),2)
# print(f"Average Temperature: {average_temp}")

# method 2
print(f"Average Temperature: {data['temp'].mean()}")

# find max temp
print(f"Maximum Temperature: {data['temp'].max()}")

# Get data in columns
# option 1:
print(data["condition"])

# option 2:
print(data.condition)

# Get data on rows
print(data[data.day == "Monday"])

## Get day value from the day which had max temp 
print(data[data.temp == data.temp.max()])

## Get Monday's temperature in 'F
monday_temp = data[data.day == "Monday"]
monday_temp_celcius = int(monday_temp.temp)
monday_temp_farenheit = (monday_temp_celcius * 9 / 5) + 32
print(monday_temp_farenheit)

## Dictionary to CSV
marks = {
    "students": ["Amy", "Bob", "Cathy"],
    "score": [45, 65, 76]
}

students_score = pandas.DataFrame(marks)
print(students_score)
students_score.to_csv("student_score.csv")
