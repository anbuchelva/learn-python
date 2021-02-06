# File Not Found Error
# with open("a_file.txt") as file:
#     file.read()

# Fix
try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

# Key Error
try:
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except KeyError as error_message:
    print(f"The key {error_message} is not found in the dictionary!")

# List Error
#a_list = [1, 2, 3]
#print(a_list[3])

# Type Error
# text = "sample text"
# print(text + 5)

# else portion to be executed if there are no exceptions / no error messages
else:
    content = file.read()
    print(content)

# finally portion  always run
finally:
    file.close()
    print("file was closed!")
