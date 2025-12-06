# main.py

from controller.pipeline import generate_project
from presenter.formatter import print_folder_tree
import json

def main():
    print("Paste your rough project notes (end with an empty line):")
    

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    notes = "\n".join(lines)
    # ---- Safety / Ethical Content Filter ----
    banned_words = ["kill", "suicide", "weapon", "bomb", "attack", "harm"]
    if any(word in notes.lower() for word in banned_words):
        print("❌ The input contains harmful or unsafe content. Processing aborted.")
        return

    # Continue normal workflow
    result = generate_project(notes)

    result = generate_project(notes)

    parsed = result["parsed"]
    readme_md = result["readme_md"]
    folder_struct = result["folder_struct"]
    validation = result["validation"]

    print("\n=== Parsed JSON ===")
    print(json.dumps(parsed, indent=2))

    print("\n=== Generated README.md ===\n")
    print(readme_md)

    with open("GENERATED_README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)
        print("\nREADME saved to GENERATED_README.md")

    print("\n=== Folder Structure JSON ===")
    print(json.dumps(folder_struct, indent=2))

    print("\n=== Folder Structure Tree View ===")
    if "error" not in folder_struct:
        print_folder_tree(folder_struct)
    else:
        print("Could not render tree (invalid folder_struct JSON).")

    print("\n=== Validation Result (from Validator Agent) ===")
    print(json.dumps(validation, indent=2))

if __name__ == "__main__":
    main()
