# Read and convert the student details
student_name =str(input("Enter the name:"))
student_age=input("Enter the age:")
student_age = int(student_age)
course_rating = float(input("enter the rating:"))

# Display the values
print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Rating: {course_rating}")

print(type(student_name))
print(type(student_age))
print(type(course_rating))
