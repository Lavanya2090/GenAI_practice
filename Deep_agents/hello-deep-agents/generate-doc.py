from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Read all Python files
project_code = ""

for file in Path(".").rglob("*.py"):
    if ".venv" not in str(file):
        project_code += f"\n\n===== FILE: {file} =====\n"
        project_code += file.read_text(encoding="utf-8")

prompt = f"""
You are a Senior Software Architect.

Analyze this entire codebase and generate detailed documentation.

Include:

1. Project Overview
2. Purpose of the Project
3. Folder Structure
4. Code Flow
5. Main Components
6. Functions and Their Responsibilities
7. Agent Architecture
8. Gemini Model Configuration
9. Dependencies Used
10. Execution Flow
11. Example Run
12. Important Concepts
13. Future Enhancements
14. Interview Questions
15. Summary

Output in Markdown format.

Codebase:

{project_code}
"""

response = model.invoke(prompt)

Path("PROJECT_DOCUMENTATION.md").write_text(
    response.content,
    encoding="utf-8"
)

print("Documentation generated successfully!")