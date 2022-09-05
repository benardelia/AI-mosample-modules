import cv2 
from cvzone.FaceDetectionModule import FaceDetector

# object of face_detector frome cvzone  module
my_face = FaceDetector()
# initialization of primary camera 
video = cv2.VideoCapture(0)


while True:
    success, frame = video.read()
    is_face_detected, face = my_face.findFaces(frame)

    cv2.imshow('Face', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break