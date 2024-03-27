import cv2
import numpy as np


my_image = np.ones((500, 700), dtype=np.uint8) * 255
my_image[0:500, 0:100] = 70
my_image[0:500, 100:200] = 120
my_image[0:500, 200:300] = 70
my_image[0:500, 300:400] = 120
my_image[0:500, 400:500] = 70
my_image[0:500, 500:600] = 120
my_image[0:500, 600:700] = 70

cv2.rectangle(my_image, (25, 25), (675, 475), 255, 5)

cv2.rectangle(my_image, (25, 130), (140, 370), 255, 5)
cv2.rectangle(my_image, (25, 180), (85, 320), 255, 5)

cv2.rectangle(my_image, (560, 130), (675, 370), 255, 5)
cv2.rectangle(my_image, (615, 180), (675, 320), 255, 5)

cv2.circle(my_image, (350, 250), 75, 255, 5)
cv2.circle(my_image, (350, 250), 5, 255, 5) 
cv2.line(my_image, (350, 25), (350, 475), 255, 5)


cv2.imshow("result", my_image)
cv2.waitKey()