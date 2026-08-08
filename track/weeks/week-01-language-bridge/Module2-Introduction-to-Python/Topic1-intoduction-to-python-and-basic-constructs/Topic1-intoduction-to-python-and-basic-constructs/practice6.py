# Read and convert the student details
student_name=input("enter the name:")
student_age=input("enter the age:")
student_age=int(student_age)
course_rating=input("enter the rating:")
course_rating=float(course_rating)

# Display the values
print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Rating: {course_rating}")

print(type(student_name))
print(type(student_age))
print(type(course_rating))
