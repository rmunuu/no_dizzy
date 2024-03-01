import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0.1) # 0.1
        self.setWindowTitle("Video Display")

        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_NoMousePropagation)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_X11DoNotAcceptFocus)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)

        desktop = QDesktopWidget()
        size = desktop.availableGeometry().size()
        self.label.setFixedSize(size.width(), size.height())
        print(size)

        self.setGeometry(desktop.availableGeometry())
        self.showFullScreen()

        self.label.setGeometry(0, 0, size.width(), size.height())

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size.height())

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGBA8888)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.timer.stop()
        self.capture.release()
        QApplication.quit()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())