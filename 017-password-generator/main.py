#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

num_letters = len(letters)
num_numbers = len(numbers)
num_symbols = len(symbols)
# print(f"count of letters: {num_letters} | count of numbers: {num_numbers} | count of symbols: {num_symbols}")

pwd = []

for letter in range(0, nr_letters):
    pwd.append(letters[random.randint(0, num_letters-1)]) # we can either use list.append or += to append the list

for symbol in range(0, nr_symbols):
    pwd += random.choice(symbols) #we can use randint or coice to get the random data from a list.

for number in range(0, nr_numbers):
    pwd += numbers[random.randint(0, num_numbers-1)]

# password = ""
# for i in pwd:
#     password += i
# print(f"Your random password is: {password}")

random.shuffle(pwd)
password = ""
for i in pwd:
    password += i
print(f"Your random strong password is: {password}")
