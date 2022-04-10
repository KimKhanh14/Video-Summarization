import cv2 # pip install opencv-python
import numpy as np # pip install numpy

#Get the video
video = cv2.VideoCapture('Result/Human.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(width)