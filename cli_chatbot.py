from google import genai
import os
import json

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Memory file
MEMORY_FILE = "chat_history.json"

# Create chat session
chat = client.chats.create(
    model="gemini-2.0-flash",
    config={
        "system_instruction": """
        You are an expert DevOps and AI assistant.
        """
    }
)

print("\n=== Persistent AI Chatbot ===")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print("\nSaving chat memory...")

        serializable_history = []

        for message in chat.get_history():

            serializable_history.append({
                "role": message.role,
                "parts": [
                    part.text for part in message.parts
                ]
            })

        with open(MEMORY_FILE, "w") as f:
            json.dump(serializable_history, f, indent=2)

        print("Chat ended.")
        break

    try:

        print("\nAI: ", end="")

        stream = chat.send_message_stream(user_input)

        for chunk in stream:
            print(chunk.text, end="", flush=True)

        print("\n")

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            print("\n[ERROR] API quota exceeded.")
            print("Please wait and try again.\n")

        elif "503" in error_message:
            print("\n[ERROR] Gemini servers are busy.")
            print("Please retry shortly.\n")

        else:
            print(f"\nUnexpected Error: {e}\n")