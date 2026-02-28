import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
import yt_dlp


class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setFixedSize(500, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Paste YouTube URL:")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://www.youtube.com/...")
        layout.addWidget(self.url_input)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def download_video(self):
        url = self.url_input.text().strip()

        if not url:
            QMessageBox.critical(self, "Error", "Please enter a YouTube URL.")
            return

        save_path = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if not save_path:
            return

        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'best'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            QMessageBox.information(
                self,
                "Success",
                f"Download Completed!\n\nSaved in:\n{save_path}"
            )

        except Exception as e:
            QMessageBox.critical(self, "Download Failed", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())