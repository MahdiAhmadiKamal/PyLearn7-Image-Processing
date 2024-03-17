import cv2


image = cv2.imread("Mahmoud_Hesabi.png")
color = 255

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        if image.shape[1]-col-200<row<image.shape[1]-col-160:
            image[row][col] = 0
    
cv2.imshow("", image)
cv2.waitKey()
cv2.imwrite("result.jpg", image)