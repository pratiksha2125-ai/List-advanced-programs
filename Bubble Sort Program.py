

number=[50,20,10,40,30]
for i in range(len(number)):
    for j in range(0,len(number)-i-1):
        if number[j]>number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]

print("Sorted list:",number)