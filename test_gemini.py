from google import genai

from config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def ask_gemini(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {e}"

print(
    ask_gemini(
        "Explain AI in one sentence."
    )
)