from models.schema import Story

sample = {
    "title": "Learning Bicycle",
    "characters": [
        {
            "name": "Tom",
            "gender": "Boy",
            "shirt": "Blue",
            "pants": "Black",
            "hair": "Short Black",
            "emotion": "Happy"
        }
    ],
    "scenes": [
        {
            "scene": 1,
            "caption": "Tom gets a bicycle.",
            "description": "Tom stands beside a bicycle."
        }
    ]
}

story = Story.model_validate(sample)

print(story)
print(story.characters[0].name)