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

