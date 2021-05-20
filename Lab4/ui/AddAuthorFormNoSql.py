from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
from bs4 import BeautifulSoup
import pymongo

class AddAuthorWindow(object):
    def __init__(self, parent):
        self.__par = parent
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 333)
        MainWindow.setMinimumSize(QtCore.QSize(600, 333))
        MainWindow.setMaximumSize(QtCore.QSize(600, 333))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(214, 0, 171, 51))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 231, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_record)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 270, 231, 51))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.parse)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 21))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 181, 21))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 211, 21))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 170, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.main = MainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_record(self):
        try:            
            name = self.lineEdit.text()
            country = self.lineEdit_2.text()
            years = self.lineEdit_3.text()
            self.__par.db['authors'].insert_one({'name':name, 'country':country, 'years':years})
            QMessageBox.information(self.main, 'Успех', 'Автор успешно добавлен')
            self.__par.update_view()
            self.main.close()            
        except:
            QMessageBox.critical(self.main, 'Ошибка', 'Данные введены неверно')
    def parse(self):
        path = QFileDialog.getOpenFileName(self.main, "Выберите файл", "", "XML files (*.xml);;JSON files (*.json)")[0]
        if path.endswith('.json'):
            try:
                with open(path, 'r') as f:
                    data = json.load(f)
                    self.lineEdit.setText(data['name'])
                    self.lineEdit_2.setText(data['country'])
                    self.lineEdit_3.setText(data['years'])
            except:
                pass
        if path.endswith('.xml'):
            try:
               with open(path, 'r') as file:
                   xml = file.read()
                   soup = BeautifulSoup(xml, 'lxml')
                   self.lineEdit.setText(soup.findAll("name")[0].text)
                   self.lineEdit_2.setText(soup.findAll("country")[0].text)
                   self.lineEdit_3.setText(soup.findAll("years")[0].text)
            except:
                pass
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно добавления автора"))
        self.label.setText(_translate("MainWindow", "Добавить автора"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Распарсить файл"))
        self.label_2.setText(_translate("MainWindow", "Введите имя автора"))
        self.label_3.setText(_translate("MainWindow", "Введите страну автора"))
        self.label_4.setText(_translate("MainWindow", "Введите годы жизни автора"))

