import spacy
import fitz  # PyMuPDF
import docx
import re
from sentence_transformers import SentenceTransformer, util

# Here loading both spacy and BERT model one by one
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text(file):
    """Extracting raw text from file types: txt, pdf, docx"""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join(page.get_text() for page in pdf)
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)
    else:
        return ""


def preprocess_text(text):
    doc = nlp(text) # Process text, removing stop words and punctuation
    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            tokens.append(token.lemma_.lower()) # Lemmatization and lowercasing words
    return tokens # Return the list of lemmatized tokens

def extract_entities(text):
    doc = nlp(text)  # Process the text with SpaCy
    
    entities = []  # Create an empty list to store the results

    for ent in doc.ents:  # Loop through each named entity in the document
        # Check if the entity is one of the types that would appear in resume
        if ent.label_ in ("ORG", "PRODUCT", "SKILL", "GPE", "PERSON"):
            entities.append(ent.text.lower())  # Add the entity to the list in lowercase

    return entities  # Return the list of extracted entities

def extract_experience_years(text):
    """Extract the number of years of experience from the text."""
    # Convert the text to lowercase so we can handle different cases like "Years" or "years"
    text = text.lower()

    # Defining a pattern to find the years of experience in text.
    # The pattern looks for numbers followed by 'years', 'yrs', 'experience', 'exp'
    pattern = r'(\d+)\s*(?:years|yrs|experience|exp)'

    # Using re.findall to find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # If we found any matches, convert them to integers
    if matches:
        years = [int(match) for match in matches]
        # Return the largest number found (in case there are multiple numbers in the text)
        return max(years)
    else:
        # If no experience is found, return 0
        return 0

def compare_keyword_match(resume_text, job_text):
    """Compare keyword match score"""
    # Get list of tokens for both resume and job description
    resume_tokens = set(preprocess_text(resume_text)) 
    job_tokens = set(preprocess_text(job_text)) 
    # Get common words between lists and divide it by the number of tokens to find out the percentage
    common_keywords = resume_tokens & job_tokens
    keyword_match_score = len(common_keywords) / len(job_tokens) * 100 if job_tokens else 0
    return common_keywords, keyword_match_score


def compare_entity_match(resume_text, job_text):
    """Compare named entity match score"""
    # Get list of entities for both resume and job description
    resume_entities = set(extract_entities(resume_text))
    job_entities = set(extract_entities(job_text))

    # Get common entities and divide it by the sum of entities in job description
    matching_entities = resume_entities & job_entities
    entity_match_score = len(matching_entities) / len(job_entities) * 100 if job_entities else 0
    return matching_entities, entity_match_score
