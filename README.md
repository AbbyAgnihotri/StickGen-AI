# StickGen-AI 🎨

**StickGen-AI** is a Generative AI application that converts a natural-language story into a multi-panel stick cartoon.

The application uses **Google Gemini** to transform the user's story into a structured story containing characters and scenes, generates scene-specific image prompts, uses **Hugging Face FLUX** for image generation, and combines the generated panels into a final comic.

---

## 🚀 Features

* 📝 Convert natural-language stories into structured stories
* 🤖 Generate story structure using Google Gemini
* 👤 Extract and maintain character attributes
* 🎬 Generate multiple scenes from a story
* ✨ Generate image prompts for each scene
* 🎨 Generate cartoon panels using Hugging Face FLUX
* 🖼️ Combine generated panels into a complete comic
* 🌐 Simple application interface
* 🧩 Modular service-based architecture
* ✅ Pydantic-based data validation
* 🧪 Unit and workflow testing
* 🔐 API keys managed through environment variables

---

## 🏗️ Architecture

```text
                         User Story
                             │
                             ▼
                    ┌─────────────────┐
                    │   Application   │
                    │       UI        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Comic Workflow  │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
        ┌──────────────┐          ┌────────────────┐
        │ StoryService │          │ PromptService  │
        └──────┬───────┘          └───────┬────────┘
               │                          │
               ▼                          │
        ┌──────────────┐                  │
        │    Gemini    │                  │
        │  Story LLM   │                  │
        └──────┬───────┘                  │
               │                          │
               └────────────┬─────────────┘
                            ▼
                    ┌────────────────┐
                    │  ImageService  │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ Hugging Face   │
                    │     FLUX       │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │  ComicService  │
                    └───────┬────────┘
                            │
                            ▼
                      Final Comic
```

---

## 🔄 Application Workflow

The application follows the following pipeline:

```text
Natural Language Story
          │
          ▼
      Gemini LLM
          │
          ▼
 Structured Story
 ┌──────────────────┐
 │ Title            │
 │ Characters       │
 │ Scenes           │
 └────────┬─────────┘
          │
          ▼
   Prompt Generation
          │
          ▼
  Scene-specific Prompts
          │
          ▼
 Hugging Face FLUX
          │
          ▼
    Generated Panels
          │
          ▼
   Comic Composition
          │
          ▼
     Final Comic
```

---

## 🧠 GenAI Components

### 1. Story Generation

Google Gemini converts a user's natural-language story into a structured representation.

The generated structure contains:

* Story title
* Characters
* Character attributes
* Scenes
* Scene descriptions
* Scene captions

The structured response is validated using **Pydantic models**.

---

### 2. Prompt Engineering

A dedicated `PromptService` converts the structured story and individual scene information into an image-generation prompt.

The prompt includes:

* Character descriptions
* Character appearance
* Character emotion
* Scene description
* Scene caption
* Cartoon style requirements
* Visual constraints

This helps provide consistent instructions to the image-generation model.

---

### 3. Image Generation

The generated prompts are passed to **Hugging Face Inference Providers** using the FLUX image-generation model.

The current implementation uses:

```text
black-forest-labs/FLUX.1-schnell
```

Each scene produces an individual comic panel.

---

### 4. Comic Composition

`ComicService` takes the generated scene images and combines them into the final comic.

The resulting comic contains multiple generated panels representing the story.

---

## 📁 Project Structure

```text
StickGen-AI/
│
├── app/
│   └── main.py
│
├── models/
│   ├── __init__.py
│   └── schema.py
│
├── services/
│   ├── __init__.py
│   ├── gemini_service.py
│   ├── story_service.py
│   ├── prompt_service.py
│   ├── image_service.py
│   └── comic_service.py
│
├── workflows/
│   └── comic_workflow.py
│
├── prompts/
│   ├── story_prompt.txt
│   └── image_prompt.txt
│
├── tests/
│   ├── test_story_service.py
│   ├── test_prompt_builder.py
│   ├── test_image_service.py
│   ├── test_comic_service.py
│   └── test_workflow.py
│
├── outputs/
│
├── utils/
│   ├── __init__.py
│   └── json_utils.py
│
├── .env
├── .gitignore
├── config.py
├── environment.yml
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | Application development                |
| Google Gemini  | Story generation and structured output |
| Pydantic       | Data validation                        |
| Hugging Face   | Image generation API                   |
| FLUX.1-schnell | Comic panel generation                 |
| Pillow         | Image processing and composition       |
| Gradio         | Application interface                  |
| python-dotenv  | Environment variable management        |
| Git            | Version control                        |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd StickGen-AI
```

### 2. Create the Conda environment

```bash
conda create -n stickgen python=3.11
```

Activate it:

```bash
conda activate stickgen
```

### 3. Install dependencies

Using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, if using the provided Conda environment:

```bash
conda env create -f environment.yml
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
HF_TOKEN=your_huggingface_token
```

The API keys should **never be committed to Git**.

Make sure `.env` is included in `.gitignore`:

```text
.env
```

---

## ▶️ Running the Application

Activate the environment:

```bash
conda activate stickgen
```

Run the application:

```bash
python -m app.main
```

The application will start the user interface.

Enter a story such as:

```text
Tom wants to learn how to ride a bicycle.
At first he is scared and falls down.
His friend encourages him to keep practicing.
Tom tries again and eventually learns to ride
the bicycle.
```

The application will generate a multi-panel comic based on the story.

---

## 🧪 Testing

The project contains tests for individual components as well as the complete workflow.

### Story service

```bash
python -m tests.test_story_service
```

### Prompt service

```bash
python -m tests.test_prompt_builder
```

### Image service

```bash
python -m tests.test_image_service
```

### Comic service

```bash
python -m tests.test_comic_service
```

### Complete workflow

```bash
python -m tests.test_workflow
```

The workflow test verifies the complete pipeline:

```text
Story
  ↓
Prompt
  ↓
Image Generation
  ↓
Comic Composition
```

---

## 📸 Example

### Input

```text
Tom wants to learn how to ride a bicycle.
At first he is scared and falls down.
His friend encourages him to keep practicing.
Tom tries again and eventually learns to ride
the bicycle.
```

### Processing

```text
User Story
    ↓
Gemini
    ↓
Structured Story
    ↓
Scene Extraction
    ↓
Prompt Generation
    ↓
FLUX Image Generation
    ↓
Panel 1
Panel 2
Panel 3
Panel 4
    ↓
Comic Composition
```

### Output

A multi-panel stick cartoon representing the story is generated and saved in the `outputs/` directory.

---

## 🧩 Design Principles

The application follows a modular service-oriented design.

### StoryService

Responsible for:

* Sending the story-generation prompt to Gemini
* Parsing the response
* Validating the result
* Returning a structured `Story` object

### PromptService

Responsible for:

* Building scene-specific image prompts
* Including character information
* Maintaining visual instructions

### ImageService

Responsible for:

* Communicating with Hugging Face
* Generating images from prompts
* Returning PIL images

### ComicService

Responsible for:

* Combining generated images
* Creating the final comic

### ComicWorkflow

Coordinates all services:

```text
StoryService
      ↓
PromptService
      ↓
ImageService
      ↓
ComicService
```

This separation makes the application easier to test, maintain, and extend.

---

## 🔐 Security

API credentials are stored using environment variables.

Do not commit:

```text
.env
```

to the repository.

If an API token is accidentally exposed, revoke it and generate a new token.

---

## ⚠️ Limitations

The current version has several limitations:

* Character appearance may vary between generated panels.
* Image generation depends on external Hugging Face services.
* Generation time depends on API availability and model load.
* Generated images may occasionally differ from the requested scene.
* The application currently focuses on simple stick-cartoon style illustrations.
* The number and layout of panels are based on the current workflow implementation.

---

## 🚀 Future Enhancements

Possible future improvements include:

1. Character reference images for improved consistency
2. Automatic speech-bubble generation
3. Multiple comic layouts
4. User-selectable art styles
5. Image regeneration for individual panels
6. More advanced character consistency
7. Cloud deployment
8. Persistent storage for generated comics
9. Download/export options
10. Support for longer stories

---

## 🎓 Project Objective

The objective of StickGen-AI is to demonstrate how multiple Generative AI capabilities can be combined into a practical end-to-end application.

The project demonstrates:

* Large Language Models
* Prompt Engineering
* Structured LLM Output
* Text-to-Image Generation
* AI Workflow Orchestration
* Image Processing
* Modular Software Architecture

---

## 👨‍💻 Project Status

**Status: Completed ✅**

The current implementation successfully supports:

```text
Natural Language Story
        ↓
AI Story Generation
        ↓
Structured Story
        ↓
Scene Prompt Generation
        ↓
AI Image Generation
        ↓
Comic Composition
        ↓
Final Comic
```

---

## 📄 License

This project was developed as an academic/project implementation.

Add an appropriate license if the repository is intended for public distribution.
