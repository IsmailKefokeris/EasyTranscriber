from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow

from src.ui.controllers.ui_functions import UIFunctions
from ..views.mainPage_ui import *

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        # Connecting to our UI Created in QtDesinger
        self.setupUi(self)

        # Set Window Title
        self.setWindowTitle("Transcribing Tool")

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
