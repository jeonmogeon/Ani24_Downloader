from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
from urllib.request import urlretrieve
from clint.textui import progress
import os.path  
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import ssl

context = ssl._create_unverified_context()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 339)
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dn_alert = QtWidgets.QLabel(self.centralwidget)
        self.dn_alert.setGeometry(QtCore.QRect(100, 80, 470, 16))
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        font.setPointSize(10)
        self.dn_alert.setFont(font)
        self.dn_alert.setText("If you want to close, PLEASE press Stop. It'll stop background progress.")
        self.dn_alert.setObjectName("dn_alert")
        self.dn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dn_btn.setGeometry(QtCore.QRect(600, 80, 81, 21))
        self.dn_btn.setObjectName("dn_btn")
        self.end_btn = QtWidgets.QPushButton(self.centralwidget)
        self.end_btn.setGeometry(QtCore.QRect(690, 80, 81, 21))
        self.end_btn.setObjectName("end_btn")
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
        self.end_btn.setText(_translate("MainWindow", "Stop"))
        self.dn_link.setText(_translate("MainWindow", "https://ani24do.com/ani_list/2858.html"))
        self.title.setText(_translate("MainWindow", "Ani24 Video Link"))
        self.Copy.setText(_translate("MainWindow", "Made by Morgan_KR, Ani24_Downloader"))
        self.dn_status.setText(_translate("MainWindow", "Downloader Started~!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSet_Directory.setText(_translate("MainWindow", "Set Directory"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))

class WindowClass(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.dn_btn.clicked.connect(self.printTextFunction)
        self.end_btn.clicked.connect(self.endprocess)

        self.dn_progress1.setMinimum(0)
        self.dn_progress2.setMinimum(0)

    def printTextFunction(self) :
        ipaddress=socket.gethostbyname(socket.gethostname())
        if ipaddress=="127.0.0.1":
            self.dn_status.setText("Not Connected")
        else:
            self.dn_status.setText(ipaddress)
            download(self.dn_link.text(), self)
            dnln = 0
    
    def endprocess(self):
        sys.exit()

def vidLinkDown(vidLink, fname, self):
    self.dn_status.setText("Downloading..")
    r = requests.get(vidLink, stream=True, allow_redirects=True, verify=False)
    print(vidLink)
    with open(fname, 'wb') as f:
        print(r.headers.get('content-length'))
        if r.headers.get('content-length') == None:
            print("Error!! Can't Load Video")
            self.dn_status.setText("Error!! Can't Load Video")
        else:
            total_length = int(r.headers.get('content-length'))
            filesize = 0
            self.dn_progress1.setMaximum(100)
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                filesize += 102400/total_length
                self.dn_progress1.setValue(filesize)
                QApplication.processEvents()
                if chunk:
                    f.write(chunk)
                    f.flush()
    
    self.dn_status.setText("Download Complete")

def download(web_url, self):
    print(web_url)
    url_type = web_url.split('/')
    dnln = 0
    if url_type[3] == "ani_list":
        print("LIST")
        self.dn_status.setText("Loading... Might seen as Stopped.")
        print("Loading... Might seen as Stopped.")
        QApplication.processEvents()
        req = urllib.request.Request(web_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=ssl._create_unverified_context())
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find_all('img', {'onerror' : "this.src='/img/video_no_image.jpg'"})

        img_url_len = len(img_url)
        dnlnt = img_url_len
        self.dn_status.setText("Loading Complete")
        print("Loading Complete")

        for i in range(0, img_url_len):
            jpg_file_name = img_url[i].get('src').split('/')[5]
            link_num = jpg_file_name.split('.')[0]
            print(img_url[i].get('alt') + " " + link_num)
            fname = img_url[i].get('alt') + ".mp4"

            self.dn_fname.setText(fname)
            lname = fname.split(" ")
            for i in range(len(lname)-2, len(lname)):
                lname[i] = ""
            self.dn_name.setText(' '.join(lname))
            QApplication.processEvents()
            vidLink = "http://test.ani24image.com/ani/download.php?id=" + link_num

            dnln += int(100/dnlnt)
            self.dn_progress2.setMaximum(int(100/dnlnt)*int(dnlnt))
            self.dn_progress2.setValue(dnln)
            QApplication.processEvents()
            if os.path.isfile(fname):
                self.dn_status.setText("Video Already Exists")
                print("Video Already Exists")
            else:
                vidLinkDown(vidLink, fname, self)

    elif url_type[3] == "ani_view":
        print("VIEW")
        self.dn_status.setText("Loading... Might seen as Stopped.")
        QApplication.processEvents()
        req = urllib.request.Request(web_url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        url_name = soup.find('div', {'class' : "qwgqwf"}).text
        link_name = url_name
        link_num = url_type[4].split('.')[0]
        fname = link_name + ".mp4"

        self.dn_fname.setText(fname)
        QApplication.processEvents()
        lname = fname.split(" ")
        for i in range(len(lname)-2, len(lname)):
            lname[i] = ""
        self.dn_name.setText(' '.join(lname))
        
        print(link_name + " " + link_num)

        vidLink = "http://test.ani24image.com/ani/download.php?id=" + link_num

        self.dn_progress2.setValue(100)
        QApplication.processEvents()
        if os.path.isfile("/" + fname):
            self.dn_status.setText("Video Already Exists")
            print("Video Already Exists")
        else:
            vidLinkDown(vidLink, fname, self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = WindowClass() 
    win.show()
    app.exec_()
