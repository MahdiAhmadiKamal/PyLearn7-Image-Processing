import cv2

image = cv2.imread("input/rubik.png")
rows, cols, _ = image.shape


for row in range(rows):
    for col in range(cols):
        B, G, R = image[row, col]
        if B==255 and G==0 and R==0 :
            B = 0
            G = 255
            R = 255
        elif B==0 and G==255 and R==0 :
            B = 255
            G = 0
            R = 255
        elif B==255 and G==255 and R==0 :
            B = 0
            G = 0
            R = 255
        image[row, col] = B, G, R
        

cv2.imshow("", image)
cv2.waitKey(0)
cv2.imwrite("output/result.jpg", image)