# Inputs for testing


cv_input = """
cv:
  name: Dakota Roth
  location: Corvallis, OR
  email: dakotajayroth@gmail.com
  phone: +1-541-206-9437
  website: https://codaea.com
  social_networks:
    - network: LinkedIn
      username: codaea
    - network: GitHub
      username: codaea
  sections:
    previous_experience:
      - company: AI Education Labs
        position: Software Engineer
        start_date: 2025-07
        location: Corvallis, OR
        highlights: 
          - Collaborated on the development of educational software platform using React, FastAPI, and LLM-based tooling
          - Reduced technical debt, improving code quality, and implementing product features within a research-driven environment
      - company: South Lane School District
        position: Technology Intern
        start_date: 2024-07
        end_date: 2025-06
        highlights: 
          - Migrated company website to new hosting provider, managing CMS configuration and content transfer for multiple sites.
          - Supported teachers and staff by resolving classroom ticket technology issues; tracked, managed, and closed tickets on a agile platform.
          - Deployed a meshtastic node to the local community radio tower, leading the strive for mesh networks
          - Managed & Deployed production Nutanix and linux systems for computer science labs
      - company: CGHS Hack Club
        summary: Local chapter of Hack Club, a nationwide coding club for high school students
        position: Founder & President
        start_date: 2023-09
        end_date: 2025-06
        highlights:
          - Organized and ran weekly meetings and coding workshops to foster a collaborative learning environment
          - Mentored students on personal coding projects, helping them develop technical skills and confidence
          - Created a supportive community for students to explore their interests in technology and programming
      - company: Fruitcraft
        summary: Minecraft server network 
        position: Lead Developer
        start_date: 2023-06
        end_date: 2023-09
        highlights:
          - Developed and maintained custom Minecraft server plugins using Java and the Spigot API to enhance gameplay and user experience.
          - Designed and implemented a scaling minigame based system to support hundreds of concurrent players.
    education:
      - institution: Oregon State University
        area: Applied Computer Science
        degree: BS
        start_date: 2025-09
        end_date: 2029-06
        location: Corvallis, OR, USA
        highlights: 
          - Worked on research in the psychology department as a technical undergrad, building software tools to facilitate studies.
          - Concurrent enrollment at Lane Community College to accelerate prerequisite completion and take advanced CS coursework earlier
    speaking_engagements:
      - name: My Laundry Dashboard and Other Absurdly Unconventional Uses for Grafana
        date: 2025-7-5
        summary: Delivered a lightning talk on creative observability, exploring how Grafana can visualize anything from laundry cycles to environmental data. Originated as a blog post before evolving into a conference talk.
    projects:
      - name: Digital Super 8
        date: 2024
        summary: Designed and built custom 3D printed Super 8 film cartridge
        skills: Fusion 360, Linux, Python, FDM Printing, soldering
        highlights:
          - Designed and 3D printed a custom cartridge to hold a Raspberry Pi Zero W and camera module, powered by a lithium battery pack
          - Developed python script to record video inside the cartridge
          - 26 GitHub stars
      - name: Browser Exporter
        date: 2025
        summary: Prometheus exporter for Chrome browser telemetry (TypeScript)
        skills: Observability, Prometheus, TypeScript, Chrome Extensions
        highlights:
          - Built a Chrome extension that exports browser telemetry (open tabs, resource usage) and a Prometheus-compatible exporter to expose these metrics for monitoring
          - Integrated with Pushgateway, created Grafana dashboards, and documented deployment workflows for monitoring adoption
          - Presented at GrafanaCON 2025 as a lightning talk on creative observability applications
      - name: Obsidian Lecture Copilot
        date: 2025
        summary: Obsidian plugin for transcribing and summarizing lectures
        skills: Prompt Engineering, Obsidian Plugin Development, ASR, LLMs
        highlights:
          - Developed an Obsidian plugin to integrate the transcription and summarization workflows directly into note-taking
          - Implemented realtime ASR workflows and LLM models to parse and rewrite lectures to a human-readable format
      - name: simpleprint
        date: 2024-01
        summary: Print server API for ESC/POS receipt printers (Go + Vue)
        highlights:
          - Developed a lightweight Go REST API to route and format print jobs for ESC/POS printers, simplifying web to kiosk integrations
          - Built a Vue frontend to generate print payloads and format images; Added CI, release artifacts, and documentation to support production usage
      - name: polaroid-thermal-printer
        date: 2024-01
        summary: Web frontend for receipt image printing (Nuxt)
        highlights:
          - Created a web UI to resize/format images for thermal printers and integrate with the simpleprint API for end-to-end printing workflows
          - Deployed a demo to a dorm-floor printing workflow
          - Packaged and maintained repository with CI and release-ready artifacts
      - name: Simpleprint Request Generator
        date: 2025
        summary: HTML tool for generating print requests for simpleprint API
        skills: Web Development, HTML, JavaScript, Alpine.js
        highlights:
          - API testing utility to generate and preview print requests for the simpleprint API
          - Built with Alpine.js for minimal dependencies and easy deployment
      - name: ToDo Print
        date: 2025
        summary: Printing Kaban Cards to Thermal Printer, for real life agile task management
        skills: Web Development, HTML, JavaScript, Alpine.js
        highlights: 
          - Designed with low friction task management in mind, allowing users to quickly print task cards for physical tracking
          - Integrated with simpleprint API for seamless printing workflows
      - name: Breathe
        date: 2025
        summary: Webapp for guided breathing that fits in a QR code
        skills: Data Compression, QR Codes, Web Development
        highlights:
          - Created a minimal web app that fits entirely within a QR code, built for Hack Club's say cheese event
          - Published a blog post analyzing QR data compression, browser bundling limits, and creative design constraints
      - name: AQI Thing
        date: 2025
        summary: API proxy for PurpleAir and Daktronix based screens
        skills: Go, REST APIs, IoT
        highlights:
          - Developed a Go-based API proxy to fetch and reformat air quality data from PurpleAir
          - Enabled integration with Daktronix screens for real-time AQI display
      - name: Oregon State Observability
        date: 2025-07
        summary: Campus telemetry dashboards (Go, Python)
        skills: Observability, Prometheus, Grafana, Python, Go 
        highlights:
          - Collected and visualized telemetry from publicly accessible Oregon State University endpoints
          - Valley Library Occupancy - Built a data ingestion pipeline from publicly accessible endpoints
          - MU Quad heatmaps - Used OpenCV motion detection with public camera feeds to visualize walking patterns
      - name: Homelab
        date: 2023
        summary: Personal server cluster for self-hosting (Variety of Technologies)
        highlights:
          - Operate a personal homelab cluster for self-hosting and production deployment
          - Responsibilities include Linux maintenance, virtualization (VMs), container orchestration with Docker
          - Running self-developed applications in production to minimize cloud expenditure with focus on reliability, resource optimization and self-service tooling
        skills:
          - Linux System Administration
          - Docker and Containerization
          - Networking and Security
          - DevOps
          - Infrastructure as Code (IaC)
      - name: Personal Blog Website
        date: 2024
        summary: CMS for personal blog 
        skills: Nuxt, Nuxt Content, CI/CD, DevOps
        highlights:
          - Custom blog/CMS using Nuxt and Nuxt Content to convert markdown into performant HTML pages
          - Implemented CI/CD pipeline to run builds and deploy the site on content or code updates, ensuring fast, repeatable releases
    skills:
      - label: Programming Languages
        details: Go, TypeScript, Python, Java, Bash, HTML, CSS
      - label: Frameworks & Libraries
        details: Vue, Nuxt, React, Next, FastAPI, Prometheus, Grafana
      - label: Tools & Platforms
        details: Docker, Git, Linux, Fusion 360, OBS Studio, Raspberry Pi, 3D Printing
"""

job_input = """
WHAT MAKES US EPIC?

At the core of Epic’s success are talented, passionate people. Epic prides itself on creating a collaborative, welcoming, and creative environment. Whether it’s building award-winning games or crafting engine technology that enables others to make visually stunning interactive experiences, we’re always innovating.

Being Epic means being a part of a team that continually strives to do right by our community and users. We’re constantly innovating to raise the bar of engine and game development.

ENGINEERING - GAMES

What We Do

Unreal projects have been leading the pack of real-time entertainment with our constantly growing team of engineering experts. We’re always improving on the tools and technology that empower content developers worldwide.

GAMEPLAY PROGRAMMER INTERN

What You'll Do

The Walt Disney Company and Epic Games are collaborating on an all-new games and entertainment universe. We are a new and growing team at Epic, aiming to build innovative new experiences and technology as part of our collaboration with Disney. As a Gameplay Programmer Intern, you will contribute to the development of core gameplay features and get hands-on experience working alongside programmers, designers, and artists.

In this role, you will

• Assist in prototyping and implementing gameplay features in collaboration with art and design
• Help debug, test, and fix bugs in gameplay systems
• Learn to write clean, maintainable C++ code
• Participate in team discussions, offering ideas and feedback

What We're Looking For

• Strong C++ knowledge
• Interest in gameplay programming
• Strong problem-solving skills
• Good interpersonal and communication skills, with demonstrated ability to communicate within a team
• The ability to react and respond effectively to constructive feedback

This internship has a flexible start date in 2026. Recruitment will be ongoing until teams find an ideal match. Applicants must be legally authorized to work in the posting location for the duration of the internship. For more information about Epic’s Early Career Program, visit epicgames.com/earlycareers. This is going to be Epic!

About Us

Epic Games spans across 25 countries with 46 studios and 4,500+ employees globally. For over 25 years, we've been making award-winning games and engine technology that empowers others to make visually stunning games and 3D content that bring environments to life like never before. Epic's award-winning Unreal Engine technology not only provides game developers the ability to build high-fidelity, interactive experiences for PC, console, mobile, and VR, it is also a tool being embraced by content creators across a variety of industries such as media and entertainment, automotive, and architectural design. As we continue to build our Engine technology and develop remarkable games, we strive to build teams of world-class talent.

Like what you hear? Come be a part of something Epic!

Epic Games deeply values diverse teams and an inclusive work culture, and we are proud to be an Equal Opportunity employer. Learn more about our Equal Employment Opportunity (EEO) Policy here.

Note to Recruitment Agencies: Epic does not accept any unsolicited resumes or approaches from any unauthorized third party (including recruitment or placement agencies) (i.e., a third party with whom we do not have a negotiated and validly executed agreement). We will not pay any fees to any unauthorized third party. Further details on these matters can be found here.
"""