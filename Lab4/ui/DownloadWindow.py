from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from datetime import datetime
from matplotlib import pyplot as plt
import requests
import os
import matplotlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.labels = []
        self.sizes = []
        self.times = []
        self.durations = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 531, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 60, 221, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 531, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 180, 221, 23))
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 131, 16))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 270, 531, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 300, 221, 23))
        self.progressBar_3.setMaximum(100)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 412, 400, 61))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        os.environ['KMP_DUPLICATE_LIB_OK']='True'
    
    
    
    def start(self):
        link1 = self.lineEdit.text()
        link2 = self.lineEdit_2.text()
        link3 = self.lineEdit_3.text()
        if not link1 == '':
            t1 = threading.Thread(target = self.download_file, args = (link1, self.progressBar))
            t1.start()
        if not link2 == '':
            t2 = threading.Thread(target = self.download_file, args = (link2, self.progressBar_2))
            t2.start()
        if not link3 == '':
            t3 = threading.Thread(target = self.download_file, args = (link3, self.progressBar_3))
            t3.start()
        try:
            t1.join()
        except:
            pass
        try:
            t2.join()
        except: 
            pass
        try:
            t3.join()
        except:
            pass
        plt.rcParams['font.size'] = '6'
        plt.subplot(121)
        plt.xlabel('File size')
        plt.pie(self.sizes, labels = self.labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.subplot(122)
        plt.xlabel('Download time plot')
        plt.ylabel('Download time')
        plt.bar(self.labels, self.times)
        ax = plt.gca()
        self.autolabel(ax.patches, ax, self.durations, height_factor = 1.01)
        plt.grid()        
        plt.show()
        print(self.durations)
    def autolabel(self, rects, ax, labels=None, height_factor=1.01,):
        for i, rect in enumerate(rects):
            height = rect.get_height()
            if labels is not None:
                try:
                    label = labels[i]
                except (TypeError, KeyError):
                    label = ' '
                else:
                    label = '%d' % int(height)
                ax.text(rect.get_x() + rect.get_width()/2., height_factor*height,
                '{}'.format(label),
                ha='center', va='bottom')
    def download_file(self, link, progressBar):
        start_time = datetime.now()
        r = requests.get(link, stream = True)
        size = int(r.headers.get('content-length'))
        progressBar.setMaximum(size)
        name = link.split('/')[-1]
        with open('data/{}'.format(name), 'wb') as f:
            for chunk in r.iter_content(chunk_size = 4096):
                if chunk:
                    f.write(chunk)
                    progressBar.setValue(progressBar.value() + 4096)
        end_time = datetime.now()
        start = matplotlib.dates.date2num(start_time)
        end = matplotlib.dates.date2num(end_time)
        diff = end - start
        duration = end_time - start_time
        self.labels.append(name + '[{} bytes]'.format(size))
        self.sizes.append(size)
        self.times.append(diff)
        self.durations.append('{}s {}ms'.format(duration.seconds, duration.microseconds / 1000))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузка файлов"))
        self.label.setText(_translate("MainWindow", "Введите URL №1"))
        self.label_2.setText(_translate("MainWindow", "Введите URL №2"))
        self.label_3.setText(_translate("MainWindow", "Введите URL №3"))
        self.pushButton.setText(_translate("MainWindow", "Start downloading!"))

