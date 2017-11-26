from PIL import Image

image = Image.open('images/image01.jpg')

resize_image = image.resize((300, 200))

resize_image.show()
