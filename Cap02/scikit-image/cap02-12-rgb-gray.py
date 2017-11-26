from skimage import color, io

image = io.imread('images/image02.jpg')

gray_image = color.rgb2gray(image)

io.imshow(gray_image)
io.show()
