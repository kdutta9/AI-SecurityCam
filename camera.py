from imutils.video.pivideostream import PiVideoStream
import imutils
import time

class Camera:
    def __init__(self):
        self.vs = PiVideoStream().start()
        print("Starting camera...")
        time.sleep(5)

    def __del__(self):
        self.vs.stop()

    def get_frame(self):
        return self.vs.read()
