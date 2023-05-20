# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 620)
        MainWindow.setMinimumSize(QSize(800, 620))
        MainWindow.setMaximumSize(QSize(800, 620))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.browseUrl = QLineEdit(self.centralwidget)
        self.browseUrl.setObjectName(u"browseUrl")
        self.browseUrl.setGeometry(QRect(410, 10, 281, 22))
        self.browseUrl.setReadOnly(True)
        self.browseBtn = QPushButton(self.centralwidget)
        self.browseBtn.setObjectName(u"browseBtn")
        self.browseBtn.setGeometry(QRect(710, 10, 75, 24))
        self.displayTranscript = QListWidget(self.centralwidget)
        self.displayTranscript.setObjectName(u"displayTranscript")
        self.displayTranscript.setGeometry(QRect(10, 120, 771, 401))
        self.displayTranscript.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.displayTranscript.setProperty("isWrapping", False)
        self.transcribeBtn = QPushButton(self.centralwidget)
        self.transcribeBtn.setObjectName(u"transcribeBtn")
        self.transcribeBtn.setGeometry(QRect(710, 40, 75, 24))
        self.saveSRTBtn = QPushButton(self.centralwidget)
        self.saveSRTBtn.setObjectName(u"saveSRTBtn")
        self.saveSRTBtn.setGeometry(QRect(694, 530, 91, 24))
        self.setupBtn = QPushButton(self.centralwidget)
        self.setupBtn.setObjectName(u"setupBtn")
        self.setupBtn.setGeometry(QRect(30, 40, 131, 24))
        self.modelChosen = QComboBox(self.centralwidget)
        self.modelChosen.addItem("")
        self.modelChosen.addItem("")
        self.modelChosen.addItem("")
        self.modelChosen.addItem("")
        self.modelChosen.addItem("")
        self.modelChosen.addItem("")
        self.modelChosen.setObjectName(u"modelChosen")
        self.modelChosen.setGeometry(QRect(10, 10, 171, 22))
        self.loadingLabel = QLabel(self.centralwidget)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(730, 70, 50, 40))
        self.loadingLabel.setMinimumSize(QSize(50, 40))
        self.loadingLabel.setMaximumSize(QSize(50, 40))
        self.loadingLabel.setScaledContents(True)
        self.infoLabel = QLabel(self.centralwidget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(8, 100, 241, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.modelChosen.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.transcribeBtn.setText(QCoreApplication.translate("MainWindow", u"Transcribe", None))
        self.saveSRTBtn.setText(QCoreApplication.translate("MainWindow", u"Save Subtitle", None))
        self.setupBtn.setText(QCoreApplication.translate("MainWindow", u"Setup Transcriber", None))
        self.modelChosen.setItemText(0, QCoreApplication.translate("MainWindow", u"Tiny - Fastest Processing", None))
        self.modelChosen.setItemText(1, QCoreApplication.translate("MainWindow", u"Base - Best Option", None))
        self.modelChosen.setItemText(2, QCoreApplication.translate("MainWindow", u"Small", None))
        self.modelChosen.setItemText(3, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.modelChosen.setItemText(4, QCoreApplication.translate("MainWindow", u"Large - Slowest Processing", None))
        self.modelChosen.setItemText(5, QCoreApplication.translate("MainWindow", u"Large-v2 - Newest", None))

        self.loadingLabel.setText("")
        self.infoLabel.setText("")
    # retranslateUi

