name = input("Enter student name: ")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Student:", name)
print("Total:", total)
print("Average:", average)

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")