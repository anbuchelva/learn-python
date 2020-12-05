student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

def grade(score):
  if score >= 91 and score <= 100:
      result = "Outstanding"
  elif score >= 81:
      result = "Exceeds Expectations"
  elif score >= 71:
      result = "Acceptable"
  else:
      result = "Fail"
  return result

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]    
    student_grades[student] = grade(score)

# 🚨 Don't change the code below 👇
print(student_grades)