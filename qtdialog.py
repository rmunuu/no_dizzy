import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QDesktopWidget

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0.1) # 0.1, 사진 투명도는 건들 X
        self.setWindowTitle("Video Display")
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.NoFocus)

        # Create a label to display the video
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)

        desktop = QDesktopWidget()
        size = desktop.availableGeometry().size()
        self.label.setFixedSize(size.width(), size.height())
        print(size)

        # Set the size of the window to cover the entire desktop
        self.setGeometry(desktop.availableGeometry())
        self.showFullScreen()

        self.label.setGeometry(0, 0, size.width(), size.height())

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Create a video capture object
        self.capture = cv2.VideoCapture(0)

        # Set the video frame size
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size.height())

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Set the transparency of the frame
            # frame = cv2.resize(frame, (self.label.width(), self.label.height()))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # frame[:,:,3] = 30 # set alpha channel to 128
            # self.label.setFixedSize(frame.shape[1], frame.shape[0])
            # self.label.setFixedSize(size.width(), size.height())
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGBA8888)