from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import time
import cv2

class Camera:
    def __init__(self, path):
        self.vs = PiVideoStream().start()
        self.detections = 0
		
        # Set path to saved images.
        self.path = path
		
        # Let camera warm up for 5 seconds.
        print("Starting camera...")
        time.sleep(5)
        self.fps = FPS().start()

    def __del__(self):
        self.vs.stop()
        cv2.destroyAllWindows()

    def get_frame(self):
        readFrame = self.vs.read()
		
        # Get FPS reading.
        self.fps.update()
        self.fps.stop()

        # Return bytes of frame.
        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf, self.fps.fps()

    def detect(self, model):
        readFrame = self.vs.read()
		
        # Initialize object detection.
        cascade = cv2.CascadeClassifier(model)
        gray = cv2.cvtColor(readFrame, cv2.COLOR_BGR2GRAY)
        detections = cascade.detectMultiScale(gray, 1.3, 4)
        found = False

        # Draw rectangle around detections.
        for (x, y, w, h) in detections:
            print("Object detected.")
            self.detections += 1
            found = True
            cv2.rectangle(readFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save image of detection to device.
        if found:
            cv2.imwrite(self.path + "cap{num}.jpg".format(num=self.detections), readFrame)
            print("Image saved to device.")

        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf