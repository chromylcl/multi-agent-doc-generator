# tests/test_parser.py

from agents.parser_agent import run_parser

def test_parser_returns_json_like():
    notes = "Build a todo app with login, add tasks, mark complete, delete tasks. Use React and Django."
    result = run_parser(notes)

    assert isinstance(result, dict)
    assert "features" in result
    assert "tech_stack" in result
