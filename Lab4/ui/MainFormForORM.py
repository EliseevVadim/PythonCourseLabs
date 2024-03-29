from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.AddAuthorFormForORM import AddAuthorWindow
from ui.EditBookForm import EditBookWindow
from ui.AddBookFormForORM import AddBookWindow
from ui.EditAuthorForm import EditAuthorWindow
from ORLibraryModule import create_tables
from ORLibraryModule import Author
from ORLibraryModule import Book
import sqlalchemy
from sqlalchemy.orm import sessionmaker

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.authors_idx = 0
        self.books_idx = 0
        self.path = r'db/ORLibrary.db'
        self.custom_view_authors = True
        self.custom_view_books = True
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.engine = sqlalchemy.create_engine('sqlite:///' + self.path, echo = False)
        Session = sessionmaker(bind = self.engine)
        self.session = Session()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 22, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 800, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clicked.connect(self.get_authors_idx)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 120, 22))
        self.pushButton_6.clicked.connect(self.create_all)
        self.pushButton_6.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 360, 181, 41))
        self.pushButton_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.addAuthorButton = QtWidgets.QPushButton(self.tab)
        self.addAuthorButton.clicked.connect(self.open_adding_author)
        self.addAuthorButton.setGeometry(QtCore.QRect(20, 360, 181, 41))
        self.addAuthorButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.addAuthorButton.setObjectName("addAuthorButton")
        self.removeAuthorButton = QtWidgets.QPushButton(self.tab)
        self.removeAuthorButton.setGeometry(QtCore.QRect(590, 360, 181, 41))
        self.removeAuthorButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.removeAuthorButton.setObjectName("removeAuthorButton")
        self.removeAuthorButton.clicked.connect(self.remove_author)
        self.searchAuthorsButton = QtWidgets.QPushButton(self.tab)
        self.searchAuthorsButton.setGeometry(QtCore.QRect(220, 460, 291, 41))
        self.searchAuthorsButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.searchAuthorsButton.setObjectName("searchAuthorsuton")
        self.searchAuthorsButton.clicked.connect(self.filter_authors)
        self.booksNumField = QtWidgets.QLineEdit(self.tab)
        self.booksNumField.setGeometry(QtCore.QRect(520, 470, 31, 20))
        self.booksNumField.setObjectName("booksNumField")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(560, 470, 31, 21))
        self.label_3.setObjectName("label_3")
        self.editAuthorButton = QtWidgets.QPushButton(self.tab)
        self.editAuthorButton.setGeometry(QtCore.QRect(310, 360, 181, 41))
        self.editAuthorButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.editAuthorButton.setObjectName("editAuthorButton")
        self.editAuthorButton.clicked.connect(self.open_editing_author)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 800, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.clicked.connect(self.get_books_idx)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.addBookButton = QtWidgets.QPushButton(self.tab_2)
        self.addBookButton.setGeometry(QtCore.QRect(20, 360, 181, 41))
        self.addBookButton.clicked.connect(self.open_adding_book)
        self.addBookButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.addBookButton.setObjectName("addBookButton")
        self.removeBookButton = QtWidgets.QPushButton(self.tab_2)
        self.removeBookButton.setGeometry(QtCore.QRect(590, 360, 181, 41))
        self.removeBookButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.removeBookButton.setObjectName("removeBookButton")
        self.removeBookButton.clicked.connect(self.remove_book)
        self.searchRussianBooks = QtWidgets.QPushButton(self.tab_2)
        self.searchRussianBooks.setGeometry(QtCore.QRect(20, 460, 271, 41))
        self.searchRussianBooks.setStyleSheet("")
        self.searchRussianBooks.clicked.connect(self.filter_russian)
        self.searchRussianBooks.setObjectName("searchRussianBooks")
        self.searchBooksByPages = QtWidgets.QPushButton(self.tab_2)
        self.searchBooksByPages.setGeometry(QtCore.QRect(400, 460, 291, 41))
        self.searchBooksByPages.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.searchBooksByPages.setObjectName("searchBooksByPages")
        self.searchBooksByPages.clicked.connect(self.filter_by_pages)
        self.pagesNumField = QtWidgets.QLineEdit(self.tab_2)
        self.pagesNumField.setGeometry(QtCore.QRect(690, 470, 31, 20))
        self.pagesNumField.setObjectName("pagesNumField")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(730, 470, 47, 21))
        self.label.setObjectName("label")
        self.editBookButton = QtWidgets.QPushButton(self.tab_2)
        self.editBookButton.clicked.connect(self.open_editing_book)
        self.editBookButton.setGeometry(QtCore.QRect(310, 360, 181, 41))
        self.editBookButton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.editBookButton.setObjectName("editBookButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.main = MainWindow
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_authors()
        self.load_books()        
    def create_all(self):
        create_tables()
        QMessageBox.information(None, 'Успех', 'Таблица создана')      
    def load_authors(self):
        authors = [(author.id, author.name, author.country, author.years) for author in self.session.query(Author)]        
        self.tableWidget.setRowCount(len(authors))
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(str(authors[i][j]))
                self.tableWidget.setItem(i, j, item)
    def load_books(self):
        books = [(book.id, book.authors_id, book.name, book.pages, book.publisher, book.publishing_year) for book in self.session.query(Book)]   
        self.tableWidget_2.setRowCount(len(books))
        for i in range(self.tableWidget_2.rowCount()):
            for j in range(self.tableWidget_2.columnCount()):
                item = QTableWidgetItem(str(books[i][j]))
                self.tableWidget_2.setItem(i, j, item)   
    def update_view(self):
        self.tableWidget.clearContents()
        self.load_authors()
    def update_view_for_books(self):
        self.tableWidget_2.clearContents()
        self.load_books()
    def open_editing_author(self):
        self.edit_author = QtWidgets.QMainWindow()
        author = self.session.query(Author).get(self.authors_idx)
        self.ui = EditAuthorWindow(self, author)
        self.ui.setupUi(self.edit_author)
        self.edit_author.show()
    def open_editing_book(self):
        self.edit_book = QtWidgets.QMainWindow()
        book = self.session.query(Book).get(self.books_idx)
        self.ui = EditBookWindow(self, book)
        self.ui.setupUi(self.edit_book)
        self.edit_book.show()
    def open_adding_author(self):
        self.add_author = QtWidgets.QMainWindow()
        self.ui = AddAuthorWindow(self)
        self.ui.setupUi(self.add_author)
        self.add_author.show()    
    def fill_books_with_list(self, source):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(source))
        for i in range(self.tableWidget_2.rowCount()):
            for j in range(self.tableWidget_2.columnCount()):
                item = QTableWidgetItem(str(source[i][j]))
                self.tableWidget_2.setItem(i, j, item)
    def fill_authors_with_list(self, source):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(source))
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(str(source[i][j]))
                self.tableWidget.setItem(i, j, item)
    def open_adding_book(self):
        self.add_book = QtWidgets.QMainWindow()
        self.ui = AddBookWindow(self)
        self.ui.setupUi(self.add_book)
        self.add_book.show()
    def get_books_idx(self):
        try:
            self.books_idx = int(self.tableWidget_2.currentItem().text())
        except:
            pass
    def remove_book(self):
        try:
            book = self.session.query(Book).get(self.books_idx)
            self.session.delete(book)
            self.session.commit()
            QMessageBox.information(None, 'Успех', 'Запись удалена')
            self.load_books()
        except:
            pass
    def get_authors_idx(self):
        try:
            self.authors_idx = int(self.tableWidget.currentItem().text())
        except:
            pass
    def remove_author(self):
        try:
            author = self.session.query(Author).get(self.authors_idx)
            self.session.delete(author)
            self.session.commit()
            QMessageBox.information(None, 'Успех', 'Запись удалена')
            self.load_authors()
            self.load_books()
        except:
            pass
    def filter_by_pages(self):
        try:
            if self.custom_view_books:
                required_pages = int(self.pagesNumField.text())
                books = [(book.id, book.authors_id, book.name, book.pages, book.publisher, book.publishing_year) for book in self.session.query(Book) if book.pages > required_pages]
                self.fill_books_with_list(books)
                self.searchBooksByPages.setText('Вернуться обратно')
            else:
                self.load_books()
                self.searchBooksByPages.setText('Отобразить книги, которые больше')
            self.custom_view_books = not self.custom_view_books
        except:
            pass
    def filter_russian(self):
        try:
            if self.custom_view_books:
                rus_authors_ids = [author.id for author in self.session.query(Author) if author.country == 'Russia' or author.country == 'Россия']                
                books = [(book.id, book.authors_id, book.name, book.pages, book.publisher, book.publishing_year) for book in self.session.query(Book) if book.authors_id in rus_authors_ids]
                self.fill_books_with_list(books)
                self.searchRussianBooks.setText('Вернуться обратно')
            else:
                self.load_books()
                self.searchRussianBooks.setText('Отобразить книги, написанные авторми из России') 
            self.custom_view_books = not self.custom_view_books
        except:
            pass
    def filter_authors(self):
        try:
            if self.custom_view_authors:               
                b_ids = [book.authors_id for book in self.session.query(Book)]
                authors = [(author.id, author.name, author.country, author.years) for author in self.session.query(Author)]
                dictionary = {author: b_ids.count(author[0]) for author in authors}
                result = [author for author in dictionary.keys() if dictionary[author]>int(self.booksNumField.text())]
                self.fill_authors_with_list(result)
                self.searchAuthorsButton.setText('Вернуться обратно')
            else:
                self.load_authors()
                self.searchAuthorsButton.setText('Отобразить авторов, у которых более')
            self.custom_view_authors = not self.custom_view_authors
        except:
            pass
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Годы жизни"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id автора"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество страниц"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Издательство"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Год издания"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_6.setText(_translate("MainWindow", "Создать таблицы"))
        self.addAuthorButton.setText(_translate("MainWindow", "Добавить"))
        self.removeAuthorButton.setText(_translate("MainWindow", "Удалить"))
        self.searchAuthorsButton.setText(_translate("MainWindow", "Отобразить авторов, у которых более"))
        self.label_3.setText(_translate("MainWindow", "книг"))
        self.editAuthorButton.setText(_translate("MainWindow", "Редактировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Авторы"))
        self.addBookButton.setText(_translate("MainWindow", "Добавить"))
        self.removeBookButton.setText(_translate("MainWindow", "Удалить"))
        self.searchRussianBooks.setText(_translate("MainWindow", "Отобразить книги, написанные авторми из России"))
        self.searchBooksByPages.setText(_translate("MainWindow", "Отобразить книги, которые больше"))
        self.label.setText(_translate("MainWindow", "страниц"))
        self.editBookButton.setText(_translate("MainWindow", "Редактировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Книги"))

