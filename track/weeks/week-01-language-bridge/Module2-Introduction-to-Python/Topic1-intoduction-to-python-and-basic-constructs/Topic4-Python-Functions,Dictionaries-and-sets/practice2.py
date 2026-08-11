def check_sign(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"
    else:
        return "zero"
    
number=int(input("enter a number:"))
result=check_sign(number)
print("result:",result)