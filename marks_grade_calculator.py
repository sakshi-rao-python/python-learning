name = input("Enter your name: ")

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)