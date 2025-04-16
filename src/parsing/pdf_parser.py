import numpy as np
import camelot
import os

def extract_tables_from_pdf(pdf_path):
    """
    Extract all tables from a PDF and store them as NumPy arrays.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        list: List of 2D NumPy arrays, each representing a table
    """
    # Check if file exists
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    
    # Extract tables using Camelot
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    
    print(f"Found {len(tables)} tables in the PDF.")
    
    # Convert each table to a NumPy array
    numpy_tables = []
    
    for i, table in enumerate(tables):
        # Get the DataFrame
        df = table.df
        
        # Convert DataFrame to NumPy array
        table_array = np.array(df.values)
        
        print(f"Table {i+1} shape: {table_array.shape}")
        numpy_tables.append(table_array)
    
    return numpy_tables
