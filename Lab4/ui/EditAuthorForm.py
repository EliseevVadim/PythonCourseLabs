from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ORLibraryModule import Author


class EditAuthorWindow(object):
    def __init__(self, parent, author):
        self.__par = parent
        self.__author = author
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 333)
        MainWindow.setMinimumSize(QtCore.QSize(600, 333))
        MainWindow.setMaximumSize(QtCore.QSize(600, 333))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(104, 0, 391, 51))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 270, 231, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update)
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
        self.load()
        self.main = MainWindow
        MainWindow.setCentralWidget(self.centralwidget)        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def load(self):
        try:
            self.lineEdit.setText(self.__author.name)
            self.lineEdit_2.setText(self.__author.country)
            self.lineEdit_3.setText(self.__author.years)
        except:
            pass
    def update(self):
       try:
            self.__author.name = self.lineEdit.text()
            self.__author.country = self.lineEdit_2.text()
            self.__author.years = self.lineEdit_3.text()
            self.__par.session.commit()
            self.__par.update_view()
            QMessageBox.information(None, 'Успех', 'Данные обновлены')
            self.main.close()
       except:
            pass
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Редактировать информацию об авторе"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.label_2.setText(_translate("MainWindow", "Введите имя автора"))
        self.label_3.setText(_translate("MainWindow", "Введите страну автора"))
        self.label_4.setText(_translate("MainWindow", "Введите годы жизни автора"))

