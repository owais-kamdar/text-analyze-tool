# aipi510_preassignment_kamdar
preassignment aipi510
# Text Analyzer Tool

The Text Analyzer Tool is a command-line utility that analyzes text files by counting word occurrences, identifying the most common words, and providing total word count and unique word count.

## Features

- Count the total number of words in a text file.
- Count the number of unique words.
- Identify and display the most common words.

## Installation

To use the Text Analyzer Tool, you'll need to have Python installed. It is recommended to use a virtual environment to manage dependencies.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/owais-kamdar/text-analyzer-tool.git
cd text-analyzer-tool
```

### Step 2: Install the Required Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Install the Text Analyzer Tool using pip:

```bash
pip install -e .
```

# USAGE
text-analyze <file_path> [<top_n>]

top n = number of most common words you want to see (defaults to 10 if no number is entered)
