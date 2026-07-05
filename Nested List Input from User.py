students=[]
n=int(input("Enter number of students:"))

for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter marks:"))
    students.append([name,marks])
print("\n Student Record:")
for student in students:
        print(student)