class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.job_id} | {self.company} | {self.role} | {self.location} | {status}"

job_one = JobDescription(
    job_id="501",
    company="TechNova",
    role="Software Engineer",
    location="Bangalore",
    is_active=True
)
job_two = JobDescription(
    job_id="502",
    company="SoftLogic",
    role="Data Analyst",
    is_active=False
)
job_three = JobDescription(
    job_id="503",
    company="DigitalCore",
    role="Project Manager",
    location="Remote",
    is_active=True
)

job_description = [job_one, job_two, job_three]
for job in job_description:
    print(job)

