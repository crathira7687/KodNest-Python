def calculate_average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def find_missing_skills(student_skills, required_skills):
    missing_skills = []

    for r in required_skills:
        if r not in student_skills:
            missing_skills.append(r)
    
    return missing_skills


def build_summary(name, marks, student_skills, required_skills):
    
    avg = calculate_average(marks)

    missing_skills = find_missing_skills(student_skills, required_skills)

    if len(missing_skills) == 0 and avg >= 60:
        status = "Ready"
    else:
        status = "Needs Practice"

    return {
        "name" : name,
        "average" : avg,
        "status" : status,
        "missing_skills" : missing_skills
    }


# Read input and display the final summary

# name
name = input("enter the name:")

# marks
num_marks = int(input("enter the no of marks:"))

marks = input("enter the marks:").split()

marks_list = []

for m in marks:
    marks_list.append(int(m))


# skills
num_skills = int(input("enter no of skills:"))

skills_list = input("enter skills list:").split()

# required skills
num_of_r_skills = int(input("enter the no of required skills:"))

r_skills_list = input("enter the required skills:").split()

# --------------------------------------------------


summary = build_summary(name, marks_list, skills_list, r_skills_list)

print(summary)




