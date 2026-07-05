
students=[]

while True:
      print("\n ---------------MENU------------------")
      print("\n 1.Add Students")
      print("\n 2.Display Students")
      print("\n  3.Search Students")
      print("\n 4.Delete Students")
      print("\n 5.Exit")


      choice =int(input("Enter choice:"))
      if choice == 1:
            name=input("Enter a syudents name:")
            marks=int(input("Enter marks:"))
            students.append([name,marks])
      elif choice == 2:
            print("\n Student Record")

            for student in students:
                  print("Name:",student[0],"Marks",student[1])

      elif choice == 3:
            name=input("Enter student name to search:")
            found=False
            for student in students:
                  if student[0] == name:
                        print(" Record Found:",student)
                        found=True
                        break
            if not found:
                  print("Student not found")

      elif choice == 4:
             name=input("Enter student name to delete :")
             found = False
             for student in students:
                  if student[0] == name:
                        students.remove(student)
                        print("Record delete")
                        found = True
                        break
                  if not found :
                     print("Student not found")

      elif choice == 5:
            print("Program ended ")
            break
      else:
            print("Invalid choice")
