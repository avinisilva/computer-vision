import numpy as np
from skimage import io, draw

image = np.zeros((100, 100), dtype=np.uint8)
r = np.array([10, 25, 80, 50])
c = np.array([10, 60, 40, 10])
x, y = draw.polygon(r, c)
image[x, y] = 1


io.imshow(image)
io.show()
