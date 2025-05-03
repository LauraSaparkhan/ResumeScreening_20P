import streamlit as st
from matcher import (
    extract_text,
    preprocess_text,
    compare_keyword_match,
    compare_entity_match,
    compare_experience,
    compare_semantic_similarity
)

# --- Streamlit UI Setup ---
st.title("Resume vs Job Description Matcher")
st.markdown("Upload a **Resume** and a **Job Description** (TXT, DOCX, or PDF).")

# File upload widgets for resume and job description
resume_file = st.file_uploader("Upload Resume", type=["txt", "pdf", "docx"])
job_file = st.file_uploader("Upload Job Description", type=["txt", "pdf", "docx"])

if resume_file and job_file:
    # Extract text from the uploaded files
    resume_text = extract_text(resume_file)
    job_text = extract_text(job_file)

    # --- Keyword Match --- 
    common_keywords, keyword_match_score = compare_keyword_match(resume_text, job_text)

    # --- Named Entity Match ---
    matching_entities, entity_match_score = compare_entity_match(resume_text, job_text)

    # --- Experience Comparison ---
    resume_years, job_required_years = compare_experience(resume_text, job_text)
    # Determine if experience meets the job requirement
    experience_result = "Meets or exceeds requirement" if resume_years >= job_required_years else "Below required"

    # --- BERT Semantic Similarity ---
    semantic_score = compare_semantic_similarity(resume_text, job_text)

    # --- Display Results ---
    st.subheader("Results")
    st.write(f"**Keyword Match Score:** {keyword_match_score:.2f}%")
    st.write(f"**Common Keywords:** {', '.join(sorted(common_keywords)) if common_keywords else 'None'}")

    st.write(f"**Named Entity Match Score:** {entity_match_score:.2f}%")
    st.write(f"**Matching Entities:** {', '.join(sorted(matching_entities)) if matching_entities else 'None'}")

    st.write(f"**Experience in Resume:** {resume_years} years")
    st.write(f"**Required Experience:** {job_required_years} years")
    st.write(f"**Experience Match:** {experience_result}")

    st.write(f"**Semantic Similarity (BERT):** {semantic_score:.2f}")

else:
    # Prompt to upload both files if not done yet
    st.info("Please upload both a resume and a job description to begin.")
