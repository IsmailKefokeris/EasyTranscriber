import datetime
import sys
import whisper
import os
import time

from PySide6.QtWidgets import QApplication, QMainWindow


from src.ui.views.mainPage_ui import *
from src.scripts.whisperFunctions import *
from src.scripts.video_manipulation_functions import *
from src.ui.controllers.ui_functions import *

from src.scripts.threads.InitWhisperThread import *
from src.scripts.threads.TranscribeAudioThread import *

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)

        # Set Window Title
        self.setWindowTitle("Transcribing Tool")

        # setup Whisper
        self.whisper = None
        # Setup Current Transcription
        self.curr_transcription = None

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
    
    # Functions

    def start_init_whisper(self):
        self.load_model_thread = InitWhisperThread(self)
        self.load_model_thread.start()


    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, "Select a File to Transcribe", "F:\EasyTranscriber", 
                                            "Audio (*.mp3);; Video (*.mp4)")
        self.browseUrl.setText(fname[0])
    
    def save_file(self):
        self.statusbar.showMessage("Selecting File Location")

        fname = QFileDialog.getSaveFileName(self, "Select Where you want to Save your file", "F:\EasyTranscriber", "SubRip (*.srt)")

        
        if self.curr_transcription:
            self.statusbar.showMessage("File Location Selected!")
            time.sleep(1)
            self.statusbar.showMessage("Saving File!")
            self.whisper.save_as_srt(self.curr_transcription, fname[0])
            self.statusbar.showMessage("File Saved!")
        else:
            self.statusbar.showMessage("Must transcribe a file first")
            return False
    
    def start_transcribe_thread(self):
        self.load_model_thread = TranscribeAudioThread(self)
        self.load_model_thread.start()
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()