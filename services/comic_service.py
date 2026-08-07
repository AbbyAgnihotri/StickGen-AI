from PIL import Image, ImageDraw, ImageFont

class ComicService:
    """
    Combines generated scene images into a 2x2 comic page.

    ```
    Each panel contains:
    - Generated scene image
    - Character dialogue in a speech bubble
    - Scene caption
    - Panel border
    """

    def __init__(self):
        self.panel_width = 512
        self.panel_height = 512
        self.caption_height = 60

        self.canvas_width = self.panel_width * 2
        self.canvas_height = (
            self.panel_height + self.caption_height
        ) * 2

    def _load_font(self, size=24):
        """
        Load a font safely.

        Falls back to PIL's default font if Arial
        is not available on the system.
        """

        font_paths = [
            "arial.ttf",
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/Arial.ttf",
        ]

        for font_path in font_paths:
            try:
                return ImageFont.truetype(
                    font_path,
                    size
                )
            except OSError:
                continue

        return ImageFont.load_default()

    def _draw_speech_bubble(
        self,
        draw,
        text,
        x,
        y,
        font,
        width=300
    ):
        """
        Draw a speech bubble containing dialogue.
        """

        if not text:
            return

        text = str(text).strip()

        if not text:
            return

        padding = 15
        bubble_height = 80

        # Keep bubble inside the panel
        width = min(
            width,
            self.panel_width - 40
        )

        # Bubble
        draw.rounded_rectangle(
            [
                x,
                y,
                x + width,
                y + bubble_height
            ],
            radius=20,
            fill="white",
            outline="black",
            width=3
        )

        # Small speech-bubble tail
        tail_x = x + 40

        draw.polygon(
            [
                (tail_x, y + bubble_height),
                (tail_x + 20, y + bubble_height),
                (tail_x + 5, y + bubble_height + 15)
            ],
            fill="white",
            outline="black"
        )

        # Dialogue
        draw.text(
            (
                x + padding,
                y + padding
            ),
            text,
            fill="black",
            font=font
        )

    def _draw_caption(
        self,
        draw,
        caption,
        x,
        y,
        font
    ):
        """
        Draw the scene caption underneath a panel.
        """

        caption_y = y + self.panel_height

        draw.rectangle(
            [
                x,
                caption_y,
                x + self.panel_width,
                caption_y + self.caption_height
            ],
            fill="white",
            outline="black",
            width=2
        )

        if not caption:
            return

        caption = str(caption).strip()

        draw.text(
            (
                x + 15,
                caption_y + 18
            ),
            caption,
            fill="black",
            font=font
        )

    def build(self, story, images):
        """
        Build the final 2x2 comic page.

        Parameters
        ----------
        story:
            Validated Story object containing scenes.

        images:
            List of PIL Image objects, one per scene.

        Returns
        -------
        PIL.Image.Image
            Final comic page.
        """

        if not images:
            raise ValueError(
                "No images provided."
            )

        if not story.scenes:
            raise ValueError(
                "Story contains no scenes."
            )

        if len(images) != len(story.scenes):
            raise ValueError(
                f"Number of images ({len(images)}) "
                f"does not match number of scenes "
                f"({len(story.scenes)})."
            )

        # Create white comic canvas
        comic = Image.new(
            "RGB",
            (
                self.canvas_width,
                self.canvas_height
            ),
            "white"
        )

        draw = ImageDraw.Draw(comic)

        # Fonts
        caption_font = self._load_font(24)
        dialogue_font = self._load_font(20)

        # Maximum of four panels for the current 2x2 layout
        if len(images) > 4:
            raise ValueError(
                "ComicService currently supports a maximum "
                "of 4 panels."
            )

        for index, image in enumerate(images):

            scene = story.scenes[index]

            # Determine panel position
            row = index // 2
            col = index % 2

            x = col * self.panel_width

            y = row * (
                self.panel_height
                + self.caption_height
            )

            # Make sure the image is a PIL image
            image = image.convert("RGB")

            # Resize generated image
            image = image.resize(
                (
                    self.panel_width,
                    self.panel_height
                )
            )

            # Place image
            comic.paste(
                image,
                (x, y)
            )

            # Panel border
            draw.rectangle(
                [
                    x,
                    y,
                    x + self.panel_width - 1,
                    y + self.panel_height - 1
                ],
                outline="black",
                width=3
            )

            # Dialogue / speech bubble
            dialogue = getattr(
                scene,
                "dialogue",
                ""
            )

            self._draw_speech_bubble(
                draw=draw,
                text=dialogue,
                x=x + 20,
                y=y + 20,
                font=dialogue_font
            )

            # Caption
            caption = getattr(
                scene,
                "caption",
                ""
            )

            self._draw_caption(
                draw=draw,
                caption=caption,
                x=x,
                y=y,
                font=caption_font
            )

        # Outer border around complete comic
        draw.rectangle(
            [
                0,
                0,
                self.canvas_width - 1,
                self.canvas_height - 1
            ],
            outline="black",
            width=4
        )

        return comic
