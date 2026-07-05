numbers = []

while True:

    print("\n1. Add Element")
    print("2. Remove Element")
    print("3. Display List")
    print("4. Search Element")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number: "))
        numbers.append(n)

    elif choice == 2:
        n = int(input("Enter number to remove: "))

        if n in numbers:
            numbers.remove(n)
        else:
            print("Element not found")

    elif choice == 3:
        print("List:", numbers)

    elif choice == 4:
        n = int(input("Enter element to search: "))

        if n in numbers:
            print("Element found")
        else:
            print("Element not found")

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")