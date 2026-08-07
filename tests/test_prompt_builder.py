from models.schema import Character, Scene, Story
from services.prompt_service import PromptService


story = Story(
    title="Learning Bicycle",
    characters=[
        Character(
            name="Tom",
            gender="boy",
            shirt="Blue",
            pants="Black",
            hair="Short Black",
            emotion="happy"
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


prompt_service = PromptService()

prompt = prompt_service.build_prompt(
    story,
    story.scenes[0]
)

print("\n========== GENERATED PROMPT ==========\n")
print(prompt)
print("\n=======================================\n")