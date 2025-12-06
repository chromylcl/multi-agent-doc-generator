# controller/pipeline.py

from typing import Dict, Any

from agents.parser_agent import run_parser
from agents.documentation_agent import run_documentation_agent
from agents.structure_agent import run_structure_agent
from agents.validator_agent import run_validator_agent  # we'll create this next


def generate_project(notes: str) -> Dict[str, Any]:
    """
    High-level pipeline controller:
    1) Parse notes
    2) Generate README
    3) Generate folder structure
    4) Validate everything
    Returns a dict with all outputs and any validation issues.
    """

    # 1. Parser Agent
    parsed = run_parser(notes)

    if "error" in parsed:
        return {
            "parsed": parsed,
            "readme_md": "",
            "folder_struct": {},
            "validation": {
                "ok": False,
                "issues": ["Parser agent failed. See parsed['raw_output']."]
            }
        }

    # 2. Documentation Agent
    readme_md = run_documentation_agent(parsed)

    # 3. Structure Agent
    folder_struct = run_structure_agent(parsed, readme_md)

    # 4. Validator Agent (LLM-based)
    validation = run_validator_agent(parsed, readme_md, folder_struct)

    return {
        "parsed": parsed,
        "readme_md": readme_md,
        "folder_struct": folder_struct,
        "validation": validation,
    }
