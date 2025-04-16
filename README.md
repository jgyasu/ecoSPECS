# ecoSPECS
Solution for the ecoSPECS challenge in ESoC 2025

![image](https://github.com/user-attachments/assets/0ef28217-341d-4f88-a60a-e99117d92f8b)

## Features

Capable of generating tables using GenAI based on a given prompt, rows and columns can be specified too. The parsing module is capable of parsing a `pdf` or a `docx` file and extracts the table from it and stores them in a list of 2-D NumPy arrays. A testing infrastrucuture for the `parsing` module is also provided.

- **Bonus 1**: Uses an open source open-weight LLM `Qwen/Qwen2.5-1.5B-Instruct` via Hugging Face transformers.

- **Bonus 2**: Uses few shot learning to generate a table from a user prompt without changing the generative model weights or architecture since language models are few-shot learners without any rows and columns specified.


- **Bonus 3**: Writes a short introduction paragraph and the generated table to `doc` or `pdf` based on the preference.

For installation and usage, see the following sections.

## Installation

For installation, first clone the repository:
```bash
git clone https://github.com/jgyasu/ecoSPECS.git
cd ecoSPECS
```

It is a good practice to work in a virtual environment. To create a new one, run:
```bash
conda create -n ecospecs python=3.11 #creates a conda environment
conda activate ecospecs #activates the environment
```
Then install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Usage

To start the CLI program, simply run:
```bash
python main.py
```

The program will ask you to choose an option from the following options:

1. Generate a document containing a short introduction and table using a prompt
2. Extract tables from a file (pdf and docx supported)

Ouput documents with the generated tables will be saved in the `output` directory.

Example: The `output` directory contains a generated document from the prompt I tried: `Create a table comparing cars`.

## Testing

The tests for the parsing module can be run using `pytest` in the `src/parsing` directory by running:
```bash
pytest test_parsing.py
```

The tasks for ESoC didn't include writing tests for the generation module, but since they do LLM calls, mocking them in the future would be the optimal choice.

## Note

This is a prototype and a possible subset of a functional end-to-end application. There are challenged that I am aware of which needs to be solved when deploying to production.
