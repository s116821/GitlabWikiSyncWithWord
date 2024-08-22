import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
word_files = [path.strip('"') for path in os.getenv('WORD_FILES').split(',')]
wiki_repo_paths = [path.strip('"') for path in os.getenv('WIKI_REPO_PATHS').split(',')]
destination_host = os.getenv('DESTINATION_HOST').strip('"')

# Function to convert and push each Word document
def convert_and_push(word_file, wiki_repo_path):
    markdown_file = word_file.replace('.docx', '.md')
    
    # Convert Word document to Markdown
    subprocess.run(['pandoc', word_file, '-o', markdown_file])
    
    # Change directory to the wiki repository
    os.chdir(wiki_repo_path)
    
    # Add, commit, and push changes to the GitLab wiki
    subprocess.run(['git', 'add', markdown_file])
    subprocess.run(['git', 'commit', '-m', f'Update wiki content from {word_file}'])
    subprocess.run(['git', 'push', destination_host])

# Process each Word document with its corresponding wiki repository path
for word_file, wiki_repo_path in zip(word_files, wiki_repo_paths):
    convert_and_push(word_file, wiki_repo_path)
