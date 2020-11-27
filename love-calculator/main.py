# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
# print(name)

true = 0
true += name.count("t")
true += name.count("r")
true += name.count("u")
true += name.count("e")

love = 0
love += name.count("l")
love += name.count("o")
love += name.count("v")
love += name.count("e")

true_love = str(true) + str(love)
true_love_as_int = int(true_love)
# print(true_love_as_int)

if true_love_as_int > 90 or true_love_as_int < 10:
  print(f"Your score is {true_love_as_int}, you go together like coke and mentos.")
elif true_love_as_int > 40 and true_love_as_int < 50:
  print(f"Your score is {true_love_as_int}, you are alright together.")
else:
  print(f"Your score is {true_love_as_int}.")
