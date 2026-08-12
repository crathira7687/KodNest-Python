def add_student(name,student=[]):
    student.append(name)
    return student

first_name=input("enter the first name:")
second_name=input("enter the second name:")
third_name=input("enter the third name:")

print(add_student(first_name))
print(add_student(second_name))
print(add_student(third_name))
