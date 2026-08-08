limit=int(input("enter the limit:"))
number=0
total=0
#use while loop
while number<=limit:
    if number%2==0:
        total+=number
    number+=1

print("Even Sum:",total)