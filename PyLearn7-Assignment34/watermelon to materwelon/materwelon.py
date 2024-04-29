import cv2


image = cv2.imread("input/watermelon.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

R, G, B = cv2.split(image)

result = cv2.merge([B, R, G])

cv2.imshow("", result)
cv2.waitKey(0)
cv2.imwrite("output/materwelon.jpg", result)