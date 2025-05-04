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
1. Launch the web app using streamlit run app.py or simply access https://resume-screening-20p.streamlit.app/.

2. Upload a resume (PDF, DOCX, or TXT).

3. Upload a job description (PDF, DOCX, or TXT).

4. View comparison results:
- Keyword match score and common terms
- Named entity match score
- Years of experience comparison
- Semantic similarity score (via BERT)
## Testing
1. File Upload
- Upload TXT, DOCX, and PDF files.
- Ensure text is correctly extracted from each file type.
Unsupported file types should trigger an error.

2. Keyword Match
- Upload a Resume and Job Description with overlapping keywords.
- Verify the Keyword Match Score and Common Keywords list.

3. Entity Match
- Upload files with named entities (e.g., skills, organizations).
- Check the Entity Match Score and Extracted Entities.

4. Experience Comparison
- Upload a Resume and Job Description with experience data.
- Verify the Experience Match score for accurate year comparison.

5. Semantic Similarity
- Upload contextually similar Resume and Job Description.
- Check the Semantic Similarity Score (should range between 0 and 1).

6. Edge Cases
- Test with empty files, unsupported file types, and large files.
- Verify the app provides proper error messages or handles them gracefully.

7. Cross-Browser Compatibility
- Test the app on different browsers (e.g., Chrome, Firefox).
- Ensure consistent functionality and UI across browsers.
## References

- [SpaCy](https://spacy.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [spaCy Entity Types](https://spacy.io/api/annotation#named-entities)
- [VisualCV Resume Samples Attribution](docs/VisualCV_Attribution.md)

## Team Members
- Laura Saparkhan, 220103028, 20P
