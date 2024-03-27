import cv2


image = cv2.imread("input/cats.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                     "haarcascade_frontalcatface_extended.xml")

cat_faces = cat_detector.detectMultiScale(image_gray)

for face in cat_faces:
    x, y, w, h = face
    cv2.rectangle(image, [x, y], [x+w, y+h], [0, 0, 0], 4)

cv2.imshow("result", image)
cv2.waitKey()