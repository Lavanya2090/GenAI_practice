from langchain_google_genai import ChatGoogleGenerativeAI
from deepagents import create_deep_agent
from tools.stock_price import get_stock_price


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

agent = create_deep_agent(
    model=model,
    tools=[get_stock_price],
    system_prompt="You are a stock assistant."
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Use the get_stock_price tool for TCS.NS"
            }
        ]
    }
)

print(response)



# test_model.py

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

response = model.invoke("What is AWS?")

print(response)