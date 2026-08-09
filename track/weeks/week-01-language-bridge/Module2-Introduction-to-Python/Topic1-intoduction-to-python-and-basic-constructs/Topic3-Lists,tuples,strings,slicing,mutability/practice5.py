word=input("enter a word:")
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))

numbers=[first,second,third]
record=(first,second,third)


print("Middle:",word[1:-1])
print("First Two:",numbers[:-1])
print("Reversed Tuple:",record[::-1])
