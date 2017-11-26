from skimage import color, io

image = io.imread('images/image03.jpg')

hsv_image = color.rgb2hsv(image)

io.imshow(hsv_image)
io.show()
