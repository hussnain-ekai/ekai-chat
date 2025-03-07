"""
Simple test script to verify the ekai-chat package installation
"""

import importlib.util
import sys

def check_module_exists(module_name):
    """Check if a module can be imported."""
    print(f"Checking if {module_name} can be imported...")
    try:
        importlib.import_module(module_name)
        print(f"✅ {module_name} imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Could not import {module_name}: {str(e)}")
        return False

def main():
    """Test the installation of ekai-chat package."""
    print("Running ekai-chat installation test...")
    
    # Check if ekai module can be imported
    if not check_module_exists("ekai"):
        print("Failed to import the ekai module. Installation may be incorrect.")
        sys.exit(1)
    
    # Try to import some key modules
    modules_to_check = [
        "ekai.main",
        "ekai.commands",
        "ekai.models",
        "ekai.io"
    ]
    
    failures = 0
    for module in modules_to_check:
        if not check_module_exists(module):
            failures += 1
    
    if failures == 0:
        print("\n✅ All checks passed! The ekai-chat package appears to be properly installed.")
        print("\nTo start using ekai, run:")
        print("  ekai --help")
    else:
        print(f"\n❌ {failures} check(s) failed. There may be issues with the ekai-chat installation.")
        print("\nTry reinstalling the package with:")
        print("  pip install -e .")

if __name__ == "__main__":
    main()
