# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
months_left = (90 - age) * 12
days_left = int((90 - age) * 365.25)
weeks_left = (90 - age) * 52

print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
