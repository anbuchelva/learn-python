#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to tip calculator!")
bill_amout = input("What was the total bill? $")
tip_amount = input(
    "What percentage of tip you would like to give? 10, 12 or 15 ")
people_count = input("How many people to split the bill? ")
total_amount = float(bill_amout) * (1 + int(tip_amount) / 100)
share_per_person = round(total_amount / int(people_count), 2)
print(f"Each person should pay: ${share_per_person}")
