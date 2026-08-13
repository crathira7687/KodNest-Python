def check_eligibility(marks,attendance,project_completed):
    if marks>=60 and attendance>=75 and project_completed=="yes":
        return "Eligible"
    else:
        return "Not Eligible"

marks=int(input("enter the marks:"))
attendance=int(input("enter the attendance:"))
project_completed=input("enter the project status:")
result=check_eligibility(marks,attendance,project_completed)
print(result)