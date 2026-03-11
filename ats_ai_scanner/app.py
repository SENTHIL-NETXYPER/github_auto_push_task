from modules.parser import parse_resume
from modules.cleaner import clean_text
from modules.semantic_matcher import semantic_match
from modules.scorer import calculate_score
from modules.ai_feedback import generate_feedback

resume_text = parse_resume("resumes/sample_resume.pdf")

clean_resume = clean_text(resume_text)

job_description = """
Python developer with Django REST API experience
"""

similarity = semantic_match(clean_resume, job_description)

score = calculate_score(similarity)

print("ATS Score:", score)

feedback = generate_feedback(clean_resume, job_description)

print("\nAI Suggestions:")
print(feedback)