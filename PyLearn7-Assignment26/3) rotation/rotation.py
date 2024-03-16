import numpy
import cv2



image = cv2.imread("3.jpg")
result1 = numpy.rot90(image)
result2 = numpy.rot90(result1)


# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         try:
#             image[i,j] = image[image.shape[0]-i, image.shape[1]-j]
            
#         except(IndexError):
#             pass


cv2.imwrite("result2.jpg", result2)