import pdfplumber
from docx import Document

def extract_text(file_path, file_type):
    if file_type == "pdf":
        with pdfplumber.open(file_path) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_type == "docx":
        doc = Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])
    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return ""
