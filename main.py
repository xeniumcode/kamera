import sys
from src.camera import CamPreview
from src.bar import BarView
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kamera")
        self.cam_preview = CamPreview()
        self.bar_view = BarView(self.cam_preview)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.bar_view)
        layout.setSpacing(1)
        layout.addWidget(self.cam_preview, 1)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.resize(700, 500)

    app.exec()
