from pathlib import Path

PROMPT = Path("prompts/story_prompt.txt").read_text(encoding="utf-8")

user_story = """
A girl wants to learn cycling.

She falls.

Her father teaches her.

She wins a race.
"""

full_prompt = f"""
{PROMPT}

Story:

{user_story}
"""