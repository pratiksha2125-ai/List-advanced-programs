

numbers=[10,20,30,40,50]

key=int(input("Enter number to search:"))
found=False

for i in numbers:
    if i==key:
        found=True
        break

if found:
    print("Element found")
else:
    print("Element is not found")