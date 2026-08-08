limit=int(input("enter the limit:"))
target=int(input("enter the target:"))
#initialisation of count,total,found
count=0
total=0
found="No"

#use for loop
for i in range(1,limit+1):
    if i%3==0:
        total+=i
        count+=1
        if i==target:
            found="Yes"
            
#display count,total,found
print("Count:",count)
print("Total:",total)
print("Found:",found)