import os,sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from splash import Ui_SplashScreen
import time
counter = 0



############SplashScreen#################################
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
#Frameless
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Progress)
        # TIMER IN MILLISECONDS
        self.timer.start(70)
        self.show()
    def Progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP



        # INCREASE COUNTER
        counter += 1
        if counter == 101:
            time.sleep(0.5)
            self.destroy()
            os.system("script.py")
            exit(0)
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen() #= QMainWindow()
    sys.exit(app.exec_())
