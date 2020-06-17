# AI Security Camera
Software that provides a live video feed of a camera and saves images when humans are detected in the frame. Powered by Raspberry Pi.

![Screenshot](https://i.imgur.com/XbX89o3.jpg)

## 📝 Table of Contents
- [Getting Started](#getting_started)
- [Software Used](#software)
- [Contributing](./CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Build Kit
- Raspberry Pi
	- I used a Raspberry Pi Zero W.
- Camera
	- I used the [Raspberry Pi Camera Module V2](https://www.raspberrypi.org/products/camera-module-v2/).
		
### Prerequisites
This project is built in Python 3, so use pip3 to install packages using bash:

```bash
sudo apt install python3-pip
```

### Installing
Clone the repository into any directory of your choice by:
```bash
cd [DIRECTORY-OF-CHOICE]
git clone https://github.com/kdutta9/RPI-SecurityCam
```
I recommend using a virtual environment, using <i>virtualenv</i>, for the project, to ensure there are no errors with dependencies and such. Make sure you create in the virtual environment in the project directory.
- Installing virtualenv
	```bash
	sudo pip3 install virtualenv
	```
- Creating a virtual environment of some name (i.e. venv)
	```bash
	cd RPI-SecurityCam
	virtualenv venv
	```
- Activating virtual environment
	```bash
	source venv/bin/activate
	```

Then, install the required packages.
```bash
pip3 install -r requirements.txt
```

## Software Used <a name = "software"></a>
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) - Object Detection
- [ImUtils](https://github.com/jrosebr1/imutils/) - Image Processing
- [Flask](https://github.com/pallets/flask) - Web Framework

## Authors <a name = "authors"></a>
- [@kdutta9](https://github.com/kdutta9)

See also the list of [contributors](https://github.com/kdutta9/AI-SecurityCam/graphs/contributors) who participated in this project.

## Acknowledgements <a name = "acknowledgement"></a>
- Inspiration for Live Streaming using Flask: [Miguel Greenberg](https://blog.miguelgrinberg.com/post/video-streaming-with-flask)
- Inspiration for Object Detection using OpenCV: [Adrian Rosebrock](https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/)