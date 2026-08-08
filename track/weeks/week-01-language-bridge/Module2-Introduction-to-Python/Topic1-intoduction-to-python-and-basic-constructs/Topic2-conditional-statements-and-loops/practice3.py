student_marks=int(input("enter the student marks:"))
attendance=int(input("enter the attendance percentage:"))
project_completion=True
#use conditions
if student_marks>=60 and attendance>=75:
    if project_completion==True:
       print("Eligible")
    else:
       print("Not Eligible")
else:
    print("Not Eligible")

