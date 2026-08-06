import gradio as gr


def greet(name):
    return f"Hello {name}! Welcome to StickGen AI."


with gr.Blocks() as demo:

    gr.Markdown("# 🚀 My First GenAI App")

    name = gr.Textbox(label="Your Name")

    output = gr.Textbox(label="Output")

    button = gr.Button("Say Hello")

    button.click(
        fn=greet,
        inputs=name,
        outputs=output
    )

demo.launch()