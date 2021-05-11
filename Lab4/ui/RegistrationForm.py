from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from LibraryModule import User

class RegWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 0);")
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
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 321, 61))
        self.pushButton.clicked.connect(self.register_user)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton.setText("Зарегистрироваться")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def register_user(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not login =='' and not password =='':
            try:
                user = User(login, password)
                user.add_to_db()
                self.display_success()
                self.window.close()
            except:
                self.display_failure()
        else:
            self.display_failure()
    def display_success(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Пользователь зарегистирирован")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#00aa00;\">Регистрация</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите логин..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите пароль..."))

