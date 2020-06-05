from imutils.video import VideoStream
from picamera import PiCamera
import numpy as np
import imutils
import time
import cv2


class SecurityFeed:
    # Initialize the video stream and model, with 2 seconds warm-up and display to console.
    def __init__(self, prototxt, model, labels, colors, thresh=0.2):
        self.prototxt = prototxt
        self.model = model
        self.labels = labels
        self.colors = colors
        self.thresh = thresh
        self.uploads = 0
        print("Loading model...")
        self.net = cv2.dnn.readNetFromCaffe(self.prototxt, self.model)
        print("Starting camera...")
        self.vs = VideoStream(usePiCamera=True).start()
        print("Warming up...")
        time.sleep(2.0)


    # Cleanup.
    def __del__(self):
        cv2.destroyAllWindows()
        self.vs.stop()


    # If person is detected, return True.
    def detect(self):
        # Grab frame, resize, and convert to blob
        frame = self.vs.read()
        frame = imutils.resize(frame, width=400)
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        # Obtain detections.
        self.net.setInput(blob)
        detections = self.net.forward()

        # Loop over detections.
        for i in np.arange(0, detections.shape[2]):
            # Get confidence and categorization of detection.
            confidence = detections[0, 0, i, 2]
            idx = int(detections[0, 0, i, 1])

            # Return True when person detected.
            if confidence > self.thresh and self.labels[idx] == "person":
                print("Person detected on camera.")
                return True

        return False


    def record(self):
        cap = PiCamera()
        self.uploads += 1
        cap.start_recording('/home/pi/Desktop/video{}.h264'.format(str(self.uploads)))

        # Record until person exits frame and leave 15 second buffer
        while not self.detect():
            time.sleep(15)
        cap.stop_recording()
        print("Recording saved locally.")
