# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# should not use len or sum function with lists

student_count = 0
sum_heights = 0

# print(student_heights)
for student in student_heights:
    student_count += 1
    sum_heights += student

# print(student_count)
# print(sum_heights)

average_height = round(sum_heights / student_count)
print(average_height)