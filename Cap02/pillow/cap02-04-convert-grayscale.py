from PIL import Image

image = Image.open('images/image01.jpg')

gray_image = image.convert("L")

gray_image.show()
