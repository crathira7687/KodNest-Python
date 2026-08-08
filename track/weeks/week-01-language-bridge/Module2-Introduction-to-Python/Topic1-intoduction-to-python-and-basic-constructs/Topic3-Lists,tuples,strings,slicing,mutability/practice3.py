name=input("enter the name:")
course=input("enter the course name:")
score=int(input("enter the score:"))

#store them in tuples
student_details=(name,course,score)
student_name,student_course,student_score=student_details


#display the details
print("Student Name:",student_name)
print("Student Course:",student_course)
print("Student Score:",student_score)