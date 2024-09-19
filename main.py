import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from pygame import mixer

class BellMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Call Bell")
        self.setMaximumSize(600, 600)

        self.setCursor(QCursor(Qt.CursorShape.BlankCursor)) #invisible cursor, comment if you want to see him

        mixer.init()

        self.click_sound = mixer.Sound("bell.mp3")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel()
        self.layout.addWidget(self.label)

        pixmap = QPixmap("bell.jpg")
        self.label.setPixmap(pixmap)

        self.central_widget.mousePressEvent = self.play_sound

        self.clicks = 0

    def play_sound(self, event):
        self.clicks += 1

        if self.clicks > 100:
            self.click_sound = mixer.Sound("anime-moan.mp3")
            self.click_sound.play()
            self.clicks = 0
            self.click_sound = mixer.Sound("bell.mp3")

        else:
            self.click_sound.play()

        print(f"Clicks count {self.clicks}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BellMenu()
    window.show()
    sys.exit(app.exec())
