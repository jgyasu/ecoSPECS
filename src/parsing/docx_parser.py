import numpy as np
import docx
import os

def extract_tables_from_docx(docx_path):
    """
    Extract all tables from a Word document and store them as NumPy arrays.
    
    Args:
        docx_path (str): Path to the .docx file
        
    Returns:
        list: List of 2D NumPy arrays, each representing a table
    """

    if not os.path.isfile(docx_path):
        raise FileNotFoundError(f"The file {docx_path} does not exist.")
    
    doc = docx.Document(docx_path)
    
    tables = doc.tables
    
    numpy_tables = []
    
    for i, table in enumerate(tables):

        rows = len(table.rows)
        cols = len(table.columns)
        
        table_data = []
        
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                cell_text = cell.text.strip()
                row_data.append(cell_text)
            table_data.append(row_data)
        
        table_array = np.array(table_data)
        
        numpy_tables.append(table_array)
    
    return numpy_tables
