def clean_json(text: str):

    text = text.strip()

    if text.startswith("```"):

        text = text.replace("```json", "")

        text = text.replace("```", "")

    return text.strip()
