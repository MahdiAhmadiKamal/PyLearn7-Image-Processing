import cv2


image = cv2.imread("pics\image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(image)

_, image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "BATMAN", (370, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 2)

cv2.imshow("logo", image)
cv2.waitKey()
cv2.imwrite("logo.jpg", image)
