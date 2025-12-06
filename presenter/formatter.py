# presenter/formatter.py

from typing import Dict, Any

def print_folder_tree(struct: Dict[str, Any], indent: str = ""):
    """Pretty-print the JSON folder structure as a tree."""
    for name, value in struct.items():
        print(f"{indent}- {name}")
        if isinstance(value, dict):
            print_folder_tree(value, indent + "  ")
