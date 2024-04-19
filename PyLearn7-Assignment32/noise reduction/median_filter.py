import cv2
import numpy as np


image1=cv2.imread("Input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
image2=cv2.imread("Input/board.tif", cv2.IMREAD_GRAYSCALE)
image3=cv2.imread("Input/image.tif", cv2.IMREAD_GRAYSCALE)
image4=cv2.imread("Input/balloons.png")
image5=cv2.imread("Input/face.png")
image6=cv2.imread("Input/fig.tif", cv2.IMREAD_GRAYSCALE)

result1 = cv2.medianBlur(image1, 3)

result2 = cv2.medianBlur(image2, 3)
result2 = cv2.medianBlur(result2, 3)

result3 = cv2.medianBlur(image3, 3)
result3 = cv2.medianBlur(result3, 3)

result4 = cv2.medianBlur(image4, 3)
result4 = cv2.medianBlur(result4, 3)
result4 = cv2.medianBlur(result4, 3)

result5 = cv2.medianBlur(image5, 3)
result5 = cv2.medianBlur(result5, 3)
result5 = cv2.medianBlur(result5, 3)
result5 = cv2.medianBlur(result5, 3)

result6 = cv2.medianBlur(image6, 3)
result6 = cv2.medianBlur(result6, 3)

result1 = np.hstack((image1, result1))
result2 = np.hstack((image2, result2))
result3 = np.hstack((image3, result3))
result4 = np.hstack((image4, result4))
result5 = np.hstack((image5, result5))
result6 = np.hstack((image6, result6))

cv2.imwrite("output/result1.jpg", result1)
cv2.imwrite("output/result22.jpg", result2)
cv2.imwrite("output/result33.jpg", result3)
cv2.imwrite("output/result444.jpg", result4)
cv2.imwrite("output/result5555.jpg", result5)
cv2.imwrite("output/result66.jpg", result6)
