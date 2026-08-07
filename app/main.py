import gradio as gr
from pathlib import Path
from datetime import datetime
from workflows.comic_workflow import ComicWorkflow


print("Starting StickGen AI...")

print("Initializing workflow...")
workflow = ComicWorkflow()
print("Workflow initialized.")

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_comic(
    story_text,
    progress=gr.Progress()
):

    if not story_text or not story_text.strip():
        raise gr.Error(
            "Please enter a story."
        )

    try:

        comic = workflow.run(
            story_text,
            progress=progress
        )

        progress(
            0.95,
            desc="Saving comic..."
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output_path = (
            OUTPUT_DIR /
            f"comic_{timestamp}.png"
        )

        comic.save(output_path)

        progress(
            1.0,
            desc="Comic ready!"
        )

        return comic, str(output_path)

    except Exception as e:

        print(f"Error: {e}")

        raise gr.Error(
            f"Generation failed: {e}"
        )

with gr.Blocks(title="StickGen AI") as demo:

    gr.Markdown(
        """
        # 🖊️ StickGen AI

        ### Turn your story into a stick cartoon comic
        """
    )

    with gr.Row():

        story_input = gr.Textbox(
            label="Enter your story",
            placeholder=(
                "Example: Tom learns to ride a bicycle "
                "in the park."
            ),
            lines=8
        )

    generate_button = gr.Button(
        "🎨 Generate Comic",
        variant="primary"
    )

    comic_output = gr.Image(
        label="Generated Comic",
        type="pil"
    )

    download_output = gr.File(
        label="Download Comic"
    )

    generate_button.click(
        fn=generate_comic,
        inputs=story_input,
        outputs=[comic_output, download_output]
    )

    gr.Examples(
        examples=[
            ["Tom learns to ride a bicycle in the park."],
            [
                "A girl finds a lost puppy and helps "
                "it find its owner."
            ],
            [
                "Two friends build a treehouse together."
            ],
        ],
        inputs=story_input
    )


if __name__ == "__main__":
    demo.launch()