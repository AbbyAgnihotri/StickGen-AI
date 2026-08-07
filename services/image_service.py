import time

from PIL import Image
from huggingface_hub import InferenceClient

from config import HF_TOKEN


class ImageService:
    """
    Generate images using Hugging Face Inference Providers.
    """

    def __init__(self):

        self.client = InferenceClient(
            api_key=HF_TOKEN
        )

        self.model = "black-forest-labs/FLUX.1-schnell"

    def generate(
        self,
        prompt: str,
        retries: int = 3
    ) -> Image.Image:

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                print(
                    f"Generating image "
                    f"(attempt {attempt}/{retries})..."
                )

                image = self.client.text_to_image(
                    prompt=prompt,
                    model=self.model
                )

                return image

            except Exception as e:

                last_error = e

                print(
                    f"Image generation failed "
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
            "Image generation failed after "
            f"{retries} attempts."
        ) from last_error