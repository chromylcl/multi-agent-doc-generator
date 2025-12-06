# agents/structure_agent.py

import json
from typing import Dict, Any
from model.llm_client import call_llm

SYSTEM_PROMPT = """
You are a Project Structure Architect.

You will receive:
- A JSON object with project info (project_name, features, tech_stack, etc.)
- Optionally, a README.md content.

Your task:
Design a clean, layered folder structure for this project.

Output:
- Return ONLY a valid JSON object representing the folder structure.
- Each key is a folder or file.
- Folders map to nested JSON objects.
- Files can be represented as empty strings "" or null.

Example format:

{
  "src": {
    "api": {},
    "models": {},
    "services": {},
    "config": {}
  },
  "tests": {
    "unit": {},
    "integration": {}
  },
  "docs": {},
  "README.md": ""
}

Rules:
- Do NOT include explanations or text outside the JSON.
- Folder names should be generic but meaningful (e.g., src, app, routes, models, services, utils, config, tests, docs).
- If tech_stack suggests frontend + backend, design separate folders (e.g., "frontend", "backend").
- If information is missing, make reasonable standard assumptions, but keep structure simple.
- Output MUST be valid JSON for python json.loads().
"""

def run_structure_agent(project_info: Dict[str, Any], readme_md: str = "") -> Dict[str, Any]:
    """
    Takes parsed project info + README (optional) and returns folder structure as a dict.
    """
    payload = {
        "project_info": project_info,
        "readme_excerpt": readme_md[:1500]  # avoid sending too long strings
    }

    user_message = json.dumps(payload, indent=2)
    raw_output = call_llm(SYSTEM_PROMPT, user_message)

    try:
        struct = json.loads(raw_output)
    except json.JSONDecodeError:
        struct = {
            "error": "Invalid JSON from structure agent",
            "raw_output": raw_output
        }

    return struct
