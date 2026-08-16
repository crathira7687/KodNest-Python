class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        is_placed
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed
    def __str__(self):
        return (
            f"STUDENT PROFILE\n"
            f"Student ID:{self.student_id}\n"
            f"Name:{self.name}\n"
            f"Course:{self.course}\n"
            f"Score:{self.score}\n"
            f"is_placed:{'placed' if self.is_placed else 'Not Placed'}"
            )
student_id=int(input("enter the student id:"))
name=input("enter the name:")
course=input("enter the course:")
score=float(input("enter the score:"))
placement_input=input("enter the placement status:")

is_placed = False
if placement_input.lower() == "yes":
    is_placed=True
else:
    is_placed=False
    
student=StudentProfile(student_id=student_id,name=name,course=course,score=score,is_placed=is_placed)
print(student)
    
            
    