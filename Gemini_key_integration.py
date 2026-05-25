import google.generativeai as genai
import os

# Read API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Use fixed model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate response
response = model.generate_content(
    "What is the capital of France?"
)

# Print response
print(response.text)