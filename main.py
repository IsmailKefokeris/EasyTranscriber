import datetime
import sys
import whisper
import os
import time

from PySide6.QtWidgets import QApplication


from src.ui.views.mainPage_ui import *
from src.scripts.whisperFunctions import *
from src.scripts.video_manipulation_functions import *
from src.ui.controllers.ui_functions import *


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
    
    def transcribe_function(self):
        if self.whisper:
            url = self.browseUrl.text()

            directory, file_name = url.rsplit('/', 1)
            name, extension = file_name.split('.', 1)

            # Check if file is a video
            if extension == "mp4":
                url = video_to_mp3(url, name)

            # Transcribes Audio
            self.statusbar.showMessage("Transcription in Progress, Please Wait!")
            QApplication.processEvents()

            self.curr_transcription = self.whisper.transcribe(url)
            results = self.whisper.display_transcribed_text(self.curr_transcription)

            self.statusbar.showMessage("Transcription Complete! Populating Display....")
            QApplication.processEvents()
            # Displays Audio
            for line in results:
                self.displayTranscript.addItem(line)
            
            self.statusbar.showMessage("Text Displayed!")

            # Deletes the file at the end if it is an mp4 file converted
            if extension == "mp4":
                os.remove(url)
                pass

        self.statusbar.showMessage("Setup Transcriber First")
        return False

    def transcribe_audio(self):
        print("transcribe Audio")

    def transcribe_video(self):
        print("transcribe Video")
    
    def initiate_whisper(self):
        self.statusbar.showMessage("Initiating Whisper Model....Setting Up Transcriber")
        QApplication.processEvents()
        self.whisper = WhisperFunctions()
        self.statusbar.showMessage("Transcriber Setup! Ready for Use!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()