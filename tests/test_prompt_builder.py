from models.schema import Character, Scene, Story
from services.prompt_service import build_prompt

story = Story(
    title="Learning Bicycle",
    characters=[
        Character(
            name="Tom",
            gender="boy",
            shirt="Blue",
            pants="Black",
            hair="Short Black"
        )
    ],
    scenes=[
        Scene(
            scene=1,
            caption="Tom starts learning.",
            description="Tom rides a bicycle in a park."
        )
    ]
)

prompt = build_prompt(story, story.scenes[0])

print(prompt)