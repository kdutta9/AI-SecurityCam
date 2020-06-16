#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import Camera
from pathlib import Path

app = Flask(__name__)
model = "models/haarcascade_fullbody.xml"
savePath = "saves/"
feed = Camera(savePath)

def mkdir():
    print("Initializing save directory...")
    Path(savePath).mkdir(parents=True, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', fps=feed.get_frame(model)[1])


def gen(camera):
    while True:
        frame = camera.get_frame(model)[0]
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(feed), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    mkdir()
    app.run(host='0.0.0.0', threaded=True)