import gradio as gr


def placeholder_generator(story, style, emotion, panels):
    return (
        f"""
Story Received!

Story:
{story}

Style:
{style}

Emotion:
{emotion}

Panels:
{panels}
""",
        None,
    )


with gr.Blocks(title="StickGen AI") as demo:

    gr.Markdown(
        """
# 🎨 StickGen AI

### Story → Comic Generator
"""
    )

    story = gr.Textbox(
        label="Enter your story",
        lines=8,
        placeholder="Type your story here..."
    )

    with gr.Row():

        style = gr.Dropdown(
            choices=[
                "Stick Figure",
                "Comic",
                "Chalk",
                "Sketch"
            ],
            value="Stick Figure",
            label="Drawing Style"
        )

        emotion = gr.Dropdown(
            choices=[
                "Happy",
                "Sad",
                "Angry",
                "Excited"
            ],
            value="Happy",
            label="Emotion"
        )

        panels = gr.Dropdown(
            choices=[2,4,6],
            value=4,
            label="Panels"
        )

    generate_btn = gr.Button(
        "Generate Comic",
        variant="primary"
    )

    status = gr.Textbox(
        label="Status"
    )

    comic = gr.Image(
        label="Generated Comic"
    )

    generate_btn.click(
        fn=placeholder_generator,
        inputs=[
            story,
            style,
            emotion,
            panels
        ],
        outputs=[
            status,
            comic
        ]
    )

demo.launch()