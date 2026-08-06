from services.image_service import ImageService

service = ImageService()

image = service.generate(

    "minimal stick figure cartoon, black outline, boy riding bicycle"

)

image.save("test.png")