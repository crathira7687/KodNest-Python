class StudentProfile:
    def __init__(self,student_id,student_name,course,current_score=0.0,skills=None,is_placed=False):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.current_score = current_score
        self.skills = [] if skills is None else list(skills)
        self.is_placed = is_placed
    def __str__(self):
            skills_join = ", ".join(self.skills) if self.skills else "Not Added"
            placement_status =  ("Placed" if self.is_placed else "Not Placed")
            return (
               f"Student ID:{self.student_id}\n"
               f"Name:{self.student_name}\n"
               f"Course:{self.course}\n"
               f"Current Score:{self.current_score:.1f}\n"
               f"Skills:{self.skills}\n"
               f"Placement Status:{self.is_placed}")
profile_one = StudentProfile(101,"Athira","Python",90,["java","python","sql"],True)

print(profile_one)