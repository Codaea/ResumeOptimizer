system_prompt = """
You are a resume optimization expert. Rewrite the provided resume material to be concise, recruiter-friendly, and highly aligned with the job description.

CRITICAL DIRECTIVES:
1. BE SELECTIVE: Include ONLY content that directly matches the job requirements. Exclude unrelated projects, skills, and experiences.
2. BE CONCISE: Recruiters spend 6-10 seconds per resume. Every bullet point must be impactful and scannable.
3. USE JOB KEYWORDS: Extract and incorporate exact terminology from the job description (e.g., "ship and deliver", "cross-functional", "autonomy").
4. PRIORITIZE IMPACT: Lead with quantifiable achievements, shipped products, and demonstrated learning ability.
5. Output ONLY valid JSON—no explanations, reasoning, or additional text.

OUTPUT FORMAT (JSON):
{
  "WorkExperience": [
    {
      "company": "Company Name",
      "position": "Job Title",
      "location": "City, State",
      "highlights": [
        "Brief, impactful achievement (1 line max) with job-relevant keywords",
        "Only include 2-3 highlights per role that match job requirements"
      ]
    }
  ],
  "Education": [
    {
      "institution": "University Name",
      "area": "Field of study",
      "degree": "Degree type abev. (BS, MS, PhD, etc.)",
      "location": "City, State",
      "start_date": "YYYY-MM",
      "end_date": "YYYY-MM or Expected YYYY-MM"
    }
  ],
  "Skills": [
    {
      "label": "Category matching job requirements",
      "details": "Only skills directly relevant to the role"
    }
  ],
  "Projects": [
    {
      "name": "Project Name",
      "description": "One-line description showing relevance to job requirements",
      "highlights": [
        "Key achievement or technology match (1 line)",
        "Impact or learning outcome (1 line)"
      ]
    }
  ]
}

CONTENT RULES:
- WorkExperience: Include only 1-2 most relevant roles. Highlights must be 1 line max, action-oriented.
- Education: Include only if degree is in Computer Science, Engineering, Mathematics, or related field.
- Skills: Group by category (Languages, Tools, Platforms). List ONLY skills used in relevant projects/roles.
- Projects: Include maximum 3-4 projects that demonstrate: shipped products, learning ability, or technical relevance.
- Dates: Always use YYYY-MM format.
- Language: Mirror job description terminology (e.g., "shipped", "autonomy", "cross-functional").

SELECTION CRITERIA:
Prioritize experiences that demonstrate:
- Ability to ship and deliver completed projects
- Learning new technologies independently
- Cross-functional collaboration or team work
- Direct technical relevance to job requirements
- Initiative and curiosity

EXCLUSIONS:
- Unrelated side projects
- Generic skills
- Outdated or irrelevant experience
- Verbose descriptions
"""

source_cv_data = """
PROFILE
Curious and self-taught software developer pursuing a B.S. in Applied Computer Science at Oregon State University. Experienced in full-stack development, data visualization, and AI-driven tooling. Skilled at turning unconventional ideas into functional systems from educational software to creative observability projects. Passionate about building reliable, maintainable software with measurable impact. Actively seeking opportunities to contribute to research or open-source projects where software meets real-world experimentation.

EDUCATION
Oregon State University - Corvallis, OR
Bachelor of Science in Applied Computer Science - Expected June 2029
RESEARCH EXPERIENCE
Adopted Capstone Project - AI Education Labs & Oregon State University
October 2025 - Present
Collaborating on the development of an educational software platform using React, FastAPI, and LLM-based tooling. Focused on reducing technical debt, improving code quality, and implementing new product features within a research-driven environment.

PUBLICATIONS & TALKS
“My Laundry Dashboard and Other Absurdly Unconventional Uses for Grafana” – GrafanaCON 2025
Delivered a lightning talk on creative observability, exploring how Grafana can visualize anything—from laundry cycles to environmental data. Originated as a blog post before evolving into a conference talk.

“Dashboards and Detergent: How Two Students Monitor Laundry Machines in a College Dorm with Grafana” – May 2025
Interviewed for a companion article expanding on the GrafanaCON presentation, demonstrating practical and humorous applications of observability tools beyond traditional metrics.

PREVIOUS EMPLOYMENT
South Lane School District - Technology Intern
Migrated the district’s website to a new hosting provider, managing CMS configuration and content transfer for multiple schools.
Supported teachers and staff by resolving classroom technology issues; tracked, managed, and closed tickets using Spiceworks Helpdesk.
Integrated Spiceworks data into Grafana dashboards to visualize IT metrics and improve helpdesk responsiveness.
Assisted with setup and deployment of a Meshtastic node on a local radio tower to improve community communication infrastructure.
PERSONAL PROJECTS
Browser Exporter: Prometheus exporter for Chrome  (Typescript) - Author 
Built a Chrome extension that exports browser telemetry (open tabs, resource usage). and a Prometheus-compatible exporter to expose these metrics for monitoring.

Integrated with Pushgateway, created Grafana dashboards, and documented deployment workflows for monitoring adoption.

simpleprint: Print server API for ESC/POS receipt printers (Go + Vue) - Author
Developed a lightweight Go REST API to route and format print jobs for ESC/POS printers, simplifying web to kiosk integrations.
Built a Vue frontend to generate print payloads and formatting images; Added CI, release artifacts, and documentation to support production usage

polaroid-thermal-printer : Web frontend for receipt image printing (Nuxt) - Author
Created a web UI to resize/format images for thermal printers and integrate with the simpleprint API for end-to-end printing workflows
deployed a demo to a dorm-floor printing workflow
Packaged and maintained repository with CI and release-ready artifacts

Obsidian-lecture-copilot: Obsidian plugin for lecture assistance (Typescript) - Author
Built an Obsidian plugin to assist lecture note-taking workflows. 
Implemented realtime ASR workflows and LLM models to parse and rewrite lectures to a humanreadable format

Breathe: Webapp for guided breathing that fits in a QR code (Typescript) - Author
Created a minimal web app that fits entirely with a QR code, built for Hack Club’s say cheese event.
Published a blog post analyzing QR data compression, browser bundling limits, and creative design constraints

Oregon State Observability: Campus telemetry dashboards (Go, Python)
Collected and visualized telemetry from publicly accessible Oregon State University endpoints
Valley Library Occupancy: Built a data ingestion pipeline from publicly accessible endpoints
MU Quad heatmaps: Used openCV motion detection with public camera feeds to visualize walking patterns 

Luke Ferry Tracker: Webapp for marking and viewing locations (Nuxt, Supabase)
Designed and deployed a location-tracking web app from concept to production in under 5 hours
Map based marking and viewing with persistent Supabase storage

Homelab: Personal server cluster for selfhosting (Variety of Technologies)
Operate a personal homelab cluster for self-hosting and production deployment
Responsibilities include Linux maintenance, Virtualization (VMs), container orchestration with Docker
Running self-developed applications in production to minimise cloud expenditure. Focus on reliability, resource optimisation and self-service tooling

Personal Blog Website: CMS for personal blog (Nuxt)
Custom blog/CMS using Nuxt and Nuxt content to convert markdown into performant HTML pages
Implemented CI/CD pipeline to run builds and deploy the site on content or code updates, ensuring fast, repeatable releases.


"""
job_description_data = """
Software Engineer Intern (Summer 2026) - Austin, TX

 

About Us

At Cloudflare, we are on a mission to help build a better Internet. Today the company runs one of the world’s largest networks that powers millions of websites and other Internet properties for customers ranging from individual bloggers to SMBs to Fortune 500 companies. Cloudflare protects and accelerates any Internet application online without adding hardware, installing software, or changing a line of code. Internet properties powered by Cloudflare all have web traffic routed through its intelligent global network, which gets smarter with every request. As a result, they see significant improvement in performance and a decrease in spam and other attacks. Cloudflare was named to Entrepreneur Magazine’s Top Company Cultures list and ranked among the World’s Most Innovative Companies by Fast Company. 

We realize people do not fit into neat boxes. We are looking for curious and empathetic individuals who are committed to developing themselves and learning new skills, and we are ready to help you do that. We cannot complete our mission without building a diverse and inclusive team. We hire the best people based on an evaluation of their potential and support them throughout their time at Cloudflare. Come join us! 

Available location(s): Austin, US

About Cloudflare's Engineering Teams

Anytime we push code, it automatically affects the millions of Internet properties (powering websites, remote teams, APIs, mobile apps, etc.) running on our global network. Cloudflare's network is one of the largest in the world and spans over 330 cities in more than 125 countries. What's more, Cloudflare operates within 50 milliseconds of 95% of the Internet-connected population globally (for context, the blink of an eye is 300-400 milliseconds!). We are passionate about making the Internet more secure, reliable, and faster for everyone.

Cloudflare’s Engineering teams build and run the software that handles the massive amount of traffic that flows through our network. We also have teams that build the UI and control plane for our software, using modern patterns and libraries in a microservices-based architecture. Technologies include: Typescript/Javascript, Go, Rust, C/C++ and Python.

About the Internship Program

The ideal summer intern is passionate about making the Internet a better place. You will work alongside experienced engineers. You will push code this summer that touches hundreds of millions of web surfers. We like to get things done, so we are looking for interns who are curious, proactive, and able to complete projects. This is a great opportunity for engineers who want to learn to develop at Internet scale.

What would you do as a Cloudflare intern?

Ship and deliver projects over 12-16 weeks with autonomy and support.
Work cross-functionally with various teams.
Work closely with a mentor to guide you through the internship and help with career goals.
Build your network across the company through our various in and out of office socials, networking programs, Employee Resource Group (ERG) programs, and Activity Groups.
Present your project to the entire company at the end of the internship.
Connect and learn from our executives and leadership team including our co-founders.
Learn and develop skills through our professional development workshops.
Write for our Cloudflare blog and be featured on Cloudflare.tv sessions. 
You can check out our internship blogs to learn more about our program and hear directly from our past interns.

Examples of desirable skills, knowledge and experience

Currently pursuing a degree or program in Computer Science, Engineering, Mathematics, Statistics or relevant field to the role.
Demonstrated critical thinking skills and drive to learn and adapt new technologies.
Curiosity, empathy and ability to get things done.
Ability to commit to a minimum 12 week summer internship.
In office 3-5 days a week in Austin, TX.
Bonus: demonstrated passion for software development, such as personal projects, open-source contributions, or experience with our developer platform Cloudflare Workers.
Please note

We will be hiring interns through the fall and early spring on a rolling basis until all roles are filled.
What Makes Cloudflare Special?

We’re not just a highly ambitious, large-scale technology company. We’re a highly ambitious, large-scale technology company with a soul. Fundamental to our mission to help build a better Internet is protecting the free and open Internet.

Project Galileo: Since 2014, we've equipped more than 2,400 journalism and civil society organizations in 111 countries with powerful tools to defend themselves against attacks that would otherwise censor their work, technology already used by Cloudflare’s enterprise customers--at no cost.

Athenian Project: In 2017, we created the Athenian Project to ensure that state and local governments have the highest level of protection and reliability for free, so that their constituents have access to election information and voter registration. Since the project, we've provided services to more than 425 local government election websites in 33 states.

1.1.1.1: We released 1.1.1.1 to help fix the foundation of the Internet by building a faster, more secure and privacy-centric public DNS resolver. This is available publicly for everyone to use - it is the first consumer-focused service Cloudflare has ever released. Here’s the deal - we don’t store client IP addresses never, ever. We will continue to abide by our privacy commitment and ensure that no user data is sold to advertisers or used to target consumers.

Sound like something you’d like to be a part of? We’d love to hear from you!
"""