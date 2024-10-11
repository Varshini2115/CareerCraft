import streamlit as st
from PyPDF2 import PdfReader

# Function to read PDF content
def read_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

# Streamlit app layout
st.title("CareerCraft: ATS-Optimized Resume Analyzer")
st.markdown("Upload your resume and a job description to get started!")

# File uploader for resume
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
resume_text = ""
if resume_file is not None:
    resume_text = read_pdf(resume_file)
    st.subheader("Resume Content:")
    if resume_text:
        st.write(resume_text)
    else:
        st.error("Could not read the resume file. Please try again.")

# File uploader for job description
job_file = st.file_uploader("Upload the job description (PDF)", type=["pdf"])
job_text = ""
if job_file is not None:
    job_text = read_pdf(job_file)
    st.subheader("Job Description Content:")
    if job_text:
        st.write(job_text)
    else:
        st.error("Could not read the job description file. Please try again.")

# Button to analyze the resume and job description
if st.button("Analyze Resume"):
    if resume_text and job_text:
        # Placeholder for analysis logic (keyword matches, etc.)
        st.success("Analyzing the resume against the job description... (This feature is under development!)")
    else:
        st.error("Please upload both your resume and the job description to analyze.")
