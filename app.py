import streamlit as st
from utils import extract_text_from_pdf
from agent import analyze_resume

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Advanced AI Resume Screening Agent")
st.caption("Upload a resume and compare it with a job description using Groq AI.")

with st.sidebar:
    st.header("About Project")
    st.write("""
    This AI agent helps recruiters screen resumes by comparing candidate skills
    with a job description and generating a structured hiring analysis.
    """)

uploaded_resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)

if uploaded_resume and job_description:
    if st.button("Analyze Resume"):
        with st.spinner("Extracting resume text..."):
            resume_text = extract_text_from_pdf(uploaded_resume)

        if not resume_text:
            st.error("Could not extract text from this PDF.")
        else:
            with st.spinner("Analyzing resume with AI..."):
                result = analyze_resume(resume_text, job_description)

            st.subheader("AI Screening Result")
            st.markdown(result)
else:
    st.info("Upload a resume PDF and paste a job description to start.")
