from models.schema import Story, Scene


def build_prompt(story: Story, scene: Scene) -> str:

    character = story.characters[0]

    prompt = f"""
Minimal stick figure cartoon,
simple black line drawing,
vector illustration,
white background,
cute educational illustration,

Character:
Name: {character.name}

Hair: {character.hair}

Shirt: {character.shirt}

Pants: {character.pants}

Emotion:
{character.emotion}

Scene:
{scene.description}

Comic style.
No realistic rendering.
No shading.
No shadows.
Clean outlines.
"""

    return prompt.strip()