from PIL import Image

image = Image.open('images/image01.jpg')

rotated_image = image.rotate(90)

rotated_image.show()
