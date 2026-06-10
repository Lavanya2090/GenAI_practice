import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.interview_agent import generate_interview_document  # import only what you need

load_dotenv()


def main():

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    agent = create_deep_agent(
        model=model,
        tools=[],
        system_prompt="You are a helpful assistant that provides information about the hello-deep-agents project.",
    )

    #print("Hello from hello-deep-agents!")
    
    result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is Deep Agents?"
            }
        ]
    }
)

    print(result)





def interview_questions():

    result = generate_interview_document()

    print(result)

if __name__ == "__main__":
    interview_questions()