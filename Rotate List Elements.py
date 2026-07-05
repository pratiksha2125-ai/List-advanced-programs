

numbers=[1,2,3,4,5]

n=int(input("Enter rotation position:"))

rotated=numbers[n:]+numbers[:n]
print("Rotated list:",rotated)