from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and return plain text.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        raise RuntimeError(
            f"Gemini Error: {e}"
        )