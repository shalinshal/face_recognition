import cv2
#from PIL import Image
cascPath ="C:/Users/Shalin/Anaconda3/Library/etc/haarcascades/"
faceCascade = cv2.CascadeClassifier(cascPath + 'haarcascade_frontalface_default.xml' )
eyeCascade = cv2.CascadeClassifier(cascPath + 'haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
def detect_face(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        _val, img = cam.read()
        if mirror:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = faceCascade.detectMultiScale(gray_img,
								 scaleFactor = 1.2,
								 minNeighbors = 5)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img,'Shalin',(x,y-5), font, .6,(0,255,0),1,cv2.LINE_AA)
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()    

def main():
    detect_face(mirror=True)

if __name__ == '__main__':
	main()
