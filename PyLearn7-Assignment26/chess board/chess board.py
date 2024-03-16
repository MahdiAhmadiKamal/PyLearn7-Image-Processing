import cv2


# mat =[[None for i in range(8)] for j in range(8)]
board = cv2.imread("square-512.jpg")

for i in range(8):
    for j in range(8):
        if (i+j) %2 != 0:
            # mat[i][j]=0
            board[i*64:(i+1)*64, j*64:(j+1)*64]=0
        # elif (i+j) %2 == 0:
        #     mat[i][j]=1
            
    # print(mat[i])


cv2.imshow("", board)
cv2.waitKey()
cv2.imwrite("result.jpg", board)




