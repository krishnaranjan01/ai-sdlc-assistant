from pathlib import Path

from src.tools.document_parser import extract_text


TEST_DATA_DIR = Path(__file__).parent / "test_data"


def test_txt_file_extraction():
    file_path = TEST_DATA_DIR / "sample_requirement.txt"

    result = extract_text(str(file_path))

    assert "AI SDLC Assistant Requirement" in result
    assert "functional requirements" in result
    assert "PDF, DOCX, and TXT" in result


def test_docx_file_extraction():
    file_path = TEST_DATA_DIR / "sample_requirement.docx"

    result = extract_text(str(file_path))

    assert "AI SDLC Assistant Requirement" in result
    assert "functional requirements" in result
    assert "PDF, DOCX, and TXT" in result


def test_pdf_file_extraction():
    file_path = TEST_DATA_DIR / "sample_requirement.pdf"

    result = extract_text(str(file_path))

    assert "AI SDLC Assistant Requirement" in result
    assert "functional requirements" in result
    assert "PDF, DOCX, and TXT" in result
