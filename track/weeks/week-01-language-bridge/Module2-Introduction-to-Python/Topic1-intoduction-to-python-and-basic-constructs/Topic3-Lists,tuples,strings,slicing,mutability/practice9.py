skills=[]
for i in range(5):
    skill=input("enter the skill:")
    skills.append(skill)

skill_record=tuple(skills)
print("skill record:",skill_record)

print("First Three:",skill_record[:3])
print("Last Two:",skill_record[-2:])

print("Alternate skills:",skill_record[::2])
print("Reversed skills:",skill_record[::-1])