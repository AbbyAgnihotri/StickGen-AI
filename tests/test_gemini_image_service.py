print("TEST FILE STARTED")

from services.image_service import ImageService

print("ImageService imported")

service = ImageService()

print("ImageService created")

image = service.generate(
"""
Create a simple children's stick cartoon.
A boy named Tom is riding a bicycle in a sunny park.
Short black hair, blue shirt, black pants.
Simple black line art.
White background.
No text.
"""
)

print("Image returned")

image.save(
"outputs/test_gemini_image.png"
)

print("IMAGE SAVED")
