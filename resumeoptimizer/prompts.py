summary = """
You are writing a professional summary for the top of a resume.
INSTRUCTIONS:

Write a 2-3 sentence professional summary that:

1. LEADS with credentials that match the role:
   - Current role/status (e.g., "Computer Science student at Oregon State")
   - Key technical areas (e.g., "specializing in backend systems and observability")
   - Years of experience with relevant technologies if applicable

2. HIGHLIGHTS 1-2 impressive achievements present in the resume:
   - Presentations/talks
   - Known companies
   - Significant projects
   - Only mention if it's actually in the resume below

3. CONNECTS to their ideal candidate description:
   - Reference their company keywords naturally
   - Frame experience in their language
   - Align with the role type

WRITING STYLE:
- Clear, confident, direct
- No buzzwords or fluff ("passionate", "driven", "rockstar")  
- Active voice, concrete nouns
- Scannable in 3 seconds

AVOID:
- Listing achievements better left for work experience bullets
- Repeating the job description back to them
- Generic statements ("team player", "fast learner")
- Adverbs and qualifiers

The summary should make someone think "this person matches what we need" not "this person really wants this job."

Output just the summary text, 2-3 sentences.
"""

cv_to_resume = """
You are optimizing a resume to match a specific job posting.

Your goal: Make a recruiter scanning this resume for 8 seconds think "this candidate is qualified."

CONSTRAINTS:
- Select top 3 work experiences
- Select top 2 projects  
- Select 10-12 most relevant skills

INSTRUCTIONS:

1. SELECT the most relevant items from each category based on:
   - Direct technical skill matches
   - Relevant responsibilities/experience
   - Impressive signal (awards, talks, known companies)

2. REWRITE bullets to emphasize relevance:
   - Lead with impact/achievement
   - Include specific technologies from their skills list
   - Use active, concrete language
   - Keep bullets scannable (1-2 lines max)
   - Mirror their terminology naturally (don't force keywords)

3. ORDER within categories by:
   - Most impressive/relevant first
   - Recent work before old work
   - Clear progression if applicable

4. PRIORITIZE scannable signal:
   - Quantified results where possible
   - Recognizable achievements (presentations, awards)
   - Technologies that match their critical skills

Remember: A tired recruiter is skimming. Make the relevant parts obvious.

Output structured JSON with selected items and optimized bullets.
"""

extract_job_details = """
You are analyzing a job posting to extract structured requirements for resume optimization.

Extract the following information:

1. ROLE INFORMATION
   - Job title
   - Company name
   - Role type (intern, new_grad, junior, mid, senior, staff)
   - Domain/department if mentioned

2. TECHNICAL SKILLS
   Extract ALL mentioned technologies, languages, frameworks, tools, and platforms.
   List each skill exactly as it appears in the posting.
   Note: If a skill is mentioned multiple times or emphasized (e.g., "primary language", "must have"), mark it as high priority.

3. EDUCATION & EXPERIENCE
   - Degree requirements (pursuing, completed, level)
   - Preferred majors/fields
   - Years of experience if specified
   - GPA requirements if mentioned

4. KEY RESPONSIBILITIES
   - What will the person actually be doing?
   - Main focus areas of the role
   - Types of projects or work

5. SOFT SKILLS & ATTRIBUTES
   - Teamwork, communication, leadership, etc.
   - Work style preferences mentioned
   - Cultural fit indicators

6. COMPANY CULTURE & VALUES
   - Keywords describing company culture
   - Values emphasized in the posting
   - Work environment (fast-paced, innovative, collaborative, etc.)

7. ATS KEYWORDS
   - Frequently repeated terms and phrases
   - Industry-standard terminology
   - Action verbs used to describe the role

8. SPECIAL REQUIREMENTS
   - Work authorization
   - Location/relocation
   - Security clearance
   - Any disqualifying factors

Output as structured JSON. Preserve exact technology names as written for ATS compatibility.
"""