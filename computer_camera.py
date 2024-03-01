import cv2
import numpy as np
from win32api import GetSystemMetrics

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, GetSystemMetrics(0))
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, GetSystemMetrics(1))

while True:
    ret, frame = capture.read()
    # alpha = frame[:, :, 3]
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.addWeighted(frame, 0.1, frame, 1-0.1, 200)
    cv2.imshow('Output', frame)
    k = cv2.waitKey(10) & 0XFF
    if k == 27: break
capture.release()
cv2.destroyAllWindows()