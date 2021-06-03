# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashTxeouh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"QFrame{\n"
"background-color:rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"border-radius :10px;\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-80, 50, 811, 141))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label__description = QLabel(self.frame)
        self.label__description.setObjectName(u"label__description")
        self.label__description.setGeometry(QRect(-220, 150, 1131, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label__description.setFont(font1)
        self.label__description.setStyleSheet(u"\n"
"color: rgb(145, 145, 145);\n"
"")
        self.label__description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 250, 571, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgb(98, 114, 164);\n"
"	color: rgb(220, 220, 220);\n"
"border-style:none;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
" border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.011, y1:0.476818, x2:1, y2:0.466, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.frame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(-230, 280, 1131, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"\n"
"color: rgb(145, 145, 145);\n"
"")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 330, 1131, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"\n"
"color: rgb(145, 145, 145);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(10, 330, 1131, 20))
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"\n"
"color: rgb(145, 145, 145);\n"
"")
        self.label_credits.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        SplashScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SplashScreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        SplashScreen.setMenuBar(self.menubar)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">COVIDET</span><span style=\" font-size:26pt;\">V2.0</span></p></body></html>", None))
        self.label__description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Made</span><span style=\" font-size:14pt;\"> To be easier...</span></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">loading...</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Made</span> To be easier...</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">created </span>by ISE 6th sem</p><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi
