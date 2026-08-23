from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_file(file_path: str) -> None:
    """
    Validate that the uploaded file exists,
    has a supported extension and is <= 5 MB.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    allowed_extensions = {".pdf", ".docx", ".txt"}

    if path.suffix.lower() not in allowed_extensions:
        raise ValueError(
            "Unsupported file type. Only PDF, DOCX and TXT files are allowed."
        )

    if path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("File size cannot exceed 5 MB.")


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""

    document = fitz.open(file_path)

    text = []

    for page in document:
        text.append(page.get_text())

    document.close()

    return "\n".join(text).strip()


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""

    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text).strip()


def extract_text_from_txt(file_path: str) -> str:
    """Read text from a TXT file."""

    path = Path(file_path)

    return path.read_text(encoding="utf-8").strip()


def extract_text(file_path: str) -> str:
    """
    Validate the file and extract text based on its type.
    """

    validate_file(file_path)

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    if extension == ".txt":
        return extract_text_from_txt(file_path)

    raise ValueError("Unsupported file type.")
