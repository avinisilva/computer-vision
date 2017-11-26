from PIL import Image
from PIL import ImageEnhance

image = Image.open('images/image01.jpg')

enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(2)

bright_image.show()
