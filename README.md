# ecoSPECS
Solution for the ecoSPECS challenge in ESoC 2025

## Features

Capable of generating tables using GenAI based on a given prompt, rows and columns can be specified too. The parsing module is capable of parsing a `pdf` or a `docx` file and extracts the table from it and stores them in a list of 2-D NumPy arrays.

- **Bonus 1**: Uses an open source open-weight LLM `Qwen/Qwen2.5-1.5B-Instruct` via Hugging Face transformers.

- **Bonus 2**: Uses few shot learning to generate a table from a user prompt without changing the generative model weights or architecture since language models are few-shot learners.


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
Once the setup and installation is done, simply execute the program by running:
```bash
python main.py
```

### Usage
