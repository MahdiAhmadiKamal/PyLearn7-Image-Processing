import cv2


image = cv2.imread("input/cats.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat_detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
# cat_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")

cat_faces = cat_detector.detectMultiScale(image_gray)

count = 0
for face in cat_faces:
    x, y, w, h = face
    cv2.rectangle(image, [x, y], [x+w, y+h], [0, 0, 0], 4)
    count  += 1

cv2.putText(image, "number of cats: " + str(count), (20, 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, 0, 2)
cv2.imshow("result", image)
cv2.waitKey()
cv2.imwrite("output/cat detector output.jpg", image)