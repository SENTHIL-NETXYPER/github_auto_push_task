import streamlit as st
import os
import tempfile
from modules.parser import parse_resume
from modules.cleaner import clean_text
from modules.semantic_matcher import semantic_match
from modules.scorer import calculate_score
from modules.ai_feedback import generate_feedback

def main():
    st.set_page_config(page_title="ATS AI Scanner", page_icon="📄", layout="wide")
    
    st.title("📄 ATS AI Resume Scanner")
    st.markdown("Upload your resume and a job description to see how well you match!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Upload Resume")
        uploaded_file = st.file_uploader("Upload your PDF resume", type=["pdf"])
        
    with col2:
        st.subheader("2. Job Description")
        job_description = st.text_area("Paste the Job Description here", height=200)

    if st.button("Analyze Resume", type="primary"):
        if uploaded_file is not None:
            with st.spinner("Analyzing..."):
                try:
                    # Save uploaded file to a temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_path = tmp_file.name

                    # Process the resume
                    resume_text = parse_resume(tmp_path)
                    clean_resume = clean_text(resume_text)
                    
                    if job_description:
                        # Calculate Match
                        similarity = semantic_match(clean_resume, job_description)
                        score = calculate_score(similarity)
                        st.subheader("ATS Score")
                        st.metric(label="Match Percentage", value=score)
                        feedback = generate_feedback(clean_resume, job_description)
                    else:
                        st.info("No Job Description provided. Performing general analysis...")
                        feedback = generate_feedback(clean_resume)
                    
                    # Clean up temp file
                    os.unlink(tmp_path)
                    
                    # Display Results
                    st.success("Analysis Complete!")
                    
                    st.subheader("AI Feedback & Suggestions")
                    st.write(feedback)
                    
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
        else:
            st.warning("Please upload a resume.")

if __name__ == "__main__":
    main()
