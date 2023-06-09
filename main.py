# AI Imports (Whisper)
import PySide6.QtGui
import torch
import whisper
# Move over to https://github.com/guillaumekln/faster-whisper (faster)

# GUI Elements from PySide6
import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QSplashScreen

# Views Imports
from src.ui.views.mainPage_ui import *

# Extra Scripts Import
from src.scripts.whisperFunctions import *
from src.scripts.video_manipulation_functions import *
from src.scripts.threads.InitWhisperThread import *
from src.scripts.threads.TranscribeAudioThread import *

# Controller Import
from src.ui.controllers.ui_functions import *

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)

        # Set Window Title
        self.setWindowTitle("Transcribing Tool")

        # Icon
        my_icon = QIcon()
        my_icon.addFile(r"src\assets\images\Icon\EasyTranscriberIcon.ico")

        self.setWindowIcon(my_icon)

        # setup Whisper
        self.whisper = None
        # Setup Current Transcription
        self.curr_transcription = None
        self.transcribed = None

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
    
    # Functions

    # Function to setup Whisper
    def start_init_whisper(self):
        model = self.modelChosen.currentIndex()
        self.loading_animation()

        self.load_model_thread = InitWhisperThread(model, self)
        self.load_model_thread.start()

    # Function to Allowing Browsing of Computer files
    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, "Select a File to Transcribe", "F:\EasyTranscriber", 
                                            "Audio (*.mp3);; Video (*.mp4)")
        self.browseUrl.setText(fname[0])
    
    # Function to save the transcribed text into srt (Subtitle File)
    def save_file(self):
        # Needs fixing must include ,000 at the end of all timestamps
        self.statusbar.showMessage("Selecting File Location")

        fname = QFileDialog.getSaveFileName(self, "Select Where you want to Save your file", "F:\EasyTranscriber", "SubRip (*.srt)")

        
        if self.transcribed:
            self.statusbar.showMessage("File Location Selected!")
            time.sleep(1)
            self.statusbar.showMessage("Saving File!")
            self.whisper.save_as_srt(self.displayTranscript, fname[0])
            self.statusbar.showMessage("File Saved!")
        else:
            self.statusbar.showMessage("Must transcribe a file first")
            return False
    
    # Function to start Transcribing through a thread
    def start_transcribe_thread(self):
        if self.whisper:
            # Create and show loading animation
            self.loading_animation()

            self.load_model_thread = TranscribeAudioThread(self)
            self.load_model_thread.start()
            
        self.statusbar.showMessage("Setup Transcriber First")
        return False

    # Cheat Loading Animation Using a GIF
    def loading_animation(self, state = "start"):
        if state == "start":
            self.loading_movie = QMovie(r"src\assets\images\gif\Iphone-spinner-2.gif")
            self.loadingLabel.setMovie(self.loading_movie)
            self.loading_movie.start()
            return True
        
        self.loading_movie.stop()
        self.loadingLabel.clear()
        return True

    def closeEvent(self, event):
        # Stopping all threads
        self.load_model_thread.stop()
        self.load_model_thread.stop()

        # Closes Window 
        event.accept()


    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pixmap = QPixmap(r"src\assets\images\SplashScreen.PNG")
    splash = QSplashScreen(pixmap)
    splash.show()

    splash.showMessage("Loading Main Window...", color="white")
    app.processEvents()

    window = MainWindow()

    window.show()

    splash.finish(window)

    app.exec()