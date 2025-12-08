from .models import BaseInfo
from .helpers import clarify_job_requirements, pull_relevant_cv_material, generate_professional_summary, build_optimized_resume
from .inputs import job_input, cv_input
def main():
    print("Welcome to Resume Optimizer!")
    job_description = job_input
    source_cv_data = cv_input

    job_details = clarify_job_requirements(job_description)

    relevant_material = pull_relevant_cv_material(source_cv_data, job_details)
    professional_summary = generate_professional_summary(relevant_material, job_details)

    base_info: BaseInfo = BaseInfo()

    build_optimized_resume(base_info, relevant_material, professional_summary)