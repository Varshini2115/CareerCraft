
# CareerCraft: ATS-Optimized Resume Analyzer

## Project Overview

### Objective:
CareerCraft helps job seekers improve their resumes by providing an analysis that compares resumes to job descriptions, identifying areas for optimization for ATS (Applicant Tracking Systems). The tool increases the chances of a resume passing through ATS filters, leading to more interview opportunities.

### Description:
Using Google Gemini (Bard) API and advanced ATS algorithms, CareerCraft evaluates resumes against job descriptions by analyzing keywords, skills, and relevant content. It then offers users a matching percentage and recommendations to enhance their applications for better ATS compliance.

---

## Project Plan

### Milestones:
- Initial setup and API integration
- Resume parsing and text extraction from PDFs
- ATS matching and feedback algorithm development
- Streamlit UI design
- Testing, debugging, and optimization
- Final documentation and deployment


### Activities:
- Text extraction from PDFs
- Integration with Google Gemini API
- Resume-to-job-description matching and feedback
- User interface creation using Streamlit

---

## Technical Specifications

### Technology Stack:
- **Programming Language**: Python
- **Framework**: Streamlit
- **APIs**: Google Gemini (Bard API)
- **Libraries**:
  - `PyPDF2`: Extract text from PDF resumes
  - `Pillow`: Handle and display images
  - `dotenv`: Manage environment variables
  - `google.generativeai`: Interact with Google Gemini API

### System Architecture:
- **Client-Side**: Streamlit-based UI for user interaction
- **Server-Side**: Backend handling PDF text extraction and Google Gemini API calls for resume analysis

### API Documentation:
- **Google Gemini API**: Processes resume text, matches keywords, and provides feedback based on job descriptions.

---

## Code Overview

### File Structure:
```
├── app.py               # Main application script
├── images/              # Image assets
├── .env                 # Environment variables (API keys)
├── README.md            # Project documentation
└── requirements.txt     # List of dependencies
```

### Key Modules:
- `app.py`: Main application logic including the UI, API calls, and PDF text extraction.
- `images/`: Stores any image assets for the application.

### Important Functions:
- `input_pdf_text(uploaded_file)`: Extracts and processes the text from PDF resumes.
- `get_gemini_response(input)`: Sends resume data to Google Gemini API for analysis and retrieves results.

---

## Setup Instructions

### Clone the Repository:
```bash
git clone https://github.com/Varshini2115/CareerCraft.git
cd CareerCraft
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:
Create a `.env` file with your Google Gemini API key:
```
GOOGLE_API_KEY=your_google_api_key
```

### Run the Application:
```bash
streamlit run app.py
```

---

## Testing and Validation

### Testing Strategy:
- **Unit Testing**: Test PDF text extraction functionality using different resume formats.
- **Integration Testing**: Validate that the ATS analysis provides accurate feedback based on job descriptions.

### Test Cases:
- Upload various resumes and ensure missing keywords are highlighted correctly.
- Test against different job descriptions for matching accuracy.

---

## Challenges and Solutions

### Challenges:
- **Text Extraction from PDFs**: 
  - **Solution**: Used `PyPDF2` for reliable text extraction.
  
- **Accurate ATS Feedback**: 
  - **Solution**: Refined Google Gemini API prompts to focus on identifying important keywords and skills.

---

## Future Enhancements

- Add support for `.docx` resumes.
- Multi-language resume analysis.
- Enhanced feedback visualizations for ATS matching scores.

---

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Documentation](https://cloud.google.com/ai/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/latest/)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)

---

## GitHub Repository

Repository Link: [CareerCraft GitHub Repository](https://github.com/Varshini2115/CareerCraft)

---

