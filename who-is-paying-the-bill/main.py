import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
no_of_people = len(names)
# print(no_of_people)
random_number = random.randint(0, no_of_people - 1)
# print(random_number)
random_name = names[random_number]
print(random_name + " is going to buy the meal today!")