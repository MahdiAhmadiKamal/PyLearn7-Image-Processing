import cv2
import numpy as np


image = cv2.imread("input/watermelon.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

H, S, V = cv2.split(image)

# Green in OpenCV: 60 degrees
# Blue in OpenCV: 120 degrees
H_new = H.copy().astype(np.float32)

for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if 30 < H[i, j] < 80:
            H_new[i, j] -= 50
        if H_new[i, j] < 0:
            H_new[i, j] += 180
        if H[i, j] < 15 or H[i, j] > 165:
            H_new[i, j] += 60

H_new = H_new.astype(np.uint8)

result = cv2.merge([H_new, S, V])
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

cv2.imshow("", result)
cv2.waitKey(0)
cv2.imwrite("output/materwelon_hsv.jpg", result)