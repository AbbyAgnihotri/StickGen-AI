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

    def run(self, story_text, progress=None):

        if progress:
            progress(0.10, desc="Generating story...")

        story = self.story_service.create_story(
            story_text
        )

        images = []

        total_scenes = len(story.scenes)

        for index, scene in enumerate(story.scenes):

            if progress:
                progress(
                    0.20 + (
                        0.60 * index / total_scenes
                    ),
                    desc=(
                        f"Generating scene "
                        f"{index + 1} of "
                        f"{total_scenes}..."
                    )
                )

            prompt = self.prompt_service.build_prompt(
                story,
                scene
            )

            image = self.image_service.generate(
                prompt
            )

            images.append(image)

        if progress:
            progress(
                0.85,
                desc="Building comic..."
            )

        comic = self.comic_service.build(
            story,
            images
        )

        return comic