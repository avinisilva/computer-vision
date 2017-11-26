# Leitura da imagem com skimage

# pip install scikit-image

from skimage import io 

image = io.imread('images/image02.jpg')
io.imshow(image)
io.show()
