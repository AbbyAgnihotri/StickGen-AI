from services.prompt_service import PromptService
from models.schema import *

story = Story(

    title="Learning Bicycle",

    characters=[

        Character(

            name="Tom",

            gender="Boy",

            shirt="Blue",

            pants="Black",

            hair="Short Black",

            emotion="Happy"

        )

    ],

    scenes=[

        Scene(

            scene=1,

            caption="Tom begins",

            description="Tom rides a bicycle in a green park."

        )

    ]

)

service = PromptService()

prompt = service.build_prompt(
    story,
    story.scenes[0]
)

print(prompt)