import os
import cv2
import numpy as np


images_path = os.listdir("input/1")

images_1 = []
for image_path in images_path:
    image = cv2.imread("input/1/" + image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("output/1.jpg", image)
    image = image.astype(np.float32)
    images_1.append(image)

result = np.zeros((2*image.shape[0], 2*image.shape[1]))
# print(result.shape)
for image in images_1:
    result[0:1000, 0:1000] += image

result = result / len(images_1)
result = result.astype(np.uint8)

cv2.imwrite("output/modified.jpg", result)