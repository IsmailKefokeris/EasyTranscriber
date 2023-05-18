from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QFileDialog

from main import *


class UIFunctions(MainWindow):
    
    def uiDefinitions(self):
        
        # Browse Button
        self.browseBtn.clicked.connect(self.browse_files)

        # Transcribe Button
        self.transcribeBtn.clicked.connect(self.start_transcribe_thread)
        self.transcribeBtn.setEnabled(False)


        # Setup Button
        self.setupBtn.clicked.connect(self.start_init_whisper)

        # save Buttons
        self.saveSRTBtn.clicked.connect(self.save_file)
        


    
