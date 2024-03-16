import cv2


image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")

print(image1.shape)
print(image2.shape)

for row in range(image1.shape[0]):
    for col in range(image1.shape[1]):
        image1[row, col] = 255- image1[row, col]

for row in range(image2.shape[0]):
    for col in range(image2.shape[1]):
        image2[row, col] = 255- image2[row, col]

# cv2.imshow("result1", image1)
# cv2.imshow("result2", image2)
# cv2.waitKey()
cv2.imwrite("result1.jpg", image1)
cv2.imwrite("result2.jpg", image2)
