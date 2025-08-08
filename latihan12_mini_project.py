student_scores = input("Enter student scores separated by commas: ")
scores = [int(score) for score in student_scores.split(",")]

grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "E"
    for score in scores
]

passing_studentss = [score for score in scores if score >= 60]
falling_students = [score for score in scores if score < 60]

print("Student Scores", scores)
print("Student Grade", grades)

for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i} Score: {score}, Grade: {grade}")

print("Passing Students:", passing_studentss)
print("Failing Students:", falling_students)