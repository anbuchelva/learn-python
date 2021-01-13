with open("file1.txt") as file1_data:
    file1_list = file1_data.readlines()

with open("file2.txt") as file2_data:
    file2_list = file2_data.readlines()

result = [int(number) for number in file1_list if number in file2_list]

# Write your code above 👆
print(result)
