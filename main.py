import numpy as np
from camera import SecurityFeed

PROTOTXT = "models/MobileNetSSD_deploy.prototxt.txt" # path to prototxt
MODEL = "models/MobileNetSSD_deploy.caffemodel" # path to model
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"] # model labels
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

security = SecurityFeed(PROTOTXT, MODEL, CLASSES, COLORS)


def start():
    while True:
        if security.detect():
            security.record()


if __name__ == '__main__':
    start()