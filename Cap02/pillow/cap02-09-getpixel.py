from PIL import Image

image = Image.open('images/image01.jpg')

print(image.getpixel((100, 100)))
