from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QMainWindow
import time
import whisper

from src.scripts.whisperFunctions import *


class InitWhisperThread(QThread):

    def __init__(self, parent: QMainWindow | None = ...) -> None:
        super().__init__(parent)
        self.parent = parent


    def run(self):
        print("RUNNING THREAD")
        self.parent.statusbar.showMessage("Initiating Whisper Model....Setting Up Transcriber")
        QApplication.processEvents()
        self.parent.whisper = WhisperFunctions()
        self.parent.statusbar.showMessage("Transcriber Setup! Ready for Use!")

    def stop(self):
        pass