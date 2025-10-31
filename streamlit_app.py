import streamlit as st
from agents import CVParserAgent, DataCollectionAgent, JDAnalysisAgent, ResumeContentAgent, CoverLetterAgent, FormattingAgent

# Page title
st.set_page_config(page_title='AI Resume and Cover Letter Generator', page_icon='🤖')
st.title('🤖 AI Resume and Cover Letter Generator')

st.write("Welcome to the AI-powered Resume and Cover Letter Generator! Fill in your details below to get started.")

# Add a text input for the Gemini API key
gemini_api_key = st.text_input("Enter your Gemini API Key", type="password")

# CV Uploader
st.header("Upload your CV")
uploaded_file = st.file_uploader("Choose a file (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file is not None and "cv_data" not in st.session_state:
    with st.spinner("Parsing your CV..."):
        cv_parser = CVParserAgent()
        st.session_state.cv_data = cv_parser.parse_cv(uploaded_file, gemini_api_key)

# User Inputs
st.header("Your Information")
name = st.text_input("Full Name", value=st.session_state.get("cv_data", {}).get("full_name", ""))
contact_info = st.text_area("Contact Information (Email, Phone, Address)", value=st.session_state.get("cv_data", {}).get("contact_info", ""))
linkedin_profile = st.text_input("LinkedIn Profile URL", value=st.session_state.get("cv_data", {}).get("linkedin_profile", ""))

st.header("Professional Experience")
experience = st.text_area("Describe your professional experience. Separate each role with a blank line.", value=st.session_state.get("cv_data", {}).get("experience", ""))

st.header("Skills")
skills = st.text_area("List your skills, separated by commas.", value=st.session_state.get("cv_data", {}).get("skills", ""))

st.header("Education")
education = st.text_area("Describe your educational background.", value=st.session_state.get("cv_data", {}).get("education", ""))

st.header("Target Job")
job_title = st.text_input("Job Title")
job_description = st.text_area("Paste the Job Description here.")

# Generate Button
if st.button("Generate Resume and Cover Letter"):
    if name and contact_info and experience and skills and education and job_title and job_description:
        st.success("Generating your tailored resume and cover letter...")

        # 1. Data Collection
        data_collection_agent = DataCollectionAgent()
        user_data = data_collection_agent.collect_data(name, contact_info, linkedin_profile, experience, skills, education)

        # 2. JD Analysis
        jd_analysis_agent = JDAnalysisAgent()
        jd_analysis = jd_analysis_agent.analyze(job_description)

        # 3. Content Generation
        resume_content_agent = ResumeContentAgent()
        resume_content = resume_content_agent.generate(user_data, jd_analysis, gemini_api_key)

        cover_letter_agent = CoverLetterAgent()
        cover_letter_content = cover_letter_agent.generate(user_data, jd_analysis, job_title, gemini_api_key)

        # 4. Formatting
        formatting_agent = FormattingAgent()

        st.header("Generated Resume")
        st.text(resume_content)

        st.header("Generated Cover Letter")
        st.text(cover_letter_content)

        # Export buttons
        formatting_agent.to_pdf(resume_content, "resume.pdf")
        formatting_agent.to_docx(resume_content, "resume.docx")
        formatting_agent.to_pdf(cover_letter_content, "cover_letter.pdf")
        formatting_agent.to_docx(cover_letter_content, "cover_letter.docx")

        with open("resume.pdf", "rb") as f:
            st.download_button("Download Resume as PDF", f, "resume.pdf")
        with open("resume.docx", "rb") as f:
            st.download_button("Download Resume as DOCX", f, "resume.docx")
        with open("cover_letter.pdf", "rb") as f:
            st.download_button("Download Cover Letter as PDF", f, "cover_letter.pdf")
        with open("cover_letter.docx", "rb") as f:
            st.download_button("Download Cover Letter as DOCX", f, "cover_letter.docx")
    else:
        st.error("Please fill in all the required fields.")
