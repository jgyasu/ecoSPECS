from docx import Document

def extract_tables_from_docx(file_path):
    """
    Extracts all tables from a .docx file and returns them
    as a list of 2D lists (each 2D list is a table).
    """
    document = Document(file_path)
    tables_data = []

    for table in document.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            table_data.append(row_data)
        tables_data.append(table_data)

    return tables_data

# Example usage
if __name__ == "__main__":
    file_path = "../generation/table.docx"  # Replace with your file path
    tables = extract_tables_from_docx(file_path)

    print(tables)
