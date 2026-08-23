from pathlib import Path

from src.tools.document_parser import (
    extract_text_from_txt,
)


def test_txt_file_extraction(tmp_path):
    """
    Test that a TXT file can be read successfully.
    """

    test_file = tmp_path / "requirement.txt"

    test_file.write_text(
        "Build a banking application that allows users to transfer money.",
        encoding="utf-8",
    )

    result = extract_text_from_txt(str(test_file))

    assert "banking application" in result
    assert "transfer money" in result
