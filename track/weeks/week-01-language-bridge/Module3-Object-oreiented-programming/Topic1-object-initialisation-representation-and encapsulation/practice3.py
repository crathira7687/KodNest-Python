class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name=name
        self.experience=experience
        self.skills=skills

    def update_experience(self,new_experience):
        self.experience=new_experience
        
    def add_skill(self,new_skill):
        self.skills.append(new_skill)

name=input("enter the name:").strip()
experience=int(input("enter the experience:"))
skills=input("enter the skills:").split()

student=StudentProfile(name,experience,skills)
new_experience=int(input("enter the new experience:"))
student.update_experience(new_experience)

new_skill=input("enter the new skill: ").strip()
student.add_skill(new_skill)

print("Updated Profile:")
print("Name:",student.name)
print("Experience:",student.experience)
print("Skills:",",".join(student.skills))
