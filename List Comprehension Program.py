
# square of number
number = [1, 2, 3, 4, 5, 6, 7, 8]
sqr=[x*x for x in number]
print(sqr)
# even numbers
even=[x for x in number if x%2==0]
print(even)

# with string
words=["apple","banana","mango"]
uppercase=[word.upper() for word in words]
print(uppercase)