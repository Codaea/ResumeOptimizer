summary = """
Write a concise, impactful professional summary for the top of a resume, following these strict guidelines: the summary must be 2–3 short sentences and must not exceed 3 lines of text. This summary should introduce the candidate, highlight their most relevant strengths and qualifications, and clearly present their value, but must not reference or allude to any specific employer, company, or target job. The summary should appear as a standard, general-purpose resume section suitable for multiple roles, rather than being tailored or overtly targeted to a particular position or organization.

Before writing, carefully analyze the provided resume and any associated job requirements. Internally, reason through what sets the candidate apart—consider unique skills, standout achievements, and directly relevant strengths. Do not begin writing the summary until this internal analysis is complete.

- Focus on clear, succinct language appropriate for a “Summary” or “Profile” section of a resume.
- Do not use bullet points, lists, formatting (such as bold or italics), or extraneous information—output plain text only.
- Write in third person (unless otherwise specified).
- The output must be a single, continuous response of 2–3 SHORT sentences (no sentence fragments), and must not exceed three lines in total length.
- Prioritize brevity, impact, and general applicability. Avoid overly long or complex sentences, and do not include details that are specific to a particular employer or job posting.
- Do not make overt or subtle references to any company, organization, or job title; keep the tone objective and professional.
- Highlight only the most universally transferable strengths and qualifications.

# Steps

1. Thoroughly review the provided resume and, if applicable, job requirements.
2. Identify the candidate’s most universally relevant qualifications, achievements, and skills.
3. Internally reason through what makes the candidate stand out among peers.
4. Write a summary in 2–3 short sentences, fitting within 3 lines, that communicates the candidate’s unique and broadly marketable value and strengths, without referencing any employer or job.

# Output Format

- Output only a plain-text summary consisting of 2–3 short sentences, not exceeding 3 lines.
- Do not use any formatting, markdown, or bullet points.
- Use first person (unless otherwise specified).
- The summary should be concise, professional, and suitable as a general resume summary, not tailored to a specific company or job.

# Examples

**Example Input (resume excerpt):**
- 5 years as marketing manager
- Led team to 130% revenue growth in 2 years
- Skilled in digital and content marketing
- Certified HubSpot and Google Ads

**Example Output:**  
Experienced marketing manager with a strong record of driving revenue growth. Expertise in digital and content marketing, supported by leading industry certifications. Recognized for strategic leadership and delivering measurable results.

*(Note: The summary above avoids any references to a specific organization or job, focusing only on skills and achievements. Actual outputs may be even more concise, depending on resume content.)*

# Reminder
First analyze and reason through the candidate’s resume and strengths internally. Only then, write a concise, general-purpose summary, ensuring all output is within the defined length and never references any specific company or job.
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

5. FORMAT output as structured JSON:
   - For start_date and end_date use YYYY-MM format. if currently employed, end_date should be an empty string.

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