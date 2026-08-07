from pathlib import Path

from models.schema import Story
from services.gemini_service import ask_gemini
from utils.json_utils import parse_llm_json

PROMPT = Path(
    "prompts/story_prompt.txt"
).read_text(encoding="utf-8")

class StoryService:

    def create_story(self, user_story: str) -> Story:
        """
        Convert a user story into a validated Story object.
        """

        full_prompt = f"""
    {PROMPT}

    Story:

    {user_story}
    """

        response = ask_gemini(full_prompt)

        data = parse_llm_json(response)

        story = Story.model_validate(data)

        return story