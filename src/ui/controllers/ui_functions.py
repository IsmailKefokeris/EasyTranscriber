from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QFileDialog

from main import *


class UIFunctions(MainWindow):
    
    def uiDefinitions(self):
        
        # Browse Button
        self.browseBtn.clicked.connect(self.browse_files)

        # Transcribe Button
        self.transcribeBtn.clicked.connect(self.transcribe_function)

        # Setup Button
        self.setupBtn.clicked.connect(self.initiate_whisper)

        # save Buttons
        self.saveSRTBtn.clicked.connect(self.save_file)
        # self.saveTXTBtn.clicked.connect()


    
