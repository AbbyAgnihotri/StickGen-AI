from huggingface_hub import InferenceClient
from PIL import Image
from config import HF_TOKEN


class ImageService:

    def __init__(self):

        self.client = InferenceClient(
            api_key=HF_TOKEN
        )

    def generate(
        self,
        prompt: str
    ) -> Image.Image:

        try:

            image = self.client.text_to_image(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )

            return image

        except Exception as e:

            raise RuntimeError(
                f"Image generation failed: {e}"
            )