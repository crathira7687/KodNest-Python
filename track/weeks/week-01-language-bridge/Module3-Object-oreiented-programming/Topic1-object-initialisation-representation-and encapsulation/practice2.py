class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id=student_id
        self.name=name
        self.course=course

first_id=int(input("enter the id:"))
first_name=input("enter the name:").strip()
first_course=input("enter the course:").strip()

second_id=int(input("enter the id:"))
second_name=input("enter the name:").strip()
second_course=input("enter the course:").strip()

first_student=StudentProfile(first_id,first_name,first_course)
second_student=StudentProfile(second_id,second_name,second_course)
print("Student 1")
print("Student ID:",first_student.student_id)
print("Name:",first_student.name)
print("Course:",first_student.course)
print("Student 2")
print("Student ID:",second_student.student_id)
print("Name:",second_student.name)
print("Course:",second_student.course)