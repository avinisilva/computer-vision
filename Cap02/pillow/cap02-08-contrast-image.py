from PIL import Image
from PIL import ImageEnhance

image = Image.open('images/image01.jpg')

enhancer = ImageEnhance.Contrast(image)
new_image = enhancer.enhance(2)

new_image.show()
