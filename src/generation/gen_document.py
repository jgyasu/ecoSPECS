import markdown
from docx import Document
import pandas as pd
from io import StringIO
import re
import os

def gen_document(response, filename):
    """Generate a Word document from the LLM generated response."""

    output_dir="output/"

    lines = response.strip().splitlines()
    table_start = next((i for i, line in enumerate(lines) if re.match(r"^\s*\|.*\|\s*$", line)), None)

    if table_start is None:
        raise ValueError("No markdown table found in the response.")

    intro = "\n".join(lines[:table_start]).strip()
    table_md = "\n".join(lines[table_start:]).strip()

    df = pd.read_csv(StringIO(table_md), sep="|", skipinitialspace=True)
    df = df.drop(df.columns[[0, -1]], axis=1)

    doc = Document()

    if intro:
        doc.add_paragraph(intro)

    table = doc.add_table(rows=1, cols=len(df.columns))

    hdr_cells = table.rows[0].cells
    for i, col_name in enumerate(df.columns):
        hdr_cells[i].text = col_name.strip()

    for _, row in df.iterrows():
        row_cells = table.add_row().cells
        for i, val in enumerate(row):
            row_cells[i].text = str(val).strip()

    os.makedirs(output_dir, exist_ok=True)
    doc.save(os.path.join(output_dir, filename))
