from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import cv2

class Camera:
    def __init__(self):
        self.vs = PiVideoStream().start()
        print("Starting camera...")
        time.sleep(5)

    def __del__(self):
        self.vs.stop()
        cv2.destroyAllWindows()

    def get_frame(self, model):
        readFrame = self.vs.read()
        cascade = cv2.CascadeClassifier(model)
        gray = cv2.cvtColor(readFrame, cv2.COLOR_BGR2GRAY)
        detections = cascade.detectMultiScale(gray, 1.3, 4)

        for (x, y, w, h) in detections:
            print("Object detected...")
            cv2.rectangle(readFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf
