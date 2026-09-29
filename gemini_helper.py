import os
import json
import re
from dotenv import load_dotenv
from google import genai

# Read the variables from the .env file into the environment
load_dotenv()

# Create the Gemini client using your key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Model name is kept in one variable so it's easy to change later
MODEL_NAME = "gemini-3.5-flash"


def ask_gemini(prompt):
    """Send a prompt to Gemini and return the text response."""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    if not response.text:
        raise ValueError("Gemini returned an empty response. Please try again.")
    return response.text

def extract_json(text):
    """Pull out just the JSON array from Gemini's response, in case it added extra text."""
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("No JSON array found in the response.")



# This block only runs when you execute this file directly
if __name__ == "__main__":
    print(ask_gemini("Explain what a variable is in one sentence."))