from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.stock_price import get_stock_price

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=[get_stock_price]
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current price of TCS.NS?"
            }
        ]
    }
)

print(result)