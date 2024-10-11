# Importing necessary libraries
import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from google.generativeai import GenerativeModel
from PIL import Image
import streamlit_vertical_space  # Custom module for vertical spacing (you might need to implement or install this)

# Load environment variables from the .env file
load_dotenv()

# Set up the Google API key from the .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the GenerativeAI module with the Google API key
GenerativeModel.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini Pro pre-trained model
model = GenerativeModel(model="gemini-pro")

# Function to get the response from Gemini Pro
def get_gemini_response(input_text):
    response = model.generate_content(input_text=input_text)
    return response

# Function to read and extract text from the uploaded PDF
def input_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Streamlit app layout
st.title("CareerCraft: ATS-Optimized Resume Analyzer")

# Upload resume
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
resume_text = ""
if resume_file is not None:
    resume_text = input_pdf_text(resume_file)
    st.subheader("Resume Content:")
    st.write(resume_text)

# Upload job description
job_file = st.file_uploader("Upload the job description (PDF)", type=["pdf"])
job_text = ""
if job_file is not None:
    job_text = input_pdf_text(job_file)
    st.subheader("Job Description Content:")
    st.write(job_text)

# Input prompt for the Gemini Pro model (for ATS)
input_prompt = """
You are tasked with building an ATS (Applicant Tracking System) optimized for analyzing resumes against job descriptions.
Expertise required includes: Software Engineering, Data Science, Full-Stack Development, Python, NLP, AI, and Machine Learning.
Structure your response into the following sections:
1. Percentage match with the job description.
2. List of missing keywords in the resume.
3. A profile summary based on the resume.
"""

# Button to trigger the analysis
if st.button("Analyze Resume"):
    if resume_text and job_text:
        st.success("Analyzing the resume against the job description...")

        # Send the job description and resume to the model for analysis
        gemini_response = get_gemini_response(input_prompt)

        # Display the analysis response
        st.subheader("Analysis Results:")
        st.write(gemini_response)
    else:
        st.error("Please upload both your resume and the job description for analysis.")

