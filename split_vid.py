import cv2
import numpy as np
import os

cap = cv2.VideoCapture('black_flag.mp4')

if not os.path.exists('data'):
    os.makedirs('data')

width = int(256)
height = int(256)
dim = (width, height)

skip = 0
currentFrame = 0
while(True):
    ret, frame = cap.read()

    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(name, resized)

    cap.set(1, skip)
    skip += 5
    currentFrame += 1

cap.release()
cv2.destroyAllWindows()
