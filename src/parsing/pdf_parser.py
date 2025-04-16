import numpy as np
import camelot
import os

def extract_tables_from_pdf(pdf_path):
    """Extract all tables from a PDF and store them as NumPy arrays."""

    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    

    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    
    numpy_tables = []
    
    for i, table in enumerate(tables):
        df = table.df
        
        table_array = np.array(df.values)

        numpy_tables.append(table_array)
    
    return numpy_tables
