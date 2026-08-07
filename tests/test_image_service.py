from services.image_service import ImageService
from services.prompt_service import PromptService
from utils.file_utils import get_output_path
from tests.test_story_service import story


image_service = ImageService()
prompt_service = PromptService()

service = ImageService()

prompt = prompt_service.build_prompt(
    story,
    story.scenes[0]
)

image = image_service.generate(prompt)

path = get_output_path()

image.save(path)

print(path)

print("Image saved successfully!")