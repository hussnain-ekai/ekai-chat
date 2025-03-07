#!/usr/bin/env python
"""
Verify that the ekai-chat package includes proper attribution to Aider
"""

import importlib
import sys
import subprocess
import re

def check_attribution_in_module_docstring():
    """Check if the ekai module docstring has attribution to Aider."""
    print("Checking module docstring for attribution...")
    
    try:
        import ekai
        docstring = ekai.__doc__ or ""
        if "based on Aider" in docstring and "https://github.com/Aider-AI/aider" in docstring:
            print("✅ Module docstring includes proper attribution to Aider")
            return True
        else:
            print("❌ Module docstring is missing proper attribution to Aider")
            return False
    except ImportError:
        print("❌ Could not import ekai module")
        return False

def check_attribution_in_cli_help():
    """Check if the CLI help output includes attribution to Aider."""
    print("Checking CLI help output for attribution...")
    
    try:
        # Run the CLI with --help flag and capture output
        result = subprocess.run(["ekai", "--help"], 
                               capture_output=True, 
                               text=True,
                               check=False)
        
        help_text = result.stdout
        
        if "Based on the excellent Aider project" in help_text:
            print("✅ CLI help includes proper attribution to Aider")
            return True
        else:
            print("❌ CLI help is missing proper attribution to Aider")
            print(f"Help text preview: {help_text[:200]}...")
            return False
    except Exception as e:
        print(f"❌ Error running CLI: {str(e)}")
        return False

def check_attribution_in_readme():
    """Check if README.md has attribution to Aider."""
    print("Checking README.md for attribution...")
    
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        if "Attribution" in readme_content and "based on [Aider]" in readme_content:
            print("✅ README.md includes proper attribution to Aider")
            return True
        else:
            print("❌ README.md is missing proper attribution to Aider")
            return False
    except Exception as e:
        print(f"❌ Error reading README.md: {str(e)}")
        return False

def check_attribution_in_package_metadata():
    """Check if package metadata has attribution to Aider."""
    print("Checking package metadata for attribution...")
    
    try:
        # Use importlib.metadata to get package metadata
        import importlib.metadata
        metadata = importlib.metadata.metadata("ekai-chat")
        description = metadata.get("Description", "")
        
        if "based on the excellent Aider project" in description:
            print("✅ Package metadata includes proper attribution to Aider")
            return True
        else:
            print("❌ Package metadata is missing proper attribution to Aider")
            print(f"Description: {description}")
            return False
    except Exception as e:
        print(f"❌ Error checking package metadata: {str(e)}")
        return False

def main():
    """Verify that ekai-chat includes proper attribution to Aider."""
    print("Running attribution verification for ekai-chat...")
    print("=" * 70)
    
    checks = [
        check_attribution_in_module_docstring,
        check_attribution_in_readme,
    ]
    
    # Only run these if the package is installed
    try:
        import ekai
        checks.append(check_attribution_in_package_metadata)
        checks.append(check_attribution_in_cli_help)
    except ImportError:
        print("⚠️ ekai package not installed, skipping some checks")
    
    results = []
    for check in checks:
        result = check()
        print("-" * 70)
        results.append(result)
    
    success = all(results)
    
    print("=" * 70)
    if success:
        print("✅ All attribution checks passed!")
        print("The ekai-chat package properly credits Aider as its foundation.")
    else:
        print("❌ Some attribution checks failed.")
        print("Please ensure all parts of the package properly credit Aider.")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
