import cv2
import keyboard


def mirror_filter(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = frame_gray.shape
    # print(frame_gray.shape)
    for i in range(h):
        for j in range(w):
            if j > w//2:
                frame[i, j] = frame[i, (j-2*(j-w//2)+1)]
    
    return frame


def sticker_glasses_lips(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray)
    # eye = eyes_detector.detectMultiScale(frame_gray)
    glasses_sticker = cv2.imread("input\glasses55.png")
    zip_sticker = cv2.imread("input\lips1.png")
    # print(eyes)
    try:
        for face in faces:
            x, y, w, h = face
            
            eye = eyes_detector.detectMultiScale(frame_gray)
            lips = lips_detector.detectMultiScale(frame_gray, 1.5, 30)
            xx, yy, ww, hh = lips[0]
            zip_sticker = cv2.resize(zip_sticker, [ww, hh])

            for i in range(hh):
                for j in range(ww):
                    if zip_sticker[i][j][0] == 0 and zip_sticker[i][j][1] == 0 and zip_sticker[i][j][2] == 0:
                            zip_sticker[i][j] = image[yy+i, xx+j]
                        
            image[yy:yy+hh, xx:xx+ww] = zip_sticker
            # print(lips)
            
            # cv2.rectangle(image, [xx, yy], [xx + ww, yy + hh], [0, 0, 0], 4)
        
            xl, yl, wl, hl = eye[0]
            # print(eye[0])
                
            xr, yr, wr, hr = eye[1]
            # print(eye[1])
            # cv2.rectangle(image, [x, y], [x+w, y+h], [0, 0, 0], 4)
            sticker_w = w
            sticker_h = int(1.3*hl)
            # print(st_w)
            # print(st_h)
            glasses_sticker = cv2.resize(glasses_sticker, [sticker_w, sticker_h])
            for i in range(sticker_h):
                for j in range(sticker_w):
                    if glasses_sticker[i][j][0] == 0 and glasses_sticker[i][j][1] == 0 and glasses_sticker[i][j][2] == 0:
                        glasses_sticker[i][j] = image[yl+i, x+j] 
            
            image[yl:yl+sticker_h, x:x+sticker_w] = glasses_sticker

    except(IndexError):
        pass

    return image
    


def pixelized_face(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray)

    for face in faces:
        x, y, w, h = face
        face_image = image[y:y+h, x:x+w]
        face_image_small = cv2.resize(face_image, [12, 12])
        face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = face_image_big

    return image

def sticker_face(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray)
    image_sticker = cv2.imread("input\mask3.png")
    for face in faces:
        x, y, w, h = face 

        sticker = cv2.resize(image_sticker, [w, h])

        for i in range(w):
            for j in range(h):
                if sticker[i][j][0] == 0 and sticker[i][j][1] == 0 and sticker[i][j][2] == 0:
                    sticker[i][j] = image[y+i, x+j] 

        image[y:y+h, x:x+w] = sticker

    return image


cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eyes_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
lips_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    _, frame = cap.read()
    

    if keyboard.is_pressed('1'):
        frame1 = sticker_face(frame)
        cv2.imshow("result", frame1)
    if keyboard.is_pressed('2'):
        frame2 = sticker_glasses_lips(frame)
        cv2.imshow("result", frame2)
    if keyboard.is_pressed('3'):
        frame3 = pixelized_face(frame)
        cv2.imshow("result", frame3)
    if keyboard.is_pressed('4'):
        frame4 = mirror_filter(frame)
        cv2.imshow("result", frame4)

    cv2.putText(frame, "face sticker: 1", (10, 390), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    cv2.putText(frame, "glasses and lips stickers: 2", (10, 415), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    cv2.putText(frame, "pixelized face: 3", (10, 440), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    cv2.putText(frame, "mirror_filter: 4", (10, 465), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    
    cv2.imshow("result", frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

