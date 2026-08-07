import time

from PIL import Image
from google import genai
from google.genai import types

from config import GEMINI_API_KEY

class ImageService:
    """
    Generate comic panel images using Gemini.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = "gemini-2.5-flash-image"

    def generate(
        self,
        prompt: str,
        retries: int = 4
    ) -> Image.Image:

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                print(
                    f"Generating image "
                    f"(attempt {attempt}/{retries})..."
                )

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=[prompt],
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE"]
                    )
                )

                if not response.parts:
                    raise RuntimeError(
                        "Gemini returned no response parts."
                    )

                for part in response.parts:

                    if part.inline_data is not None:

                        image = part.as_image()

                        if image is not None:

                            print(
                                "Image generated successfully."
                            )

                            return image

                raise RuntimeError(
                    "Gemini response did not contain an image."
                )

            except Exception as e:

                last_error = e

                error_text = str(e)

                print(
                    f"Image generation failed "
                    f"on attempt {attempt}: {error_text}"
                )

                # Only retry temporary availability/rate-limit errors
                retryable = (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                )

                if not retryable:
                    raise RuntimeError(
                        f"Gemini image generation failed: "
                        f"{error_text}"
                    ) from e

                if attempt < retries:

                    wait_time = 2 ** attempt

                    print(
                        f"Temporary Gemini error. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

        raise RuntimeError(
            "Gemini image generation failed after "
            f"{retries} attempts."
        ) from last_error

