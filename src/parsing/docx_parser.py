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
    # Check if file exists
    if not os.path.isfile(docx_path):
        raise FileNotFoundError(f"The file {docx_path} does not exist.")
    
    # Open the document
    doc = docx.Document(docx_path)
    
    # Get all tables
    tables = doc.tables
    
    print(f"Found {len(tables)} tables in the document.")
    
    # Convert each table to a NumPy array
    numpy_tables = []
    
    for i, table in enumerate(tables):
        # Get the number of rows and columns
        rows = len(table.rows)
        cols = len(table.columns)
        
        # Create an empty 2D list to store table data
        table_data = []
        
        # Extract text from each cell
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                # Get text from cell
                cell_text = cell.text.strip()
                row_data.append(cell_text)
            table_data.append(row_data)
        
        # Convert to NumPy array
        table_array = np.array(table_data)
        
        print(f"Table {i+1} shape: {table_array.shape}")
        numpy_tables.append(table_array)
    
    return numpy_tables
