import cv2
import numpy as np
from win32api import GetSystemMetrics
from PIL import Image

print(GetSystemMetrics(0), GetSystemMetrics(1))

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, GetSystemMetrics(0))
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, GetSystemMetrics(1))

while True:
    ret, frame = capture.read()
    frame = Image.fromarray(frame)
    frame = frame.convert("RGBA")
    frame.putalpha(128)
    frame = np.array(frame)
    cv2.imshow('Output', frame)
    k = cv2.waitKey(10) & 0XFF
    if k == 27: break
capture.release()
cv2.destroyAllWindows()



# import cv2
# import numpy as np
# from win32api import GetSystemMetrics
# from PIL import Image

# capture = cv2.VideoCapture(0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, GetSystemMetrics(0))
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, GetSystemMetrics(1))
