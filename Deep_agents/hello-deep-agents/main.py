import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.stock_price import get_stock_price
from tools.fundamentals import *
from tools.technical_indicators import *
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
    
#     result = agent.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "What is Deep Agents?"
#             }
#         ]
#     }
# )

#     print(result)

# if __name__ == "__main__":
#     main()



def interview_questions():

    result = generate_interview_document()

    print(result)

# if __name__ == "__main__":
#     interview_questions()

def create_stock_agent():

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    return create_deep_agent(
        model=model,
        tools=[get_stock_price, get_company_fundamentals, get_technical_indicators],
        system_prompt="""
        You are a professional stock analyst.

            When a user asks:

            - Should I buy a stock?
            - Is a stock a good investment?
            - Should I hold or sell?

            You MUST perform the following steps:

            1. Call get_stock_price.
            2. Call get_company_fundamentals.
            3. Call get_technical_indicators.

            After gathering all data provide:

            - Current Price
            - Fundamental Analysis
            - Technical Analysis
            - Risks
            - Opportunities
            - Verdict (BUY/HOLD/AVOID)

            Do not provide recommendations until all three tools have been used.
        """
    )


def select_agent():

    print("\nAvailable Agents:")
    print("1. Deep Agent Demo")
    print("2. Stock Agent")

    choice = input("\nSelect Agent (1/2): ").strip()

    agent_map = {
        "1": {
            "agent": main,
            "query": "What is Deep Agents?"
        },
        "2": {
            "agent": create_stock_agent,
            "query": "Should I buy TCS.NS for long-term investment?"
        }
    }

    if choice not in agent_map:
        print("Invalid Choice")
        return

    selected = agent_map[choice]

    # Create only the selected agent
    agent = selected["agent"]()

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": selected["query"]
                }
            ]
        }
    )

    print("\nResponse:")
    print(result)


if __name__ == "__main__":
    select_agent()

# print(
#     get_stock_price.invoke(
#         {"symbol": "TATATECH.NS"}
#     )
# )