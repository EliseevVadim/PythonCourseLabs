from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import *
import sqlite3
import json
from dicttoxml import dicttoxml
from ui.AddAuthorForm import AddAuthorWindow
from ui.AddBookForm import AddBookWindow

class MainView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.authorsWidget = QtWidgets.QTableWidget(self.tab)
        self.authorsWidget.setGeometry(QtCore.QRect(10, 10, 771, 441))
        self.authorsWidget.setObjectName("authorsWidget")
        self.authorsWidget.clicked.connect(self.get_idx)
        self.authorsWidget.setColumnCount(3)
        self.authorsWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 490, 221, 41))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_adding_author)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 490, 281, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.save_to_file)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.authorsWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.authorsWidget_2.setGeometry(QtCore.QRect(10, 10, 771, 441))
        self.authorsWidget_2.setObjectName("authorsWidget_2")
        self.authorsWidget_2.setColumnCount(5)
        self.authorsWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.authorsWidget_2.setHorizontalHeaderItem(4, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 480, 471, 51))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_adding_book)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.main = MainWindow
        self.load()
        self.load_books()
    
    def load(self):
        path = r'db/library.db'
        db = sqlite3.connect(path)
        with db:
            cursor = db.cursor()
            result = cursor.execute('SELECT name, country, [life-years] FROM Authors')
            self.authorsWidget.setRowCount(0)
            for row_num, row_dat in enumerate(result):
                self.authorsWidget.insertRow(row_num)
                for col_num, data in enumerate(row_dat):
                    self.authorsWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
    
    def load_books(self):
        path = r'db/library.db'
        db = sqlite3.connect(path)
        with db:
            cursor = db.cursor()
            result = cursor.execute('SELECT authors_id, name, pages, publisher, [publishing_year]  FROM Books')
            self.authorsWidget_2.setRowCount(0)
            for row_num, row_dat in enumerate(result):
                self.authorsWidget_2.insertRow(row_num)
                for col_num, data in enumerate(row_dat):
                    self.authorsWidget_2.setItem(row_num, col_num, QTableWidgetItem(str(data)))
                    
    def open_adding_author(self):
        self.add_author = QtWidgets.QMainWindow()
        self.ui = AddAuthorWindow(self)
        self.ui.setupUi(self.add_author)
        self.add_author.show()

    def update_view(self):
        self.authorsWidget.clearContents()
        self.load()
        
    def open_adding_book(self):
        self.add_book = QtWidgets.QMainWindow()
        self.ui = AddBookWindow(self)
        self.ui.setupUi(self.add_book)
        self.add_book.show()
    def update_view_for_books(self):
        self.authorsWidget_2.clearContents()
        self.load_books()
    def get_idx(self):
        self.__idx = self.authorsWidget.currentRow()
    def save_to_file(self):        
        path = r'db/library.db'
        db = sqlite3.connect(path)
        with db:
            for_file = {}
            authors = []
            cursor = db.cursor()
            result = cursor.execute('SELECT name, country, [life-years] FROM Authors')
            authors = result.fetchall()
            current = authors[self.authorsWidget.currentRow()]
            for_file['name'] = current[0]
            for_file['country'] = current[1]
            for_file['years'] = current[2]
            path = QFileDialog.getOpenFileName(self.main, "Выберите файл", "", "XML files (*.xml);;JSON files (*.json)")[0]
            with open(path, 'w') as f:
                if path.endswith('.json'):
                    json.dump(for_file, f)
                elif path.endswith('.xml'):
                    xml = dicttoxml(for_file)
                    f.write(xml.decode())
            QMessageBox.information(self.main, 'title', 'done')
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        item = self.authorsWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.authorsWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.authorsWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Годы жизни"))
        self.pushButton.setText(_translate("MainWindow", "Добавить автора"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить информацию об авторе"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Авторы"))
        item = self.authorsWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id автора"))
        item = self.authorsWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.authorsWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Количество страниц"))
        item = self.authorsWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Издательство"))
        item = self.authorsWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Год издания"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить книгу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Книги"))

