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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 616)
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
        self.transcribeBtn = QPushButton(self.centralwidget)
        self.transcribeBtn.setObjectName(u"transcribeBtn")
        self.transcribeBtn.setGeometry(QRect(710, 40, 75, 24))
        self.saveSRTBtn = QPushButton(self.centralwidget)
        self.saveSRTBtn.setObjectName(u"saveSRTBtn")
        self.saveSRTBtn.setGeometry(QRect(710, 530, 75, 24))
        self.saveTXTBtn = QPushButton(self.centralwidget)
        self.saveTXTBtn.setObjectName(u"saveTXTBtn")
        self.saveTXTBtn.setGeometry(QRect(630, 530, 75, 24))
        self.setupBtn = QPushButton(self.centralwidget)
        self.setupBtn.setObjectName(u"setupBtn")
        self.setupBtn.setGeometry(QRect(10, 10, 121, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.transcribeBtn.setText(QCoreApplication.translate("MainWindow", u"Transcribe", None))
        self.saveSRTBtn.setText(QCoreApplication.translate("MainWindow", u"Save as srt", None))
        self.saveTXTBtn.setText(QCoreApplication.translate("MainWindow", u"Save as txt", None))
        self.setupBtn.setText(QCoreApplication.translate("MainWindow", u"Setup Transcriber", None))
    # retranslateUi

