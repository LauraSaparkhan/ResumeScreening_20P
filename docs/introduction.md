# 📄 Resume Matcher – Final Documentation

## 📌 Overview

This project compares a candidate’s resume to a job description using natural language processing (NLP) techniques. It outputs match scores for keywords, named entities, years of experience, and semantic similarity using SpaCy and Sentence-BERT.

---

## ⚙️ Features

- ✅ Extracts text from `.txt`, `.pdf`, and `.docx` files  
- ✅ Cleans and lemmatizes text using SpaCy  
- ✅ Identifies and compares named entities  
- ✅ Extracts years of experience  
- ✅ Computes keyword match score  
- ✅ Computes semantic similarity using BERT  

---

## 🧠 Technologies Used

- `spaCy` (for NLP and NER)
- `SentenceTransformers` (BERT-based semantic similarity)
- `PyMuPDF` (`fitz`, for PDF parsing)
- `python-docx` (for reading DOCX files)
- `re` (for regex pattern matching)

---

## 📁 File Descriptions

| Function | Purpose |
|----------|---------|
| `extract_text(file)` | Reads and extracts text from `.txt`, `.pdf`, or `.docx` |
| `preprocess_text(text)` | Lemmatizes and cleans the text using SpaCy |
| `extract_entities(text)` | Extracts named entities like skills, organizations, etc. |
| `extract_experience_years(text)` | Finds years of experience mentioned in the text |
| `compare_keyword_match(resume, job)` | Calculates keyword overlap score |
| `compare_entity_match(resume, job)` | Calculates named entity overlap score |
| `compare_experience(resume, job)` | Extracts and compares experience in years |
| `compare_semantic_similarity(resume, job)` | Measures semantic similarity using BERT |

---

## 🔍 Function Summaries

### `extract_text(file)`
Extracts plain text from `.txt`, `.pdf`, and `.docx`. Uses `fitz` for PDFs and `docx` for Word files.

---

### `preprocess_text(text)`
- Removes stopwords and punctuation
- Lemmatizes tokens (e.g., “working” → “work”)

---

### `extract_entities(text)`
Detects named entities from text using SpaCy.  
Extracts entities of type:
- `ORG` (organizations)
- `PRODUCT`
- `SKILL` (custom)
- `GPE` (geopolitical locations)
- `PERSON`

---

### `extract_experience_years(text)`
Uses regex to search for experience patterns (e.g., “5 years of experience”).

---

### `compare_keyword_match(resume_text, job_text)`
- Tokenizes and lemmatizes both inputs
- Calculates percentage of shared keywords

---

### `compare_entity_match(resume_text, job_text)`
- Extracts named entities from both inputs
- Calculates percentage of matching entities

---

### `compare_experience(resume_text, job_text)`
- Extracts numerical experience values
- Compares resume and job requirements

---

### `compare_semantic_similarity(resume_text, job_text)`
- Encodes both texts using BERT
- Returns cosine similarity score (0 to 1)

---

## 📈 Sample Output

```python
common_keywords, keyword_score = compare_keyword_match(resume, job)
entities, entity_score = compare_entity_match(resume, job)
resume_years, job_years = compare_experience(resume, job)
similarity = compare_semantic_similarity(resume, job)
