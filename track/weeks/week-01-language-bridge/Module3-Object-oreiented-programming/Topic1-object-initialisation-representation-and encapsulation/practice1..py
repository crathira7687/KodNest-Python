class StudentProfile:
    def __init__(self,student_id,name,course,experience,skills):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills
        

student_id=int(input("enter the student id:"))
name=input("enter the name:").strip()
course=input("enter the course:").strip()
experience=input("enter the experience:").strip()
skills=input("enter the skills:").split()

student=StudentProfile(student_id,name,course,experience,skills)

print("Student ID:",student.student_id)
print("Name:",student.name)
print("Course:",student.course)
print("Experience:",student.experience)
print("Skills:",",".join(skills))