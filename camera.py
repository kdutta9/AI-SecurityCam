from imutils.video.pivideostream import PiVideoStream
import time
import cv2

class Camera:
    def __init__(self, path):
        self.vs = PiVideoStream().start()
        self.detections = 0
        self.path = path
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
        found = False

        for (x, y, w, h) in detections:
            print("Object detected.")
            self.detections += 1
            found = True
            cv2.rectangle(readFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if found:
            cv2.imwrite(self.path + "cap{num}.jpg".format(num=self.detections), readFrame)
            print("Image saved to device.")

        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf
