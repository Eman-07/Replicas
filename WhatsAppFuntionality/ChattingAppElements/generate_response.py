# generate_response.py
import google.generativeai as genai
import sys

genai.configure(api_key="ENTER_API_KEY")

def generate(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = sys.argv[1]  # Get the prompt from command-line arguments
    print(generate(prompt))
