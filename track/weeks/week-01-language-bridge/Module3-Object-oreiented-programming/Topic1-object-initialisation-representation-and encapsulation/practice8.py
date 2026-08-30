class StudentProfile:
    def __init__(self,student_id,name,score,skills):
        self.__student_id=student_id
        self.__name=name
        self.__score=score
        self.__skills=skills

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,new_score):
        if 0<=new_score<=100:
            self.__score=new_score

    @property
    def skills(self):
        return tuple(self.__skills)
    
    def add_skill(self,new_skill):
        new_skill=new_skill.strip()
        if new_skill and new_skill not in self.skills:
            self.__skills.append(new_skill)


    def __str__(self):
        return f"""STUDENT PROFILE
Student ID:{self.student_id}
Name:{self.name}
Score:{self.score}
Skills:{', '.join(self.skills)}"""
        
student_id=int(input("enter the student id:"))
name=input("enter the name:").strip()
initial_score=int(input("enter the score:"))
skills_input=input("enter the skills:").strip()
new_score=int(input("enter the new score:"))
new_skill=input("enter the new skill:").strip()

initial_skills=[
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()    
]

student=StudentProfile(student_id=student_id,name=name,score=initial_score,skills=initial_skills)
student.add_skill(new_skill)
print(student)