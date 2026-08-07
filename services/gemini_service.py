from google import genai
from config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)

model="gemini-2.5-flash"


def ask_gemini(
    prompt: str,
    retries: int = 3
) -> str:

    last_error = None

    for attempt in range(1, retries + 1):

        try:

            print(
                f"Calling Gemini "
                f"(attempt {attempt}/{retries})..."
            )

            # Keep your existing Gemini API call here.
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text

        except Exception as e:

            last_error = e

            print(
                f"Gemini request failed "
                f"on attempt {attempt}: {e}"
            )

            if attempt < retries:

                wait_time = attempt * 2

                print(
                    f"Retrying in "
                    f"{wait_time} seconds..."
                )

                time.sleep(wait_time)

    raise RuntimeError(
        f"Gemini request failed after "
        f"{retries} attempts."
    ) from last_error