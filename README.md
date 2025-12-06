# Multi-Agent Documentation & Project Structure Generator

## Overview

This project is a multi-agent AI system that converts rough, unstructured developer notes into:

- A professional `README.md`
- A layered project folder structure (JSON)
- Optional tree view output in the terminal

The system demonstrates a **Model–Controller–Presenter (MCP)** architecture and **multi-agent collaboration** using LLMs.

---

## Architecture

### MCP Layers

- **Model**

  - `model/llm_client.py` – wraps the LLM client (OpenAI) and handles all model calls.

- **Controller**

  - `controller/pipeline.py` – orchestrates the sequence:
    1. Parser Agent
    2. Documentation Agent
    3. Structure Agent
    4. Validator Agent

- **Presenter**
  - `presenter/formatter.py` – formats and prints folder structure as a human-readable tree.

### Agents

- `agents/parser_agent.py`

  - Role: Parse raw notes into structured JSON (project_name, features, tech_stack, etc.)

- `agents/documentation_agent.py`

  - Role: Generate a professional README.md from parsed JSON.

- `agents/structure_agent.py`

  - Role: Propose a layered folder structure in JSON.

- `agents/validator_agent.py`
  - Role: Validate outputs (parsed JSON, README, folder structure) and report issues/suggestions.

---

## Flow

```text
User Notes
   ↓
Parser Agent (JSON)
   ↓
Documentation Agent (README.md)
   ↓
Structure Agent (Folder JSON)
   ↓
Validator Agent (Issues/Suggestions)
   ↓
Presenter (Tree View, Files)
```
