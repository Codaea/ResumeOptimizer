from openai import OpenAI
from .models import JobDetails, RelevantMaterial, BaseInfo
import rendercv
from pathlib import Path
import .prompts as prompts

client = OpenAI()

def clarify_job_requirements(job_description: str) -> JobDetails:
    print("Clarifying job requirements...")
    # Implementation goes here
    response = client.responses.parse(
        model='gpt-5-mini',
        input=[
            {
                "role": "system",
                "content": prompts.extract_job_details
            },
            {
                "role": "user",
                "content": job_description
            }
        ]
        text_format=JobDetails
    )

    if response.output_parsed is None:
        raise ValueError("Failed to parse job requirements")
    
    return response.output_parsed

def pull_relevant_cv_material(source_cv_data: str, job_description_data: JobDetails) -> RelevantMaterial:
    print("Extracting relevant material...")
    # Implementation goes here
    response = client.responses.parse(
        model='gpt-5-mini',
        input=[
            {
                "role": "developer",
                "content": prompts.cv_to_resume
            },
            {
                "role": "user",
                "content": f"SOURCE MATERIAL: {source_cv_data}"
            },
            {
                "role": "user",
                "content": f"SOURCE JOB DESCRIPTION: {job_description_data}"
            }
        ],
        text_format=RelevantMaterial
    )
    if response.output_parsed is None:
        raise ValueError("Failed to parse relevant CV material")
    # work experience, projects, skills, education
    return response.output_parsed

def generate_professional_summary(relevant_material: RelevantMaterial, job_details: JobDetails) -> str:
    print("Generating professional summary...")
    # Generate summary from extracted material
    response = client.responses.create(
        model='gpt-5-mini',
        input=[
            {
                "role": "developer",
                "content": prompts.summary
            },
            {
                "role": "user",
                "content": f"Relevant Material: {relevant_material}"
            },
            {
                "role": "user",
                "content": f"Job Details: {job_details}"
            }
        ]
    ),
    return response[0].output_text

def build_optimized_resume(base_info: BaseInfo, relevant_material: RelevantMaterial, summary: str):
    print("Building optimized resume...")
    # Combine all parts into final resume
    cv_data: dict = {
        "cv": {
            "name": base_info.name,
            "location": base_info.location,
            "email": base_info.email,
            "phone": base_info.phone,
            "website": base_info.website,
            "social_networks": [
                { "network" : "LinkedIn", "username": base_info.linkedin },
                { "network" : "GitHub", "username": base_info.github }
            ],
            "sections": {
                "summary": [ summary ],
            },
        }
    }

    # Append relevant material sections
    
    cv_data['cv']['sections']['education'] = [entry.model_dump() for entry in relevant_material.Education]
    cv_data['cv']['sections']['work experience'] = [entry.model_dump() for entry in relevant_material.WorkExperience]
    cv_data['cv']['sections']['projects'] = [entry.model_dump() for entry in relevant_material.Projects]
    cv_data['cv']['sections']['skills'] = [entry.model_dump() for entry in relevant_material.Skills]

    print(cv_data)
    print("Generating PDF...")
    # build cv dict into pdf
    try: 
        rendercv.api.create_a_pdf_from_a_python_dictionary(cv_data, Path("out.pdf"))
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()