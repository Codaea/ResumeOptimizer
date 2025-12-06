from openai import OpenAI
import rendercv
from pydantic import BaseModel, Field
from prompt import system_prompt, source_cv_data, job_description_data
from pathlib import Path
import traceback

class Response(BaseModel):
    type: str

class BaseInfo():
    name = "Dakota Roth"
    location = "Corvallis, OR"
    email = "dakota@codaea.com"
    phone = "+1-541-206-9437"
    linkedin = "codaea"
    github = "codaea"
    website = "https://codaea.com"

base_info = BaseInfo()

# 3 queries, one for each section of the resume
# optimize work experience, education, skills, projects for the job description
# write a summary based off material pulled 2-3 sentences from everything pulled

cv_data: dict = {
    "cv": {
        "name": base_info.name,
        "location": base_info.location,
        "email": base_info.email,
        "phone": base_info.phone,
        "website": base_info.website,
        "social_networks": [
            { "network": "LinkedIn", "username": base_info.linkedin },
            { "network": "GitHub", "username": base_info.github },
        ],
        "sections": {
            "summary": [
                    "Highly motivated software engineer with a passion for developing innovative solutions."
            ],
        }
    }
}

class WorkExperience(BaseModel):
    company: str
    position: str
    location: str
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

client = OpenAI()

print("Finding and extracting relevant material from CV...")
response = client.responses.parse(
    model='gpt-5-mini',
    input=[ 
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"Source Material: {source_cv_data}"
        },
        {
            "role": "user",
            "content": f"Source Job Description: {job_description_data}"
        }
    ],
    text_format=RelevantMaterial
)

if response.output_parsed is None:
    raise ValueError("Parsed output from response is None.")

ai_relevant_material: RelevantMaterial = response.output_parsed



cv_data['cv']['sections']['education'] = [entry.model_dump() for entry in ai_relevant_material.Education]
cv_data['cv']['sections']['work experience'] = [entry.model_dump() for entry in ai_relevant_material.WorkExperience]
cv_data['cv']['sections']['projects'] = [entry.model_dump() for entry in ai_relevant_material.Projects]
cv_data['cv']['sections']['skills'] = [entry.model_dump() for entry in ai_relevant_material.Skills]

print("Generating professional summary...")
response = client.chat.completions.create(
    model='gpt-5-mini',
    messages=[
        {
            "role": "system",
            "content": """
            You are a helpful assistant that summarizes resume content into a concise professional summary. \n Based on the following resume sections, write a concise 2-3 sentence professional summary suitable for a resume.
            
            Closely follow this writing style:

<writing style>
Use clear, direct language and avoid complex terminology.
Aim for a Flesch reading score of 80 or higher.
Use the active voice.
Avoid adverbs.
Avoid buzzwords and instead use plain English.
Use jargon where relevant.
Avoid being salesy or overly enthusiastic and instead express calm confidence.

Write 2-3 sentences (50-80 words). Focus on credentials, not achievements:
- Years of experience with specific technologies/languages
- Companies or types of companies worked at
- Educational background if relevant
- Core technical areas of expertise

Do NOT include specific projects, metrics, or achievements - those belong 
in the work experience section.
</writing style>
            """
        },
        {
            "role": "user",
            "content": f" resume: {ai_relevant_material.model_dump()}"
        }
    ]
)

summary = response.choices[0].message.content
cv_data['cv']['sections']['summary'] = [summary]

print("Creating PDF...")
try:
    rendercv.api.create_a_pdf_from_a_python_dictionary(cv_data, Path("out.pdf"))
    print("Success!")
except Exception as e:
    print(f"Error creating PDF: {e}")
    traceback.print_exc()
