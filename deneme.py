import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a button that when clicked, opens Google in the default web browser
        self.button = QPushButton("Google'a Git", self)
        self.button.clicked.connect(self.open_google)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def open_google(self):
        url = QUrl("https://www.google.com/")
        QDesktopServices.openUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
