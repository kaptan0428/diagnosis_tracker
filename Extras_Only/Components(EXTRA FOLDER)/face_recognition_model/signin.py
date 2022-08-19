from os import path
import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
video_capture = cv2.VideoCapture(0)
name="jello"
PROJECT_ROOT = path.abspath(path.dirname(__file__))
location = path.join(PROJECT_ROOT, 'Training_images')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(200, 200),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if faces is not 0:
        cv2.imwrite(path.join(location , 'waka.jpg'), frame)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.putText(frame,'Face',(x, y), font, 2,(255,0,0),5)
    cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)      
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()