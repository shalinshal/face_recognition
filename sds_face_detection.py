# import libraries
import cv2
import sds_face_recognition

cascPath ="C:/Users/Shalin/Anaconda3/Library/etc/haarcascades/"
faceCascade = cv2.CascadeClassifier(cascPath + 'haarcascade_frontalface_default.xml' )
eyeCascade = cv2.CascadeClassifier(cascPath + 'haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

#face detection function
def detect_face(face_recognizer, mirror=False):
    cam = cv2.VideoCapture(0)
    cam.release()
    while True:
        _val, img = cam.read()
        if mirror:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray for face detection
            face = faceCascade.detectMultiScale(gray_img,
								 scaleFactor = 1.2,
								 minNeighbors = 5)
        for (x, y, w, h) in face:                   #detect faces in the image
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            name = sds_face_recognition.predict(face_recognizer, img)
            cv2.putText(img, name, (x,y-5), font, .6,(0,255,0),1,cv2.LINE_AA)
        cv2.imshow('frame',img)
        if cv2.waitKey(5) & 0xFF == ord('q'):       #quit program on pressing 'Q'
            break
    cam.release()
    cv2.destroyAllWindows()    

def main():
    face_recognizer = sds_face_recognition.main()
    detect_face(face_recognizer, mirror=True)

if __name__ == '__main__':
	main()