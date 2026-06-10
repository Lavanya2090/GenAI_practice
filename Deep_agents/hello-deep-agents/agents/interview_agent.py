from pathlib import Path
from .documentation_agent import build_documentation_agent, read_project_code


def generate_interview_document():

    code = read_project_code()
    documentation_agent = build_documentation_agent()

    result = documentation_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Analyze this project.

                    Generate:

                    1. Beginner Interview Questions
                    2. Intermediate Interview Questions
                    3. Advanced Interview Questions
                    4. Scenario Based Questions
                    5. Deep Agents Questions
                    6. LangChain Questions
                    7. Gemini Questions
                    8. Tool Calling Questions
                    9. Multi Agent Questions
                    10. Real Time Use Cases

                    For every question provide:

                    - Question
                    - Answer
                    - Explanation

                    Project code:

                    {code}

                    Output markdown only.
                    """
                }
            ]
        }
    )

    content = result["messages"][-1].content

    Path("generated").mkdir(exist_ok=True)

    Path(
        "generated/Interview_Questions.md"
    ).write_text(
        content,
        encoding="utf-8"
    )

    return "Interview_Questions.md generated successfully"