import cv2
import numpy as np


image = cv2.imread("watermelon1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
V = np.count_nonzero(image[:, :, 2])
print(np.array(image[:,:,2] > 200))
print(image[:,:,2])
print(V)
