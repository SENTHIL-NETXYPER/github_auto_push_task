from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the current directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_feedback(resume, job):

    prompt = f"""
    Compare this resume with the job description.

    Resume:
    {resume}

    Job Description:
    {job}

    Suggest improvements for ATS optimization.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content