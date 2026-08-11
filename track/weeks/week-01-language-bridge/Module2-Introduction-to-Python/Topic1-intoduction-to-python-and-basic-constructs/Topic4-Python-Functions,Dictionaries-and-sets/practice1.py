def calculate(first_number,second_number,operator):
    if operator=='+':
        return first_number+second_number
    elif operator=='-':
        return first_number-second_number
    elif operator=='*':
        return first_number*second_number
    elif operator=='/':
        return first_number/second_number
    
first_number=int(input("enter the first number:"))
second_number=int(input("enter the second number:"))
operator=input("enter the operator:")

result=calculate(first_number,second_number,operator)
print("Result:",result)