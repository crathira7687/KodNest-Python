class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        return (
            f"STUDENT PROFILE\n"
            f"Student ID:{self.student_id}\n"
            f"Name:{self.name}\n"
            f"Course:{self.course}\n"
            f"Experience:{self.experience}\n"
            f"Skills:{','.join(self.skills)}"
        )

student_id = int(input("enter the id:"))
name = input("enter the name: ").strip()
course = input("enter the course: ").strip()
experience = input("enter the experience: ")
skills = input("enter the skills: ").split()

student = StudentProfile(student_id, name, course, experience, skills)

print(student)