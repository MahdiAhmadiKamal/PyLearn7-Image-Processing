import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread("input/download.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("", image)
cv2.waitKey()
print(image.shape)


rows = int(input("enter image's width: "))
cols = int(input("enter image's height: "))


img = np.zeros((cols, rows), dtype=np.uint8)
cv2.imshow("", img)
cv2.waitKey()