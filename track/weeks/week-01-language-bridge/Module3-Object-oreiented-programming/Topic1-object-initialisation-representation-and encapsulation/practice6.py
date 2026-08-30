class CandidateProfile:
    def __init__(self,name,email,score):
        self.name=name
        self._email=email
        self.__score=score

    def get_email(self):
        return self._email

    def get_score(self):
        return self.__score

name=input("enter the name:").strip()
email=input("enter the email:").strip()
score=int(input("enter the score:"))

candidate=CandidateProfile(name,email,score)

print("Name:",candidate.name)
print("Email:",candidate.get_email())
print("Score:",candidate.get_score())
