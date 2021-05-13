from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ORLibraryModule import Book
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ORLibraryModule import Author
from ORLibraryModule import Book

class AddBookWindow(object):
    def __init__(self, parent):
        self.__parent = parent
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 412)
        self.path = r'db/ORLibrary.db'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.engine = sqlalchemy.create_engine('sqlite:///' + self.path, echo = False)
        Session = sessionmaker(bind = self.engine)
        self.session = Session()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(214, 0, 171, 51))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 181, 21))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.nameField = QtWidgets.QLineEdit(self.centralwidget)
        self.nameField.setGeometry(QtCore.QRect(210, 70, 211, 20))
        self.nameField.setObjectName("nameField")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 221, 21))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pagesField = QtWidgets.QLineEdit(self.centralwidget)
        self.pagesField.setGeometry(QtCore.QRect(250, 120, 211, 20))
        self.pagesField.setObjectName("pagesField")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 241, 21))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.publishierField = QtWidgets.QLineEdit(self.centralwidget)
        self.publishierField.setGeometry(QtCore.QRect(270, 170, 211, 20))
        self.publishierField.setObjectName("publishierField")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 161, 21))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.yearField = QtWidgets.QLineEdit(self.centralwidget)
        self.yearField.setGeometry(QtCore.QRect(190, 220, 211, 20))
        self.yearField.setObjectName("yearField")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 161, 21))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 321, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_record)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 270, 69, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.main = MainWindow
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fill_combobox()
    
    def fill_combobox(self):
        try:
            self.comboBox.clear()
            ids = [author.id for author in self.session.query(Author)]
            for id in ids:
                self.comboBox.addItem(str(id))
        except:
            pass
                
    def add_record(self):
        try:
            book = Book(authors_id = int(self.comboBox.currentText()), name = self.nameField.text(), pages = int(self.pagesField.text()), publisher = self.publishierField.text(), publishing_year = int(self.yearField.text()))
            engine = sqlalchemy.create_engine('sqlite:///db/ORLibrary.db', echo = False)
            Session = sessionmaker(bind = engine)
            session = Session()
            session.add(book)
            session.commit()
            QMessageBox.information(self.main, 'Успех', 'Книга успешно добавлена')
            self.__parent.update_view_for_books()
            session.close()
            self.main.close()
        except:
            QMessageBox.critical(self.main, 'Ошибка', 'Данные введены неверно')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно добавления книги"))
        self.label.setText(_translate("MainWindow", "Добавить книгу"))
        self.label_2.setText(_translate("MainWindow", "Введите название книги"))
        self.label_3.setText(_translate("MainWindow", "Введите количество страниц"))
        self.label_4.setText(_translate("MainWindow", "Введите название издательства"))
        self.label_5.setText(_translate("MainWindow", "Введите год издания"))
        self.label_6.setText(_translate("MainWindow", "Выберите id автора"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))

