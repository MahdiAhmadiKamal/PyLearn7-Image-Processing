import cv2
import numpy as np

image = np.random.randint(6, size=(5, 5))
snow_image = np.ones_like(image) * 255

box = np.zeros((10,10), dtype=int)
box[0:5, 0:5] = image[0:5, 0:5]

print(box)
print(image)
# print(snow_image)
# print(cv2.add(image, snow_image))
c = np.count_nonzero(image < 1)
# print(c)