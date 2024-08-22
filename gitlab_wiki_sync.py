import os
import shutil
import pypandoc
import subprocess

# Get environment variables
word_files = [os.path.expandvars(path) for path in os.getenv('WORD_FILES').split(';')]
wiki_repo_paths = [os.path.expandvars(path) for path in os.getenv('WIKI_REPO_PATHS').split(';')]
destination_hosts = [os.path.expandvars(host) for host in os.getenv('DESTINATION_HOSTS').split(';')]

# Function to convert and push each Word document
def convert_and_push(word_file, wiki_repo_path, destination_host):
    markdown_file = word_file.replace('.docx', '.md')
    
    # Extract the filename from markdown_file and replace spaces with dashes
    markdown_filename = os.path.basename(markdown_file).replace(' ', '-')
    markdown_file = os.path.join(os.path.dirname(markdown_file), markdown_filename)
    
    # Convert Word document to Markdown using pypandoc
    try:
        pypandoc.convert_file(word_file, 'markdown', outputfile=markdown_file)
    except Exception as e:
        print(f"Error converting {word_file} to Markdown: {e}")
        return

    # Move the converted Markdown file to the wiki repository
    dest_markdown_file = os.path.join(wiki_repo_path, os.path.basename(markdown_file))
    try:
        shutil.move(markdown_file, dest_markdown_file)
    except Exception as e:
        print(f"Error moving {markdown_file} to {dest_markdown_file}: {e}")
        return

    # Change directory to the wiki repository destination folder for Converted word doc
    try:
        os.chdir(wiki_repo_path)
    except Exception as e:
        print(f"Error changing directory to {wiki_repo_path}: {e}")
        return

    # Extract the filename from the full path for commit message
    word_file_name = os.path.basename(word_file)
    
    # Add, commit, and push changes to the GitLab wiki using git
    try:
        subprocess.run(['git', 'add', dest_markdown_file], check=True)
        subprocess.run(['git', 'commit', '-m', f"Update wiki content from {word_file_name}"], check=True)
        subprocess.run(['git', 'push', destination_host], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes to the GitLab wiki: {e}")

# Process each Word document with its corresponding wiki repository path and destination host
for word_file, wiki_repo_path, destination_host in zip(word_files, wiki_repo_paths, destination_hosts):
    convert_and_push(word_file, wiki_repo_path, destination_host)