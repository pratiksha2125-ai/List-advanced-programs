

li1=[1,2,3,4,5,6]
li2=[4,5,6,7,8]

common=[]
for i in li1:
    if i in li2:
        common.append(i)
print("Common elements are:",common)