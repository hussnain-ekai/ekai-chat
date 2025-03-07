#!/usr/bin/env python
"""
Script to rebrand Aider to ekai across the codebase.
This script copies files from 'aider' directory to 'ekai',
replacing instances of "aider" with "ekai" and "Aider" with "ekai" in file content.
"""

import os
import re
import shutil
from pathlib import Path

# Define source and destination directories
SRC_DIR = Path('aider')
DEST_DIR = Path('ekai')

# Define subdirectories that need to be created
SUBDIRS = ['coders', 'queries', 'resources', 'website']

# Define replacement patterns
REPLACEMENTS = [
    (re.compile(r'\baider\b'), 'ekai'),  # Exact match for 'aider'
    (re.compile(r'\bAider\b'), 'ekai'),  # Exact match for 'Aider'
    (re.compile(r'\bAIDER\b'), 'ekai'),  # Exact match for 'AIDER'
    (re.compile(r'Aider-AI'), 'hussnain-ekai'),  # GitHub org replacement
    (re.compile(r'aider-chat'), 'ekai-chat'),  # Package name
    (re.compile(r'aider\.chat'), 'ekai.ai'),  # Website domain
]

# Paths to exclude or handle specially
EXCLUDE_PATHS = [
    # Add any paths to exclude here
]

# Create subdirectories
for subdir in SUBDIRS:
    os.makedirs(DEST_DIR / subdir, exist_ok=True)

def process_file_content(content):
    """Replace instances of 'aider' and 'Aider' with 'ekai'."""
    for pattern, replacement in REPLACEMENTS:
        content = pattern.sub(replacement, content)
    return content

def copy_and_modify(src_path, dest_path):
    """Copy file from source to destination and modify its content."""
    # Skip if in exclude list
    if any(exclude in str(src_path) for exclude in EXCLUDE_PATHS):
        return
    
    # Make parent directories if needed
    os.makedirs(dest_path.parent, exist_ok=True)
    
    # Process text-based files
    if src_path.suffix in ['.py', '.md', '.txt', '.html', '.js', '.css', '.toml', '.yml', '.yaml', '.ini']:
        with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Modify content
        modified_content = process_file_content(content)
        
        # Write to destination
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
    else:
        # Copy binary files without modification
        shutil.copy2(src_path, dest_path)

def process_directory(src_dir=SRC_DIR, dest_dir=DEST_DIR):
    """Process all files and directories recursively."""
    for item in src_dir.iterdir():
        # Get destination path
        rel_path = item.relative_to(SRC_DIR)
        dest_path = dest_dir / rel_path
        
        if item.is_dir():
            # Create destination directory
            os.makedirs(dest_path, exist_ok=True)
            # Process subdirectory
            process_directory(item, dest_path)
        else:
            # Process file
            copy_and_modify(item, dest_path)

if __name__ == "__main__":
    print(f"Rebranding from 'aider' to 'ekai'...")
    print(f"Source directory: {SRC_DIR.absolute()}")
    print(f"Destination directory: {DEST_DIR.absolute()}")
    
    # Process the main directory
    process_directory()
    
    print("Rebranding complete!")
