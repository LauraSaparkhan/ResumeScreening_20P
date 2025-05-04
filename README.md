# Resume Screening Tool
## Introduction
This project is Python-based resume screening tool for both job applicants and employers that allows users to compare a resume to job description.
## Problem Statement
It's not always easy for recruiters and job seekers to figure out if a resume is a good for a job description. This process is usually done manually, which takes a lot of time, and there's always the chance of human bias. Our smart matching tool handles this comparison using natural language processing (NLP) and machine learning techniques to analyze both resumes and job descriptions. It provides metrics—like keyword overlap, entity recognition, experience comparison, and semantic similarity—to deliver a compatibility score. Our solution makes the evaluation process faster and more accurate, which helps make better hiring decisions. 
## Objectives
- To help users measure the relevance of a resume for a job description.
- To extract and compare key information such as keywords, named entities, and experience.
- To compute a semantic similarity score using transformer models.
- To present results in an easy-to-understand web interface.
## Technology Stack
- Frontend: Streamlit
- Backend: Python
- Libraries: SpaCy, SentenceTransformers, PyMuPDF, python-docx, re
- NLP Models: en_core_web_sm, all-MiniLM-L6-v2
## Installation Instructions
1. Clone the repository
```bash
git clone https://github.com/LauraSaparkhan/ResumeScreening_20P.git
```
2. Navigate into the project directory
```bash
cd ResumeScreening_20P
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Start the application
```bash
streamlit run app.py
```
## Usage Guide
## Testing
## References
## Team Members



https://resume-screening-20p.streamlit.app/
