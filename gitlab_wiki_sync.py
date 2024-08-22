import subprocess
import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
word_files = [path.strip('"') for path in os.getenv('WORD_FILES').split(',')]
wiki_repo_paths = [path.strip('"') for path in os.getenv('WIKI_REPO_PATHS').split(',')]
destination_hosts = [path.strip('"') for path in os.getenv('DESTINATION_HOSTS').split(',')]

# Function to convert and push each Word document
def convert_and_push(word_file, wiki_repo_path, destination_host):
    markdown_file = word_file.replace('.docx', '.md')
    
    # Convert Word document to Markdown
    subprocess.run(['pandoc', word_file, '-o', markdown_file])

    # Move the converted Markdown file to the wiki repository
    dest_markdown_file = os.path.join(wiki_repo_path, os.path.basename(markdown_file))
    shutil.move(markdown_file, dest_markdown_file)
    
    # Change directory to the wiki repository destination folder for Converted word doc
    os.chdir(wiki_repo_path)

    # Extract the filename from the full path for commit message
    word_file_name = os.path.basename(word_file)
    
    # Add, commit, and push changes to the GitLab wiki
    subprocess.run(['git', 'add', dest_markdown_file])
    subprocess.run(['git', 'commit', '-m', f'Update wiki content from {word_file_name}'])
    subprocess.run(['git', 'push', destination_host])

# Process each Word document with its corresponding wiki repository path and destination host
for word_file, wiki_repo_path, destination_host in zip(word_files, wiki_repo_paths, destination_hosts):
    convert_and_push(word_file, wiki_repo_path, destination_host)
