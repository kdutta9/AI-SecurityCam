import numpy as np
from camera import SecurityFeed
from flask import Flask, render_template, Response
import threading

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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(security),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    t = threading.Thread(target=start, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)