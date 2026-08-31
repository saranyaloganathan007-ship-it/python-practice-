name = input("Enter student name: ")
mark = int(input("Enter mark: "))

if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"

print("Student:", name)
print("Grade:", grade)