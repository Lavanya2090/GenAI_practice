from google import genai
import os

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create chat session
chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("\n=== Gemini CLI Chatbot ===")
print("Type 'exit' to quit\n")

while True:

    # User input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("\nChat ended.")
        break

    try:
        # Send message to Gemini
        response = chat.send_message(user_input)

        # Print AI response
        print(f"\nAI: {response.text}\n")

    except Exception as e:
        print(f"\nError: {e}\n")