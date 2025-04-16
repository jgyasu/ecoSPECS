from src.generation.gen_model import gen_response
from src.generation.gen_document import gen_document
from src.generation.gen_few_shot_prompt import few_shot_prompt

from src.parsing.docx_parser import extract_tables_from_docx
from src.parsing.pdf_parser import extract_tables_from_pdf

from src.utility.header import header

from termcolor import colored

def main():
    print(colored(header, "yellow"))
    print(colored("\nTable Generator and Parser.\n", "yellow"))
    
    print("Please choose an option:\n")
    print(f"{colored('[1]', 'blue')} Generate a document containing a short introduction and table using a prompt")
    print(f"{colored('[2]', 'blue')} Extract tables from a file (pdf and docx supported)")
    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        print("\nPlease enter your prompt:", end="")
        user_prompt = input()
        print("\nPlease enter the filename (e.g. name.docx):", end="")
        filename = input()
        headers = {
            "columns": ["Brand", "Engine", "Price"],
        }
        prompt = few_shot_prompt(user_prompt, headers)
        response = gen_response(prompt)
        gen_document(response, filename=filename)
    
    elif choice == "2":
        print("\nPlease enter the file path:", end="")
        file_path = input()
        file_type = file_path.split('.')[-1]
        
        if file_type == "pdf":
            tables = extract_tables_from_pdf(file_path)
        elif file_type == "docx":
            tables = extract_tables_from_docx(file_path)
        else:
            print("\nUnsupported file type. Please provide a pdf or docx file.")
            return
        
        for i, table in enumerate(tables):
            print(f"Table {i+1}:")
            print(table)

    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        return



if __name__ == "__main__":
    main()