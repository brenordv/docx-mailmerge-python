import os
from pathlib import Path

from mailmerge import MailMerge

from src.data_fetcher import generate_random_data

# Define the path for the template and the output directory
template_path = './templates/Letter_Appt.Confirm.docx'
output_dir = './merged_documents/'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

number_of_recipients = 5  # Number of documents to create

# Perform the mail merge
with MailMerge(template_path) as document:
    for count, recipient in generate_random_data(number_of_recipients):
        filename = f'{count:05d}__{recipient["firstname"]}_{recipient["lastname"]}.docx'

        document.merge(**recipient)
        output_path = Path(output_dir).joinpath(filename)
        document.write(output_path)
        print(f'Document for {recipient["firstname"]} {recipient["lastname"]} created at {output_path}')

print('Mail merge complete. Documents are in the merged_documents directory.')
