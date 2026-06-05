from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# Australian Format PDF
def create_australian_pdf():
    filename = 'Rolyn_Kiunisala_CV.pdf'
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=8,
        spaceBefore=6,
        fontName='Helvetica-Bold',
        borderPadding=3,
        borderColor=colors.HexColor('#e2e8f0'),
        borderWidth=0.5,
        borderBottom=1
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        leading=12
    )
    
    # Header
    story.append(Paragraph("ROLYN KIUNISALA", title_style))
    story.append(Paragraph("Full Stack Software Developer | Software Engineer", subtitle_style))
    story.append(Paragraph("Cebu, Philippines | rolynkiunisala@gmail.com | +63 906 454 4620<br/>LinkedIn: linkedin.com/in/rolyn-kiunisala-b862ab377", body_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    story.append(Paragraph("Full Stack Software Developer with over 3 years of experience in designing, developing, and maintaining enterprise and web-based applications. Skilled in backend and frontend development, API integration, and system enhancement within Agile environments. Experienced in delivering client-based solutions, automation initiatives, and cloud-based deployments. Strong ability to adapt quickly to new technologies and contribute to scalable software systems.", body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Core Skills
    story.append(Paragraph("CORE SKILLS", heading_style))
    skills = [
        "<b>Programming Languages:</b> Java, JavaScript, C#, Python, PHP",
        "<b>Frontend:</b> HTML, CSS/SCSS, JavaScript, Angular, React (basic)",
        "<b>Backend:</b> Node.js, .NET, Java, Python",
        "<b>Database:</b> MySQL, SQL",
        "<b>Cloud & DevOps:</b> AWS, Azure DevOps, CI/CD, Lambda",
        "<b>Tools:</b> Git, GitHub, VS Code, Visual Studio, GitHub Copilot",
        "<b>Methodologies:</b> Agile / Scrum",
        "<b>Other:</b> REST API Development, System Integration, Debugging, Deployment, Network Basics, SCM"
    ]
    for skill in skills:
        story.append(Paragraph("• " + skill, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    story.append(Paragraph("<b>Full Stack Software Developer</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'))))
    story.append(Paragraph("ALMA Phil Manpower Services Corp. – Cebu City, Philippines | March 18, 2026 – Present (Project-Based Contract)", ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8.5, textColor=colors.HexColor('#475569'))))
    
    job1_details = [
        "Design, develop, and maintain full stack web applications based on client requirements.",
        "Develop and integrate REST APIs and backend services using Node.js, Java, and .NET.",
        "Build responsive frontend interfaces using Angular and modern web technologies.",
        "Perform debugging, troubleshooting, and performance optimization.",
        "Collaborate with project managers and technical teams in Agile environment.",
        "Participate in system enhancements, testing, and deployment activities.",
        "Ensure code quality, scalability, and security compliance."
    ]
    for detail in job1_details:
        story.append(Paragraph("• " + detail, body_style))
    story.append(Spacer(1, 0.08*inch))
    
    story.append(Paragraph("<b>Software Engineering / Packaged App Development Associate</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'))))
    story.append(Paragraph("Accenture Inc. – Ebloc 2, Cebu IT Park, Cebu City, Philippines | February 27, 2023 – March 18, 2026", ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8.5, textColor=colors.HexColor('#475569'))))
    
    job2_details = [
        "Developed and supported enterprise-level software applications.",
        "Worked on packaged application development and system enhancements.",
        "Participated in software testing, debugging, and production support.",
        "Collaborated with global teams in Agile delivery environment.",
        "Delivered system fixes and enhancements within SLA timelines.",
        "Supported API integrations and backend services using Java, .NET, and Node.js."
    ]
    for detail in job2_details:
        story.append(Paragraph("• " + detail, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Education
    story.append(Paragraph("EDUCATION", heading_style))
    story.append(Paragraph("<b>Bachelor of Science in Computer Engineering</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold')))
    story.append(Paragraph("University of Cebu – Main Campus, Sanciangko St., Cebu City | 2017 – 2018", body_style))
    story.append(Paragraph("<b>Arcelo Memorial National High School</b> • San Vicente, Liloan, Cebu", body_style))
    story.append(Paragraph("<b>Simeon Ayuda Elementary School</b> • San Vicente, Liloan, Cebu", body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Projects & Achievements
    story.append(Paragraph("PROJECTS & ACHIEVEMENTS", heading_style))
    story.append(Paragraph("<b>GEN AI Mini-Hackathon Winner</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, fontName='Helvetica-Bold')))
    story.append(Paragraph("Team project, 2025", body_style))
    achievements = [
        "Built a conversational AI agent for structured change request intake.",
        "Collected resources, schedule, environment, and requirement details.",
        "Generated submission-ready structured summaries."
    ]
    for achievement in achievements:
        story.append(Paragraph("• " + achievement, body_style))
    
    doc.build(story)
    print("✅ Australian format PDF saved: Rolyn_Kiunisala_CV.pdf")

# Professional Format PDF
def create_professional_pdf():
    filename = 'Rolyn_Kiunisala_Professional_CV.pdf'
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=0.75*inch, leftMargin=0.75*inch,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=10.5,
        textColor=colors.HexColor('#475569'),
        spaceAfter=10,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=10.5,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=8,
        spaceBefore=6,
        fontName='Helvetica-Bold',
        borderPadding=2,
        borderColor=colors.HexColor('#e2e8f0'),
        borderWidth=0.5,
        borderBottom=1
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5,
        alignment=TA_JUSTIFY,
        leading=11
    )
    
    # Header
    story.append(Paragraph("ROLYN KIUNISALA", title_style))
    story.append(Paragraph("Full Stack Software Developer", subtitle_style))
    story.append(Paragraph("Cebu, Philippines | rolynkiunisala@gmail.com | +63 906 454 4620 | LinkedIn: linkedin.com/in/rolyn-kiunisala-b862ab377", body_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Summary
    story.append(Paragraph("SUMMARY", heading_style))
    story.append(Paragraph("Full Stack Software Developer with over 3 years of experience in designing, developing, and maintaining enterprise and web-based applications. Skilled in backend and frontend development, API integration, and system enhancement within Agile environments. Experienced in delivering client-based solutions, automation initiatives, and cloud-based deployments. Strong ability to adapt quickly to new technologies and contribute to scalable software systems.", body_style))
    story.append(Spacer(1, 0.08*inch))
    
    # Skills
    story.append(Paragraph("SKILLS", heading_style))
    skills = [
        "<b>Programming Languages:</b> Java, JavaScript, C#, Python, PHP",
        "<b>Frontend:</b> HTML, CSS/SCSS, JavaScript, Angular, React (basic)",
        "<b>Backend:</b> Node.js, .NET, Java, Python",
        "<b>Database:</b> MySQL, SQL",
        "<b>Cloud & DevOps:</b> AWS, Azure DevOps, CI/CD, Lambda",
        "<b>Tools:</b> Git, GitHub, VS Code, Visual Studio, GitHub Copilot",
        "<b>Methodologies:</b> Agile / Scrum",
        "<b>Other:</b> REST API Development, System Integration, Debugging, Deployment, Network Basics, SCM"
    ]
    for skill in skills:
        story.append(Paragraph("• " + skill, body_style))
    story.append(Spacer(1, 0.08*inch))
    
    # Experience
    story.append(Paragraph("EXPERIENCE", heading_style))
    story.append(Paragraph("<b>Full Stack Software Developer</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=9.5, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'))))
    story.append(Paragraph("ALMA Phil Manpower Services Corp. – Cebu City, Philippines | March 18, 2026 – Present (Project-Based Contract)", ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8.5, textColor=colors.HexColor('#475569'), spaceAfter=3)))
    
    job1_details = [
        "Design, develop, and maintain full stack web applications based on client requirements.",
        "Develop and integrate REST APIs and backend services using Node.js, Java, and .NET.",
        "Build responsive frontend interfaces using Angular and modern web technologies.",
        "Perform debugging, troubleshooting, and performance optimization.",
        "Collaborate with project managers and technical teams in Agile environment.",
        "Participate in system enhancements, testing, and deployment activities.",
        "Ensure code quality, scalability, and security compliance."
    ]
    for detail in job1_details:
        story.append(Paragraph("• " + detail, body_style))
    story.append(Spacer(1, 0.06*inch))
    
    story.append(Paragraph("<b>Software Engineering / Packaged App Development Associate</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=9.5, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'))))
    story.append(Paragraph("Accenture Inc. – Ebloc 2, Cebu IT Park, Cebu City, Philippines | February 27, 2023 – March 18, 2026", ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8.5, textColor=colors.HexColor('#475569'), spaceAfter=3)))
    
    job2_details = [
        "Developed and supported enterprise-level software applications.",
        "Worked on packaged application development and system enhancements.",
        "Participated in software testing, debugging, and production support.",
        "Collaborated with global teams in Agile delivery environment.",
        "Delivered system fixes and enhancements within SLA timelines.",
        "Supported API integrations and backend services using Java, .NET, and Node.js."
    ]
    for detail in job2_details:
        story.append(Paragraph("• " + detail, body_style))
    story.append(Spacer(1, 0.08*inch))
    
    # Education
    story.append(Paragraph("EDUCATION", heading_style))
    story.append(Paragraph("<b>Bachelor of Science in Computer Engineering</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=9.5, fontName='Helvetica-Bold')))
    story.append(Paragraph("University of Cebu – Main Campus, Sanciangko St., Cebu City | 2017 – 2018", body_style))
    story.append(Paragraph("<b>Arcelo Memorial National High School</b> • San Vicente, Liloan, Cebu", body_style))
    story.append(Paragraph("<b>Simeon Ayuda Elementary School</b> • San Vicente, Liloan, Cebu", body_style))
    story.append(Spacer(1, 0.08*inch))
    
    # Projects & Achievements
    story.append(Paragraph("PROJECTS & ACHIEVEMENTS", heading_style))
    story.append(Paragraph("<b>GEN AI Mini-Hackathon Winner</b>", ParagraphStyle('Bold', parent=styles['Normal'], fontSize=9.5, fontName='Helvetica-Bold')))
    story.append(Paragraph("Team project, 2025", body_style))
    achievements = [
        "Built a conversational AI agent for structured change request intake.",
        "Collected resources, schedule, environment, and requirement details.",
        "Generated submission-ready structured summaries."
    ]
    for achievement in achievements:
        story.append(Paragraph("• " + achievement, body_style))
    
    doc.build(story)
    print("✅ Professional format PDF saved: Rolyn_Kiunisala_Professional_CV.pdf")

if __name__ == "__main__":
    create_australian_pdf()
    create_professional_pdf()
    print("\n✅ Both PDF documents have been successfully created!")
