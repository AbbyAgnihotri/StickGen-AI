import gradio as gr

from workflows.comic_workflow import ComicWorkflow


workflow = ComicWorkflow()


def generate_comic(story_text):
    if not story_text or not story_text.strip():
        return None

    try:
        comic = workflow.run(story_text)

        return comic

    except Exception as e:
        print(f"Error: {e}")
        raise gr.Error(str(e))


demo = gr.Interface(
    fn=generate_comic,
    inputs=gr.Textbox(
        label="Enter your story",
        placeholder="Example: Tom learns to ride a bicycle in the park.",
        lines=5
    ),
    outputs=gr.Image(
        label="Generated Stick Cartoon"
    ),
    title="StickGen AI",
    description=(
        "Transform a simple story into a generated stick cartoon."
    ),
    examples=[
        ["Tom learns to ride a bicycle in the park."],
        ["A girl finds a lost puppy and helps it find its owner."],
        ["Two friends build a treehouse together."]
    ]
)


if __name__ == "__main__":
    demo.launch()