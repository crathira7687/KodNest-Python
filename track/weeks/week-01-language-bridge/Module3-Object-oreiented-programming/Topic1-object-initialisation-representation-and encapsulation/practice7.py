class StudentProfile:
    def __init__(self,name,score):
        self.name=name
        self.__score=score

    def get_score(self):
        return self.__score
    
    def set_score(self,new_score):
        if 0<=new_score<=100:
            self.__score=new_score
            return True
        else:
            return False

name=input("enter the name:").strip()
initial_score=int(input("enter the initial score:"))
new_score=int(input("enter the new score:"))

student=StudentProfile(name,initial_score)

result=student.set_score(new_score)
if result:
    print("score updated")
else:
    print("invalid score")

print("Name:",name)
print("Final score:",student.get_score())