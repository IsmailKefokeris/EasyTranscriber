import os
from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QMainWindow
import time
import whisper


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

            self.parent.curr_transcription = self.parent.whisper.transcribe(url)
            results = self.parent.whisper.display_transcribed_text(self.parent.curr_transcription)

            self.parent.statusbar.showMessage("Transcription Complete! Populating Display....")
            QApplication.processEvents()
            # Displays Audio
            for line in results:
                self.parent.displayTranscript.addItem(line)
            
            self.parent.statusbar.showMessage("Text Displayed!")

            # Deletes the file at the end if it is an mp4 file converted
            if extension == "mp4":
                os.remove(url)
            
            self.parent.browseBtn.setEnabled(True)
            self.parent.transcribeBtn.setEnabled(True)

        self.parent.statusbar.showMessage("Setup Transcriber First")
        return False
    
    def stop(self):
        pass