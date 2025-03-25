# Car_Number_Plate_Recognition_Sysytem
Car Number Plate Detection

Overview

This project implements a car number plate detection model using OpenCV (cv2). It processes images and videos to detect and extract license plates, making use of Haar cascades and contour detection techniques.

Features

Detects car number plates from images and videos

Uses OpenCV's Haar cascades for plate detection

Extracts and crops detected number plates

Saves the extracted plates as separate images

Requirements

Ensure you have the following dependencies installed:
pip install opencv-python numpy
Installation

Clone the repository:
git clone https://github.com/yourusername/car-number-plate-detection.git
cd car-number-plate-detection
Usage

Run the script to detect number plates from an image:
python detect_plate.py --image path/to/image.jpg
Run the script on a video file:
python detect_plate.py --video path/to/video.mp4
