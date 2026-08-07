from PIL import Image, ImageDraw, ImageFont


class ComicService:

    WIDTH = 1024
    HEIGHT = 1024

    PANEL_WIDTH = 470
    PANEL_HEIGHT = 430

    MARGIN = 20

    def build(

        self,

        story,

        images

    ):

        comic = Image.new(

            "RGB",

            (

                self.WIDTH,

                self.HEIGHT

            ),

            "white"

        )

        draw = ImageDraw.Draw(comic)

        try:

            font = ImageFont.truetype(

                "arial.ttf",

                24

            )

        except:

            font = ImageFont.load_default()

        positions = [

            (20,20),

            (530,20),

            (20,520),

            (530,520)

        ]

        for img,scene,pos in zip(

            images,

            story.scenes,

            positions

        ):

            img = img.resize(

                (

                    self.PANEL_WIDTH,

                    self.PANEL_HEIGHT

                )

            )

            comic.paste(

                img,

                pos

            )

            draw.rectangle(

                [

                    pos,

                    (

                        pos[0]+self.PANEL_WIDTH,

                        pos[1]+self.PANEL_HEIGHT

                    )

                ],

                outline="black",

                width=2

            )

            draw.text(

                (

                    pos[0],

                    pos[1]+self.PANEL_HEIGHT+10

                ),

                scene.caption,

                fill="black",

                font=font

            )

        return comic