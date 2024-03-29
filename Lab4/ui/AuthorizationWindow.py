from PyQt5 import QtCore, QtGui, QtWidgets
from ui.RegistrationForm import RegWindow
from ui.MainForm import MainView
import sqlite3
import hashlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 0);")
        self.main = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(197, 20, 206, 41))
        self.label.setStyleSheet("background-color: rgba(255, 85, 0, 0);\n"
"font: 75 32pt \"Arial\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 291, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 291, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Arial\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 321, 61))
        self.pushButton.clicked.connect(self.authorize)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton.setText("Войти")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 300, 321, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton_2.setText("Регистрация")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.clicked.connect(self.open_registration)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def open_registration(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = RegWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def authorize(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not login == '' and not password == '':
            hashedPassword = hashlib.md5(password.encode())
            password = str(hashedPassword.hexdigest())
            attempt = (login, password)
            path = r'db/library.db'
            db = sqlite3.connect(path)
            with db:
                cursor = db.cursor()
                cursor.execute('SELECT Login, Password FROM Users')
                users = cursor.fetchall()
                if attempt in users:
                    self.display_success()
                    self.next_window = QtWidgets.QMainWindow()
                    self.ui = MainView()
                    self.ui.setupUi(self.next_window)
                    self.next_window.show()
                    self.main.close()                    
                else:
                    self.display_failure()
        else:
            self.display_failure()
    def display_success(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Вы успешно вошли")
        msg.setWindowTitle("Информация")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
        msg.exec_()
    def display_failure(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Проверьте введенные данные")
        msg.setWindowTitle("Ошибка")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
        msg.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#00aa00;\">Авторизация</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите логин..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите пароль..."))

