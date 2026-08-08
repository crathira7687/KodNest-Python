#Read the value of n
n=int(input("enter a number:"))

#initialising variables
counter=1
total=0

#calculate total
while counter<n:
    total+=counter
    counter+=1

#display total
print(f"Total: {total}")