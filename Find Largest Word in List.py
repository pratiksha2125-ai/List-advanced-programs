

word=["apple","banana","watermelon"]

largest=word[0]

for i in word:
    if len(i)>len(largest):
        largest=i
print("Largest word is :",largest)