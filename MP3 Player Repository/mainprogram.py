# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainprogram.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from playsound import playsound
import multiprocessing
from pygame import mixer
from pydub import AudioSegment
import ffmpeg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.songInstanceValue = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 230, 231, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentTextChanged.connect(lambda: self.pushButton.pressed.connect(self.songSwitch))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 350, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.songPlay)
        self.on = False
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuChoose_Song = QtWidgets.QMenu(self.menubar)
        self.menuChoose_Song.setObjectName("menuChoose_Song")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuChoose_Song.menuAction())

        try:
            self.path = os.environ["HOMEPATH"]
            self.path = self.path + "\Documents\Music Folder"
            self.directory = os.listdir(self.path)

        except FileNotFoundError:
            self.path = os.environ["HOMEPATH"]
            self.path = self.path + "\Documents\Music Folder"
            self.directory = os.mkdir(self.path)

        for song in self.directory:
            if song.endswith(".mp3") or song.endswith(".wma"):
                self.song = song.replace(".wma", "")
                
                print(self.song)
                self.comboBox.addItem(self.song)

    

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MP3 Player"))
        self.label_2.setText(_translate("MainWindow", "Play Song"))
        self.pushButton.setText(_translate("MainWindow", "Play"))
        self.menuChoose_Song.setTitle(_translate("MainWindow", "Choose Song"))


    def songPlay(self,song):
        if self.on == False:
            self.on = True
            self.songInstanceValue = self.songInstanceValue + 1
            self.songPath = self.comboBox.currentText()
            for song in self.directory:
                if self.songPath in song:
                    self.songPath = song
            self.songPath = self.comboBox.currentText()
            for song in self.directory:
                if self.songPath in song:
                    self.song = song
                    self.songPath = self.path + f"\{song}"
            if self.songInstanceValue == 1:
                self.p = multiprocessing.Process(target=playsound, args=(self.songPath,))
                self.p.start()
                self.pushButton.setText("Pause")
            else:
                self.errorMessage = QtWidgets.QErrorMessage()
                self.errorMessage.showMessage("Song is already playing")
        elif self.on == True:
                self.on = False
                self.songStop()
                self.songInstanceValue = 0
                self.pushButton.setText("Play")

    def songStop(self):
        self.p.terminate()

    def songSwitch(self): 
        pass
        

        

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    app.aboutToQuit.connect(lambda: ex.p.kill())
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
    

