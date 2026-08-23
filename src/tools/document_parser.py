from pathlib import Path
from pypdf import PdfReader


def extract_text(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    elif path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    else:
        raise ValueError("Currently supported: PDF and TXT")
