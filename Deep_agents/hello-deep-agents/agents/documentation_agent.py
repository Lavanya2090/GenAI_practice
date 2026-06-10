from pathlib import Path
from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI


def build_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )


def build_documentation_agent():
    return create_deep_agent(
        model=build_model(),
        tools=[read_project_code],
        system_prompt="""
    You are a Senior Documentation Architect.

    Your responsibilities:

    1. Read source code
    2. Understand architecture
    3. Explain execution flow
    4. Generate markdown documentation
    5. Generate interview preparation notes
    """
    )


def read_project_code():
    """
    Read all project Python files
    """

    code = ""

    for file in Path(".").rglob("*.py"):
        if ".venv" not in str(file):
            code += f"\n\n===== FILE: {file} =====\n"
            code += file.read_text(encoding="utf-8")

    return code
