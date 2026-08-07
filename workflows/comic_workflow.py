from services.story_service import StoryService
from services.prompt_service import PromptService
from services.image_service import ImageService
from services.comic_service import ComicService


class ComicWorkflow:

    def __init__(self):

        self.story_service = StoryService()

        self.prompt_service = PromptService()

        self.image_service = ImageService()

        self.comic_service = ComicService()

    def run(self, story_text):

        story = self.story_service.create_story(
            story_text
        )

        images = []

        for scene in story.scenes:

            prompt = self.prompt_service.build_prompt(
                story,
                scene
            )

            image = self.image_service.generate(
                prompt
            )

            images.append(image)

        comic = self.comic_service.build(
            story,
            images
        )

        return comic