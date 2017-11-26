import numpy as np
from skimage import io, draw 

image = np.zeros((100, 100), dtype=np.uint8)

x, y = draw.circle(50, 50, 10)
image[x, y] = 1

io.imshow(image)
io.show()
