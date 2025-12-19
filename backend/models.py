from pydantic import BaseModel, Field

class JobDetails(BaseModel):
    role_title: str = Field(description="The exact job title as listed in the job posting.")
    company: str = Field(description="The name of the company offering the job.")
    role_type: str = Field(description="intern, new_grad, junior, etc.")

    technical_skills: list[str] = Field(
        description="all technologies mentioned - exact names"
    )

    responsibilities: list[str] = Field(
        description="Key job functions, priority order"
    )

    company_keywords: list[str] = Field(
        description="Values, culture words: innovation, teamwork, impact, etc."
    )

    ideal_candidate: str = Field(
        description="One Sentence: what kind of person they want"
    )


# Models for cv material extraction
class BaseInfo():
    name: str = "Dakota Roth"
    location: str = "Corvallis, OR"
    email: str = "dakota@codaea.com"
    phone: str = "+1-541-206-9437"
    linkedin: str = "codaea"
    github: str = "codaea"
    website: str = "https://codaea.com"


class WorkExperience(BaseModel):
    company: str
    position: str
    location: str
    start_date: str = Field(description="YYYY-MM")
    end_date: str = Field(description="YYYY-MM or empty if present")
    highlights: list[str] = Field(description="List of bullet points describing key achievements and responsibilities.")

class Education(BaseModel):
    institution: str = Field(description="Name of the educational institution.")
    area: str = Field(description="Field of study or major.")
    degree: str = Field(description="Degree obtained. (BS, MS, PhD, etc.)")
    location: str = Field(description="Location of the institution.")
    start_date: str = Field(description="Start date of the educational program. Represented as YYYY-MM.")
    end_date: str = Field(description="End date of the educational program.")

class Skills(BaseModel):
    label: str = Field(description="Category or type of skills.")
    details: str = Field(description="Description of skills, technologies, or proficiencies.")

class Projects(BaseModel):
    name: str = Field(description="Name of the project.")
    description: str = Field(description="Brief description of the project.")
    highlights: list[str] = Field(description="Key highlights or features of the project.")

class RelevantMaterial(BaseModel):
    WorkExperience: list[WorkExperience] 
    Education: list[Education] 
    Skills: list[Skills] 
    Projects: list[Projects]
