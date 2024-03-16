import cv2


image_1 = cv2.imread("1.jpg")
image_2 = cv2.imread("2.jpg")

print(image_1.shape)
print(image_2.shape)

image_1_colored = cv2.cvtColor(image_1, cv2.COLOR_)
