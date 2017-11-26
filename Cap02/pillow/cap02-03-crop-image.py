from PIL import Image

image = Image.open('images/image01.jpg')

dimensions = (100, 100, 400, 400)
cropped_image = image.crop(dimensions)

cropped_image.show()
