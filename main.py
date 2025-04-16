from src.generation.gen_model import gen_response
# from src.generation.gen_document import gen_table
from src.generation.gen_few_shot_prompt import few_shot_prompt

from src.parsing.docx_parser import extract_tables_from_docx
from src.parsing.pdf_parser import extract_tables_from_pdf

def main():
    print("""Welcome to Table Generator and Parser.
          This my solution for ecoSPECS applied project at ESoC 2025.""")
    
    print("Please choose an option:")
    print("1. Generate a table using a prompt")
    print("2. Extract tables from a file (pdf and docx supported)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Please enter your prompt:")
        user_prompt = input()
        headers = {
            "columns": ["Brand", "Engine", "Price"],
        }
        prompt = few_shot_prompt(user_prompt, headers)
        response = gen_response(prompt)
        print(response)
    
    elif choice == "2":
        print("Please enter the file path:")
        file_path = input()
        file_type = file_path.split('.')[-1]
        
        if file_type == "pdf":
            tables = extract_tables_from_pdf(file_path)
        elif file_type == "docx":
            tables = extract_tables_from_docx(file_path)
        else:
            print("Unsupported file type. Please provide a pdf or docx file.")
            return
        
        for i, table in enumerate(tables):
            print(f"Table {i+1}:")
            print(table)


if __name__ == "__main__":
    main()