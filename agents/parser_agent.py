# agents/parser_agent.py

import json
from typing import Any, Dict
from model.llm_client import call_llm

SYSTEM_PROMPT = """
You are a Parser Agent for software projects.

You receive rough, unstructured notes written by a developer about a new feature or project.

Your task:
1. Understand the notes.
2. Extract important information.
3. Return a STRICT JSON object with the following keys:

{
  "project_name": string or null,
  "summary": string or null,
  "goal": string or null,
  "features": [string, ...],
  "tech_stack": [string, ...],
  "requirements": [string, ...],
  "non_functional_requirements": [string, ...],
  "assumptions": [string, ...]
}

Rules:
- If some information is missing, use null for strings or [] for lists.
- DO NOT invent technologies or features that are not implied by the notes.
- DO NOT add any text outside the JSON. No explanations, no commentary, no markdown.
- Output MUST be valid JSON that can be parsed by json.loads() in Python.
"""

def run_parser(notes: str) -> Dict[str, Any]:
    """Run the parser agent on raw notes and return a Python dict."""
    raw_output = call_llm(SYSTEM_PROMPT, notes)

    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError:
        # fallback: return raw text wrapped so we can debug
        parsed = {
            "error": "Invalid JSON from LLM",
            "raw_output": raw_output
        }

    return parsed
