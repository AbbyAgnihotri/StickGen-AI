import json


def parse_llm_json(text: str) -> dict:
    """
    Cleans Gemini output and converts it to Python dictionary.
    """

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.startswith("```"):
        text = text.replace("```", "")

    text = text.strip()

    return json.loads(text)