from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, job_description):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
You are an expert AI Resume Screening Agent.

Analyze the candidate resume against the given job description.

Give output in this exact format:

## Match Percentage
Give percentage out of 100.

## Candidate Summary
Short summary of candidate profile.

## Matched Skills
List skills from resume that match the job description.

## Missing Skills
List important skills missing from resume.

## Strengths
List candidate strengths.

## Weaknesses
List candidate weaknesses.

## Resume Improvement Suggestions
Give practical suggestions to improve resume.

## Final Recommendation
Choose one:
- Strong Match
- Good Match
- Average Match
- Not Suitable

Keep the answer professional and interview-ready.
"""
            },
            {
                "role": "user",
                "content": f"""
Resume:
{resume_text[:7000]}

Job Description:
{job_description[:4000]}
"""
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
