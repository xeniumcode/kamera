from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import (
    QCamera,
    QMediaDevices,
    QMediaCaptureSession,
    QImageCapture,
)
from PyQt6.QtMultimediaWidgets import QVideoWidget


class CamPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grayscale_enabled = False

        camera_device = QMediaDevices.defaultVideoInput()
        self.camera = QCamera(camera_device)
        self.preview = QVideoWidget()
        self.preview.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.preview)

        self.session = QMediaCaptureSession()
        self.session.setCamera(self.camera)
        self.session.setVideoOutput(self.preview)

        self.image_capture = QImageCapture()
        self.session.setImageCapture(self.image_capture)

        self.camera.start()
