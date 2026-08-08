number_count=int(input("enter a number count:"))
#initialisation
positive_count=0
negative_count=0
zero_count=0
total=0
#loop
for i in range(number_count):
    number=int(input("enter a number:"))
    total+=number
    if number>0:
        positive_count+=1
    elif number<0:
        negative_count+=1
    else:
        zero_count+=1
#display result
print("Positive Count:",positive_count)
print("Negative Count:",negative_count)
print("Zero Count:",zero_count)
print("Total:",total)
