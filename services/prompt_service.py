from models.schema import Story, Scene


class PromptService:
    """
    Converts Story objects into optimized image prompts.
    """

    BASE_STYLE = """
minimal stick figure cartoon,
simple black line art,
white background,
vector illustration,
educational comic,
clean outlines,
cute,
minimal details,
comic style,
black outlines
"""

    NEGATIVE_PROMPT = """
photorealistic,
3d,
oil painting,
watermark,
signature,
text,
logo,
extra fingers,
extra arms,
blurry,
low quality
"""

    def build_prompt(
        self,
        story: Story,
        scene: Scene
    ) -> str:

        character = story.characters[0]

        prompt = f"""
{self.BASE_STYLE}

Character

Name: {character.name}

Gender: {character.gender}

Hair: {character.hair}

Shirt: {character.shirt}

Pants: {character.pants}

Emotion: {character.emotion}

Scene

{scene.description}

Negative Prompt

{self.NEGATIVE_PROMPT}
"""

        return prompt.strip()