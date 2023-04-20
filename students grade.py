student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

students_grade = {}
for students in student_scores:
        score = student_scores[students]
        if score > 90:
          students_grade[students] ="outstanding"
        elif score > 80:
          students_grade[students] = "unexoected"
        elif score > 70:
          students_grade[students] = "good"
        else:
          students_grade[students] = "Your imp for our class so wait"


print(students_grade)