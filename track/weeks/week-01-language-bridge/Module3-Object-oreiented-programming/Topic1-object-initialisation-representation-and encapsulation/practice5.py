class JobDescription:
    def __init__(self, job_id, company, role, location, required_skills, is_active):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.required_skills = required_skills
        self.is_active = is_active

    def __str__(self):
        return (
            f"JOB DESCRIPTION\n"
            f"Job ID:{self.job_id}\n"
            f"Company:{self.company}\n"
            f"Role:{self.role}\n"
            f"Location:{self.location}\n"
            f"Required Skills:{','.join(self.required_skills)}\n"
            f"Status:{'Active' if self.is_active else 'Closed'}"
        )

job_id = int(input("enter the job id:"))
company = input("enter the company name:").strip()
role = input("enter the role:").strip()
location = input("enter the location:").strip()
skills_input = input("enter the required skills:")
status_input = input("enter the status:")

required_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_active = status_input.lower() == "yes"

job = JobDescription(job_id, company, role, location, required_skills, is_active)

print(job)
