height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

if int(height) > 3:
    raise ValueError("Humans height shouldn't be more than 3 metres")

if int(weight) < 15:
    raise ValueError("BMI calculation is not for kids")

# Write your code below this line 👇
bmi = float(weight) / float(height) ** 2
bmi = int(bmi)
print(bmi)
