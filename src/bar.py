from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QToolBar, QVBoxLayout
from PyQt6.QtMultimedia import QSoundEffect
from src.camera import CamPreview


class BarView(QWidget):
    def __init__(self, cam: CamPreview, parent=None):
        super().__init__(parent)
        self.cam = cam
        topbar = QToolBar("TopBar")
        topbar.setMovable(False)
        topbar.setIconSize(QSize(24, 24))
        topbar.setStyleSheet("QToolBar { border: 0px; margin: 0px; padding: 0px; }")

        self.shutter = QSoundEffect(self)
        self.shutter.setSource(QUrl.fromLocalFile("src/output.wav"))
        self.shutter.setVolume(0.9)

        act_photo = QAction("Take a picture", self)
        act_photo.triggered.connect(lambda: self.take_photo(cam))
        topbar.addAction(act_photo)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(topbar)

    def take_photo(self, cam: CamPreview):
        self.shutter.play()
        cam.image_capture.captureToFile()
