with open("file1.txt") as file1_data:
    file1_list = file1_data.readlines()

with open("file2.txt") as file2_data:
    file2_list = file2_data.readlines()

file1_list_stripped = [int(number.strip()) for number in file1_list]
file2_list_stripped = [int(number.strip()) for number in file2_list]

result = [number for number in file1_list_stripped if number in file2_list_stripped]

# Write your code above 👆
print(result)
