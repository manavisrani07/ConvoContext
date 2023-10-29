# ConvoContext

ConvoContext is a Python application that leverages the power of the Hugging Face Transformers library to provide you with instant answers to your questions based on context. It's a versatile tool that can work with various file types like PDFs, DOCX, PPTX, CSV and plain text files.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example Usage](#reference)
- [Contributing](#contributing)

## About

This project is a work in progress, created by [Manav Israni](https://github.com/manavtech07). It may take some time to process larger contexts, but it will improve over time.

## Getting Started

These instructions will help you get started with ConvoConnect and set up the environment.

### Prerequisites

To use ConvoContext, you'll need to have the following installed:

- Python 3
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the ConvoContext repository and change the directory:

   ```bash
   git clone https://github.com/manavtech07/ConvoConnect.git
   cd ConvoConnect
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How It Works

ConvoContext combines the power of language models and file parsing to answer questions based on provided context. It currently supports PDF, DOCX, PPTX, CSV, and plain text file formats.

**ConvoContext is still a work in progress**, and further developments are planned to expand its capabilities and enhance its performance. This project represents a minor step in the journey of mine and aims to provide a foundation for future improvements.

In the case of CSV format, ConvoContext can also provide small insights regarding data, such as identifying the highest salary.

## Usage

1. To upload the content
   ```bash
   from get_content import FileContentReader
   file_reader = FileContentReader()
   from google.colab import files
   uploaded_files = files.upload()
   file_paths = list(uploaded_files.keys())
   file_reader.set_file_paths(file_paths)
   combined_content = file_reader.read_content()

   ```
2. When prompted, enter your question.
3. ConvoContext will provide you with answers based on the provided context.
4. If not this way, you can type the content
   ```bash
   combined_content= input("Content: ")
   ```

5. Now main.py
   ```bash
   from main import QAModel, ContentExtractor

   question = input("Question: \n")

   if model_name == "google/tapas-base-finetuned-wtq":
       qa_model = QAModel(model, tokenizer, tqa)
       answer = qa_model.answer_csv(question, combined_content)
       print("\n------------------------------------------------------------------------------------------------\n\nAnswer: ", answer)
   else:
       qa_model = QAModel(model, tokenizer, tqa)
       answer = qa_model.answer_question(question, combined_content)

       extracted_reference = ContentExtractor.extract_context(combined_content, answer['start'], answer['end'])

       print(f'\n------------------------------------------------------------------------------------------------\n\nAnswer: {answer["answer"]}\n\n------------------------------------------------------------------------------------------------\n\nContext:\n')
       print(extracted_reference)
   ```

## Reference

For reference, you can refer to this Colab notebook: [ConvoContext](https://colab.research.google.com/drive/1RXes7JYkGgsmLbS3mj2o61nOzdI6E29C?usp=sharing)

## Contributing

Contributions to make ConvoContext even better are welcomed. If you'd like to contribute, please open an issue or a pull request on our GitHub repository:)




   
   


   
   


