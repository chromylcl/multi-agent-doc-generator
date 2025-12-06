# agents/validator_agent.py

import json
from typing import Any, Dict
from model.llm_client import call_llm

SYSTEM_PROMPT = """
You are a Validation Agent.

You will receive three things:
1) parsed_info: JSON from the parser agent
2) readme_md: README content from the documentation agent
3) folder_struct: JSON from the structure agent

Your task:
- Check for obvious issues, such as:
  - Missing project_name
  - Empty features or tech_stack
  - README missing key sections
  - Folder structure too shallow or weird
- Summarise potential problems and suggestions briefly.

Output format (STRICT JSON):

{
  "ok": boolean,
  "issues": [string, ...],
  "suggestions": [string, ...]
}

Rules:
- If everything looks reasonable, ok should be true and issues can be empty.
- Do NOT output anything except this JSON.
- Do NOT use markdown. No explanations outside JSON.
"""

def run_validator_agent(
    parsed_info: Dict[str, Any],
    readme_md: str,
    folder_struct: Dict[str, Any],
) -> Dict[str, Any]:
    payload = {
        "parsed_info": parsed_info,
        "readme_md": readme_md[:2000],
        "folder_struct": folder_struct,
    }
    user_message = json.dumps(payload, indent=2)

    raw_output = call_llm(SYSTEM_PROMPT, user_message)

    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError:
        data = {
            "ok": False,
            "issues": ["Validator agent returned invalid JSON."],
            "suggestions": [],
            "raw_output": raw_output,
        }

    return data
