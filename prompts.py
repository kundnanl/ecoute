INITIAL_RESPONSE = "Best of Luck for the Interview"

def create_prompt(transcript):
    resume = """
LAKSH RAJESHKUMAR KUNDNANI
200 Malta Avenue, Brampton, ON, L6Y 6H8
(647) 897 3510 | kundnanl@sheridancollege.ca | LinkedIn | Portfolio | GitHub

HIGHLIGHTS OF QUALIFICATIONS
- Possessing strong interpersonal and communication skills, including verbal and written communication,
quality assurance, test automation, ML model training and evaluation, enabling effective collaboration
and information sharing, essential for troubleshooting and problem-solving in team projects.
- Holding an AWS Certified Cloud Practitioner certification, with hands-on experience in utilizing one of
the major cloud platforms (services such as EC2, S3, Load Balancer, Firewalls, VPC).
- Additionally, I bring my knowledge of various Software Development Life Cycle (SDLC)
methodologies, SOLID design principles, CI/CD pipeline, and streamlined API development.
- Furthermore, I have familiarity and comprehension of Programming Languages, frameworks,
microservices, adaptability, UML (Visual Paradigm, draw.io, etc.), and technology business requirements
definition, enhancing my capabilities to tackle complex challenges.

TECHNICAL SKILLS
Programming Languages: Java, JavaFX, R, JavaScript, HTML, CSS, XML, PHP, Python (Pandas, PyTorch,
TensorFlow, scikit-learn, etc.), C#, shell/bash scripting.
Frameworks: React Native, Node.js, Selenium, Spring security (MVC concepts), AngularJS
Software: NetBeans, Twine, Microsoft Office (Word, Excel, PowerPoint, Visio, Outlook, SharePoint), SQL
Server, PowerBI, Git, Microsoft visual studio, Salesforce, Atlassian Tools (Jira, Bitbucket)
Operating Systems: Mac iOS, Unix/Linux, Android, Windows
Database: PL/SQL, MySQL, Oracle, MS SQL Server, JSON, MongoDB, Firebase, NoSQL, Docker
Networking: VLAN, TCP/IP, DNS, IP subnetting, Cisco Routers, WAN, ICMP, LAN, ACL, Wireshark
Others: Agile Methodologies (Scrum, Kanban), Junit, AWS (Load balancing, VPN, NAT), REST/SOAP, Web API

EDUCATION
Software Development & Network Engineering Advanced Diploma January 2023 - August 2025
Sheridan College, Brampton, Ontario
- GPA: 3.84 / 4.0
- Relevant course work: Enterprise Java Development, Systems dev methodologies, Computer and Network
Security, Database design and implementation, and Computer Architecture
- Founded and led a programming club with over 150+ members, demonstrating strong leadership acumen by
providing mentorship and guidance to students in enhancing their programming skills.
- Conducted group research about different chat bots implementing different AI algorithms.

RELEVANT WORK EXPERIENCE
Applied Computing Tutor, Sheridan College January 2024 - April 2024
- Facilitated interactive learning sessions for students enrolled in applied computing courses, fostering a
collaborative and engaging learning environment.
- Developed customized learning materials and exercises tailored to students' needs, ensuring comprehension and
mastery of key concepts in computer science and programming.
- Provided personalized assistance and guidance to students, addressing their questions and concerns related to
course content, assignments, and projects.
- Evaluated student performance through assessments and feedback, identifying areas for improvement and
implementing strategies to support student success.
- Collaborated with faculty members to align course objectives with industry standards and emerging trends in
applied computing, enhancing the relevance and effectiveness of the curriculum.

Research Assistant, Vasishtha Group of Schools April 2023 - October 2023
- Conducted extensive research on educational technology integration, focusing on optimizing digital learning
platforms and enhancing student engagement.
- Assisted in the development and implementation of data acquisition systems for educational research projects,
utilizing IoT architectures and sensor technologies.
- Contributed to the analysis and interpretation of research data, employing machine learning algorithms and data
analytics techniques.
- Engaged in regular team meetings and presentations, effectively communicating project progress and findings to
stakeholders.

ACADEMIC PROJECTS
Discord Clone, Sheridan College, Brampton, ON November 2023 – December 2023
- Employed Socket.io for real time messaging, demonstrating expertise in WebSocket communication, event
handling, ensuring seamless, instantaneous user interactions.
- Implemented robust database management using Prisma ORM and MySQL on Planetscale, showcasing skills
in database design, optimization, and secure data handling, ensuring efficient and scalable data operations.
- Crafted an aesthetically pleasing and responsive UI with TailwindCSS and ShadcnUI, showcasing proficiency
in modern front-end technologies for an engaging and user-friendly experience.

Data Guard, Geek Fest Hackathon, Bell September 2023 – October 2023
- Create an innovative solution to protect sensitive data from cyber-attacks and ensure data privacy.
- Proposed solution: developed a project implementing multi-layered security solution based on a defense in
depth strategy through efficient team collaboration.
- Integrated AES-256 + homomorphic encryption at the application layer with a machine learning model
to decrypt the solution (without sharing the private/public keys/flags) working with an anomaly
detection, demonstrating creative thinking and technology business requirements definition.

CERTIFICATIONS
- Python Essentials II July 2023
- AWS certified Cloud Practitioner September 2023
- Introduction to Cyber Security by Cisco July 2023
    """

    return f"""
You will receive a transcript of a job interview conversation. When the interviewer asks a question, respond appropriately.

Resume: {resume}

Transcript of the conversation between you and the interviewer:
{transcript}

If the question is situational or behavioral, respond using the STAR method (Situation, Task, Action, Result). For technical questions, provide a detailed explanation of the concept or technology. If the question is about your resume, explain the relevant experience or project in detail.

Please respond confidently and directly in square brackets without asking for clarification or repetition.

"""

