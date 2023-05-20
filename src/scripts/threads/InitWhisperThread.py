# PySide6 Functions Import
from PySide6.QtCore import QThread, QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow

# Addtional Scripts Import
from src.scripts.whisperFunctions import *
from src.scripts.FasterWhisperFunctions import *


class InitWhisperThread(QThread):

    def __init__(self, model, parent: QMainWindow | None = ...) -> None:
        super().__init__(parent)
        self.parent = parent
        self.model = model


    def run(self):
        self.parent.statusbar.showMessage("Initiating Whisper Model....Setting Up Transcriber")
        self.parent.whisper = FasterWhisperFunctions(self.model)
        QCoreApplication.processEvents() 
        self.parent.statusbar.showMessage("Transcriber Setup! Ready for Use!")
        self.parent.transcribeBtn.setEnabled(True)

        # Removing Loading animation
        self.parent.loadingLabel.clear()
        QCoreApplication.processEvents()

    def stop(self):
        self.parent.loadingLabel.clear()
        self.terminate()