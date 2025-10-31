import google.generativeai as genai
from docx import Document
from fpdf import FPDF
import re

class DataCollectionAgent:
    def collect_data(self, name, contact_info, linkedin_profile, experience, skills, education):
        """Gathers and structures the user's career data."""
        return {
            "name": name,
            "contact_info": contact_info,
            "linkedin_profile": linkedin_profile,
            "experience": experience,
            "skills": skills,
            "education": education
        }

class JDAnalysisAgent:
    def analyze(self, job_description):
        """Analyzes the job description to extract keywords and requirements."""
        # A more sophisticated approach would use NLP techniques like named entity recognition
        # and part-of-speech tagging to identify key skills and requirements.
        # For this implementation, we'll use a simple regex to extract potential keywords.
        keywords = re.findall(r'\b\w+\b', job_description.lower())
        return {
            "keywords": list(set(keywords)),
            "requirements": job_description
        }

class ResumeContentAgent:
    def generate(self, user_data, jd_analysis, api_key):
        """Generates tailored resume content based on the user's data and the job description analysis."""
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Based on the following user data and job description, generate a professional resume.

        **User Data:**
        - Name: {user_data['name']}
        - Contact Info: {user_data['contact_info']}
        - LinkedIn: {user_data['linkedin_profile']}
        - Experience: {user_data['experience']}
        - Skills: {user_data['skills']}
        - Education: {user_data['education']}

        **Job Description:**
        {jd_analysis['requirements']}

        **Instructions:**
        - The resume should be tailored to the job description, highlighting the most relevant skills and experience.
        - Use a professional and clear format.
        - Emphasize achievements and quantifiable results.
        """
        response = model.generate_content(prompt)
        return response.text

class CoverLetterAgent:
    def generate(self, user_data, jd_analysis, job_title, api_key):
        """Generates a tailored cover letter."""
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Based on the following user data and job description, generate a compelling cover letter.

        **User Data:**
        - Name: {user_data['name']}
        - Experience: {user_data['experience']}
        - Skills: {user_data['skills']}

        **Job Title:** {job_title}
        **Job Description:**
        {jd_analysis['requirements']}

        **Instructions:**
        - The cover letter should be addressed to the hiring manager (if not specified, use a generic greeting).
        - It should clearly articulate why the candidate is a good fit for the role, drawing direct connections between their experience and the job requirements.
        - Maintain a professional and enthusiastic tone.
        """
        response = model.generate_content(prompt)
        return response.text

class FormattingAgent:
    def to_pdf(self, text, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(filename)

    def to_docx(self, text, filename):
        document = Document()
        document.add_paragraph(text)
        document.save(filename)
