from pdfminer.high_level import extract_text
from docx import Document
import re

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    """Extracts text from a DOCX file."""
    doc = Document(docx_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def parse_text(text):
    """Parses the extracted text to find specific information."""
    # Example: finding email addresses
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    # You can add more patterns here to find phone numbers, skills, etc.
    return {
        "emails": emails,
        # extract email from resume
    }

def parse_resume(file_path):
    # Determines the file type and extracts information from the resume.
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"
    
    info = parse_text(text)
    return info

file_path = 'path_to_your_resume' # example file path C:/Users/Resume.pdf
parsed_info = parse_resume(file_path)
print(parsed_info)
