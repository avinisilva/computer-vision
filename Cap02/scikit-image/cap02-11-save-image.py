from skimage import io

image = io.imread('images/image02.jpg')

io.imsave('images/new_image.jpg', image)
