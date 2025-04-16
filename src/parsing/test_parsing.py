import pytest
import numpy as np

from .pdf_parser import extract_tables_from_pdf
from .docx_parser import extract_tables_from_docx

def arrays_equal_ignore_dtype(a, b):
    """Check if two numpy arrays are equal, ignoring their data types."""

    return a.shape == b.shape and np.all(a.astype(str) == b.astype(str))

def test_extract_tables_from_pdf():
    """Test if extracted tables from PDF match expected output."""

    expected_output = [
        np.array([
            ['1', '2', '3', '4'],
            ['A', 'B', 'C', 'D'],
            ['5', '6', '7', '8']
        ], dtype=object),
        np.array([
            ['9', '10', '11', '12', '13'],
            ['Ef', 'Gh', 'Ij', 'Kl', 'Mn'],
            ['14', '15', '16', '17', '18'],
            ['19', '20', '21', '22', '23']
        ], dtype=object)
    ]

    result = extract_tables_from_pdf("../../data/test.pdf")

    assert len(result) == len(expected_output), "Number of tables doesn't match"

    for res_table, exp_table in zip(result, expected_output):
        assert arrays_equal_ignore_dtype(res_table, exp_table), \
            f"Mismatch in table:\nExpected:\n{exp_table}\nGot:\n{res_table}"
        
def test_extract_tables_from_docx():
    """Test if extracted tables from PDF match expected output."""

    expected_output = [
        np.array([
            ['1', '2', '3', '4'],
            ['A', 'B', 'C', 'D'],
            ['5', '6', '7', '8']
        ], dtype=object),
        np.array([
            ['9', '10', '11', '12', '13'],
            ['Ef', 'Gh', 'Ij', 'Kl', 'Mn'],
            ['14', '15', '16', '17', '18'],
            ['19', '20', '21', '22', '23']
        ], dtype=object)
    ]

    result = extract_tables_from_docx("../../data/test.docx")

    assert len(result) == len(expected_output), "Number of tables doesn't match"

    for res_table, exp_table in zip(result, expected_output):
        assert arrays_equal_ignore_dtype(res_table, exp_table), \
            f"Mismatch in table:\nExpected:\n{exp_table}\nGot:\n{res_table}"
