from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import wget
import requests
from urllib.request import urlretrieve
from clint.textui import progress
import os.path  
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ani24.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.dn_btn.clicked.connect(self.printTextFunction)

        self.dn_progress1.setMinimum(0)
        self.dn_progress2.setMinimum(0)

    def printTextFunction(self) :
        download(self.dn_link.text(), self)
        dnln = 0

def vidLinkDown(vidLink, fname, self):
    r = requests.get(vidLink, stream=True, allow_redirects=True)
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

def download(web_url, self):

    print(web_url)
    url_type = web_url.split('/')
    dnln = 0
    if url_type[3] == "ani_list":
        print("LIST")
        self.dn_status.setText("Loading... Might seen as Stopped.")
        QApplication.processEvents()
        req = urllib.request.Request(web_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find_all('img', {'onerror' : "this.src='/img/video_no_image.jpg'"})

        img_url_len = len(img_url)
        dnlnt = img_url_len

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
        req = urllib.request.Request(web_url, headers={'User-Agent': 'Mozilla/5.0'})
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
