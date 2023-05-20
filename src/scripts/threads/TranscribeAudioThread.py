
# Import Operation System Module
import os

# PySide6 Functions Import
from PySide6.QtCore import QThread, Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem

# Additional Scripts Import
from src.scripts.video_manipulation_functions import *
from src.scripts.whisperFunctions import *


class TranscribeAudioThread(QThread):

    def __init__(self, parent: QMainWindow | None = ...) -> None:
        super().__init__(parent)
        self.parent = parent

    def run(self):
        if self.parent.whisper:
            self.parent.transcribeBtn.setEnabled(False)
            self.parent.browseBtn.setEnabled(False)

            # Get Path to Video or Audio
            url = self.parent.browseUrl.text()

            directory, file_name = url.rsplit('/', 1)
            name, extension = file_name.split('.', 1)

            # Check if file is a video
            if extension == "mp4":
                url = video_to_mp3(url, name)

            # Transcribes Audio
            self.parent.statusbar.showMessage("Transcription in Progress, Please Wait!")
            QApplication.processEvents()

            self.parent.curr_transcription, info = self.parent.whisper.transcribe(url)
            self.parent.transcribed = self.parent.whisper.display_transcribed_text(self.parent.curr_transcription)

            self.parent.statusbar.showMessage("Transcription Complete! Populating Display....")
            QApplication.processEvents()

            # Clear all previous Items if any
            self.parent.displayTranscript.clear()

            # Displays Audio
            if self.parent.transcribed:
                for i, line in enumerate(self.parent.transcribed, start=1):
                    item_index = QListWidgetItem(f"{i}")
                    item_time = QListWidgetItem(f"{line[0]} --> {line[1]}")
                    item_text = QListWidgetItem(f"{line[2]}")

                    flags = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable

                    item_text.setFlags(flags)

                    self.parent.displayTranscript.addItem(item_index)
                    self.parent.displayTranscript.addItem(item_time)
                    self.parent.displayTranscript.addItem(item_text)
            
            self.parent.statusbar.showMessage("Text Displayed!")

            # Deletes the file at the end if it is an mp4 file converted
            if extension == "mp4":
                os.remove(url)
            
            self.parent.browseBtn.setEnabled(True)
            self.parent.transcribeBtn.setEnabled(True)

        self.parent.statusbar.showMessage("Setup Transcriber First")
        return False
    
    def stop(self):
        self.terminate()