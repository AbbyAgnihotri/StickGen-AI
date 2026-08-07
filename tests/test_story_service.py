from services.story_service import create_story

story = create_story(
"""
A boy learns to ride a bicycle.

He falls twice.

His father teaches him.

He finally rides confidently.
"""
)

print(story.model_dump_json(indent=4))