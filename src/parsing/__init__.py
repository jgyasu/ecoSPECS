from .docx_parser import extract_tables_from_docx
from .pdf_parser import extract_tables_from_pdf

__all__ = [extract_tables_from_pdf,
           extract_tables_from_docx]