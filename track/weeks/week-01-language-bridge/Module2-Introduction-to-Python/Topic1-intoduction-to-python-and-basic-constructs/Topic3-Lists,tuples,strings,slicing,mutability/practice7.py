skills=[]
for i in range(5):
    skill=input("enter the skill:")
    skills.append(skill)

skill_record=tuple(skills)

print("Skill record:",skill_record[:])
print("First Three:",skill_record[:3])
print("Last Two:",skill_record[-2:])
print("Alternate Skills:",skill_record[::2])
print("Reversed Skills:",skill_record[::-1])