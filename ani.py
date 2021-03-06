# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Projects\ani24.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 339)
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dn_btn.setGeometry(QtCore.QRect(690, 80, 81, 21))
        self.dn_btn.setObjectName("dn_btn")
        self.dn_progress2 = QtWidgets.QProgressBar(self.centralwidget)
        self.dn_progress2.setGeometry(QtCore.QRect(20, 200, 761, 21))
        self.dn_progress2.setProperty("value", 0)
        self.dn_progress2.setObjectName("dn_progress2")
        self.dn_link = QtWidgets.QLineEdit(self.centralwidget)
        self.dn_link.setGeometry(QtCore.QRect(20, 40, 761, 31))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(11)
        self.dn_link.setFont(font)
        self.dn_link.setObjectName("dn_link")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 20, 331, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.dn_fname = QtWidgets.QLabel(self.centralwidget)
        self.dn_fname.setGeometry(QtCore.QRect(20, 120, 721, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(12)
        self.dn_fname.setFont(font)
        self.dn_fname.setText("")
        self.dn_fname.setObjectName("dn_fname")
        self.dn_name = QtWidgets.QLabel(self.centralwidget)
        self.dn_name.setGeometry(QtCore.QRect(20, 180, 721, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(12)
        self.dn_name.setFont(font)
        self.dn_name.setText("")
        self.dn_name.setObjectName("dn_name")
        self.dn_progress1 = QtWidgets.QProgressBar(self.centralwidget)
        self.dn_progress1.setGeometry(QtCore.QRect(20, 140, 761, 21))
        self.dn_progress1.setProperty("value", 0)
        self.dn_progress1.setObjectName("dn_progress1")
        self.Copy = QtWidgets.QLabel(self.centralwidget)
        self.Copy.setGeometry(QtCore.QRect(20, 280, 231, 16))
        self.Copy.setObjectName("Copy")
        self.dn_status = QtWidgets.QLabel(self.centralwidget)
        self.dn_status.setGeometry(QtCore.QRect(490, 270, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dn_status.setFont(font)
        self.dn_status.setObjectName("dn_status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_Directory = QtWidgets.QAction(MainWindow)
        self.actionSet_Directory.setObjectName("actionSet_Directory")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuFile.addAction(self.actionSet_Directory)
        self.menuFile.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ani24 Downloader"))
        self.dn_btn.setText(_translate("MainWindow", "Download"))
        self.dn_link.setText(_translate("MainWindow", "https://ani24do.com/ani_list/2858.html"))
        self.title.setText(_translate("MainWindow", "Ani24 Video Link"))
        self.Copy.setText(_translate("MainWindow", "Made by Morgan_KR, Ani24_Downloader"))
        self.dn_status.setText(_translate("MainWindow", "Downloader Started~!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSet_Directory.setText(_translate("MainWindow", "Set Directory"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
