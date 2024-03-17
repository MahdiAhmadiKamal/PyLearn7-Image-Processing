import cv2


board = cv2.imread("square-512.jpg")
color = 255

for row in range(board.shape[0]):
    color -= 255/board.shape[0]
    for col in range(board.shape[1]):
        board[row][col] = color
    
cv2.imshow("", board)
cv2.waitKey()
cv2.imwrite("result.jpg", board)