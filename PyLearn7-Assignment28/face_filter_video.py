import cv2


def chess_face(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray)

    for face in faces:
        x, y, w, h = face
        face_image = image[y:y+h, x:x+w]
        face_image_small = cv2.resize(face_image, [12, 12])
        face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = face_image_big

    return image

def sticker(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray)
    image_sticker = cv2.imread("input\lightbulb.png")
    for face in faces:
        x, y, w, h = face 

        sticker = cv2.resize(image_sticker, [w, h])
        image[y:y+h, x:x+w] = sticker

    return image
        

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

while True:
    _, frame = cap.read()
    
    cv2.imshow("result", frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    if cv2.waitKey(25) & 0xFF == ord('1'):
        frame = sticker(frame)
        cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('2'):
        ...
    if cv2.waitKey(25) & 0xFF == ord('3'):
        frame = chess_face(frame)
        cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('4'):
        ...

    
