import cv2


board = cv2.imread("square-512.jpg")

print(board.shape)


board[246:266, 246:266] = 0

board[226:246, 266:286] = 0
board[226:246, 226:246] = 0

board[206:226, 286:306] = 0
board[206:226, 206:226] = 0

board[186:206, 306:326] = 0
board[186:206, 186:206] = 0

board[186:306, 306:326] = 0
board[186:306, 186:206] = 0


cv2.imshow("", board)
cv2.waitKey()
cv2.imwrite("result.jpg", board)