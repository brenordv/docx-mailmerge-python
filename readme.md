# Mail Merge Automation Repository

## What is this repository?

This repository contains scripts to demonstrate the process of automated generation of personalized documents using the
mail merge functionality. It includes a script for generating random test data (`data_fetcher.py`) and a main 
script (`main.py`) that performs the mail merge using a provided Word document template.

You could change the implementation of the `data_fetcher.py` script to fetch data from a database or other data source
that will suit your needs. The main script will remain almost the same (you might need to delete/remove the print
statements).

> Note: I'm not sure, but you might need to parse datetime objects to string before using them on the Word document.
> Not sure about that...

## Required Packages

Before running the scripts, ensure you have the following packages installed:

- `python-docx`: for reading, writing, and creating Word documents.

You can install itusing pip:

```bash
pip install -r requirements.txt
```

# How to Use

1. Prepare Your Template:
   - Create a Word document template with the necessary merge fields and save it in the ./templates/ directory. The
   fields should correspond to the data you wish to merge (e.g., firstname, lastname).

2. Generate Random Data (Optional):
   - Run the random_data_generator.py script to generate test data for the mail merge. You can modify this script to
   include additional fields or different sample data.

3. Perform the Mail Merge:
   - Run the mail_merge_script.py script. This script reads your template and the generated data to create personalized
documents for each entry in the data set.

4. Check the Results:
   - The merged documents will be saved in the ./merged_documents/ directory. Each document will be named using a 
combination of a unique identifier and the recipient's name for easy identification.

# Important Gotchas
- Template Fields: Ensure that the field names in your Word document template exactly match the keys in your data 
source. Mismatches will result in fields not being properly replaced.
- Document Format: The template must be a Word document (.docx). Other formats are not supported by the python-docx and 
mailmerge packages.
- Output Directory: The script assumes an ./merged_documents/ directory for output. If it doesn't exist, the script will
attempt to create it, but you should ensure you have the necessary permissions.
- Encoding Issues: Be mindful of character encoding. If your data contains special or non-ASCII characters, ensure your
environment and the Word document handle them correctly.
- Dependencies: Always work in a virtual environment and ensure you've installed all required dependencies before
running the scripts.

# Contributing
Feel free to fork this repository and contribute by submitting a pull request. We appreciate your input in improving 
this mail merge automation demo tool!

# References
- The sample template was downloaded from here: https://support.redtailtechnology.com/s/article/Sample-Mail-Merge-Letter-Templates
