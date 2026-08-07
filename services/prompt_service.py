from pathlib import Path

IMAGE_PROMPT = Path(
"prompts/image_prompt.txt"
).read_text(
encoding="utf-8"
)

class PromptService:


    def build_prompt(self, story, scene):

        character_descriptions = []

        for character in story.characters:

            description = (
                f"Character: {character.name}. "
                f"Gender: {character.gender}. "
                f"Shirt: {character.shirt}. "
                f"Pants: {character.pants}. "
                f"Hair: {character.hair}. "
                f"Emotion: {character.emotion}."
            )

            character_descriptions.append(
                description
            )

        characters_text = "\n".join(
            character_descriptions
        )

        prompt = IMAGE_PROMPT.format(
            characters=characters_text,
            scene_description=scene.description,
            scene_caption=scene.caption
        )

        return prompt.strip()

