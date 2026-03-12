# from groq import Groq
# import os
# from dotenv import load_dotenv

# # Load environment variables from the .env file in the current directory
# load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def generate_feedback(resume, job=""):
    
#     if not job:
#         prompt = f"""
#         Analyze this resume comprehensively without a specific job description.

#         Resume:
#         {resume}

#         Please provide your response in valid JSON format ONLY, like this:
#         {{
#             "score": <a number from 0 to 100 representing overall resume quality and ATS readiness>,
#             "feedback": "<your detailed markdown feedback structured with Headers and Subheaders. Include sections like: 1. Formatting & Clarity, 2. Suggested Roles, 3. ATS Optimization Tips>"
#         }}
#         """
#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[{"role":"user","content":prompt}],
#             response_format={"type": "json_object"}
#         )
#         import json
#         try:
#             result = json.loads(response.choices[0].message.content)
#             return result.get("feedback", "No feedback provided."), result.get("score", 0)
#         except Exception:
#             return response.choices[0].message.content, 75 # Fallback
#     else:
#         prompt = f"""
#         Compare this resume with the job description.

#         Resume:
#         {resume}

#         Job Description:
#         {job}

#         Please provide a highly structured evaluation using Markdown headers (Topics and Subtopics). Include these specific sections:
        
#         ### 📌 Missing Keywords
#         List the important skills or keywords present in the Job Description but missing in the resume.
        
#         ### 💡 AI Suggestions & Improvements
#         Actionable tips to improve the resume for this specific role and boost ATS readability.
        
#         ### 📝 Formatting & Clarity
#         Suggestions on the resume's structure, impact, and overall presentation.
#         """

#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[{"role":"user","content":prompt}]
#         )

#         return response.choices[0].message.content
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from the .env file if it exists
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Prioritize Streamlit secrets for cloud deployment, fallback to environment variables
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def generate_feedback(resume, job=""):
    if not client:
        return "GROQ_API_KEY not found. Please check your environment variables or Streamlit secrets.", 0
    
    if not job:
        prompt = f"""
        Analyze this resume comprehensively without a specific job description.

        Resume:
        {resume}

        Please provide your response in valid JSON format ONLY, like this:
        {{
            "score": <a number from 0 to 100 representing overall resume quality and ATS readiness>,
            "feedback": "<your detailed markdown feedback. Include these specific sections:
            ### 💡 AI Suggestions & Improvements
            List actionable tips to improve content.
            
            ### 🚀 ATS Optimization Tips
            Suggestions to boost ATS readability.
            
            ### 📌 Potential Missing Keywords
            Keywords that are usually expected for roles matching this resume.>"
        }}
        """
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role":"user","content":prompt}],
                response_format={"type": "json_object"}
            )
            import json
            result = json.loads(response.choices[0].message.content)
            return result.get("feedback", "No feedback provided."), result.get("score", 0)
        except Exception as e:
            return f"Error generating feedback: {str(e)}", 0
    else:
        prompt = f"""
        Compare this resume with the job description.

        Resume:
        {resume}

        Job Description:
        {job}

        Please provide your response in valid JSON format ONLY, like this:
        {{
            "score": <a number from 0 to 100 representing the match percentage based on skills and experience>,
            "feedback": "<your detailed markdown feedback. Include these specific sections:
            ### 📌 Missing Keywords
            List the important skills or keywords present in the Job Description but missing in the resume.
            
            ### 💡 AI Suggestions & Improvements
            Actionable tips to improve the resume for this specific role.
            
            ### 📝 Formatting & Clarity
            Suggestions on structure and presentation.>"
        }}
        """
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role":"user","content":prompt}],
                response_format={"type": "json_object"}
            )
            import json
            result = json.loads(response.choices[0].message.content)
            return result.get("feedback", "No feedback provided."), result.get("score", 0)
        except Exception as e:
            return f"Error comparing resume to job description: {str(e)}", 0
        
