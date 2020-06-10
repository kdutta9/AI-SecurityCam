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

    def get_frame(self):
        readFrame = self.vs.read()
        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf
