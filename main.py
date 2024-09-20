import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QSoundEffect

class BellMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Call Bell")
        self.setMaximumSize(600, 600)

        # Hide the cursor; comment this line if you want to see the cursor
        self.setCursor(QCursor(Qt.CursorShape.BlankCursor)) 

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel()
        self.layout.addWidget(self.label)

        pixmap = QPixmap("bell.jpg")
        self.label.setPixmap(pixmap)

        self.central_widget.mousePressEvent = self.play_sound

        self.clicks = 0

        # Initialize QSoundEffect for bell
        self.bell_sound = QSoundEffect()
        self.bell_sound.setSource(QUrl.fromLocalFile("bell.wav"))  # Use the converted .wav file
        self.bell_sound.setVolume(0.5)  # Volume: 0.0 to 1.0

        # Initialize QSoundEffect for moan
        self.moan_sound = QSoundEffect()
        self.moan_sound.setSource(QUrl.fromLocalFile("anime-moan.wav"))  # Use the converted .wav file
        self.moan_sound.setVolume(0.5)  # Volume: 0.0 to 1.0

    def play_sound(self, event):
        self.clicks += 1

        if self.clicks > 100:
            self.moan_sound.play()
            self.clicks = 0
        else:
            self.bell_sound.play()

        print(f"Clicks count {self.clicks}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BellMenu()
    window.show()
    sys.exit(app.exec())
