from PIL import Image
from tests.test_story_service import story
from services.comic_service import ComicService

images = [

    Image.open("outputs/panel1.png"),

    Image.open("outputs/panel2.png"),

    Image.open("outputs/panel3.png"),

    Image.open("outputs/panel4.png")

]

comic = ComicService().build(

    story,

    images

)

comic.save(

    "outputs/comic.png"

)