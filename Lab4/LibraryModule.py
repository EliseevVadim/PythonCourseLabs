import hashlib
import sqlite3
import abc

class IRecordable:
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def add_to_db(self):
        raise NotImplementedError

class User(IRecordable):
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__db = r'db/library.db'
    def add_to_db(self):
        db = sqlite3.connect(self.__db)
        with db:
            cursor = db.cursor()
            hashedPassword = hashlib.md5(self.__password.encode())
            self.__password = str(hashedPassword.hexdigest())
            cursor.execute('INSERT INTO Users(Login, Password) Values(?, ?)', 
                           (self.__login, self.__password))
            db.commit()



class Author(IRecordable):
    def __init__(self, name, country, life_years):
        self.__name = name
        self.__country = country
        self.__life_years = life_years
    def add_to_db(self):
        if self.__name == '' or self.__country == '' or self.__life_years == '':
            raise Exception
        self.__db = r'db/library.db'
        db = sqlite3.connect(self.__db)
        with db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO Authors(name, country, [life-years]) Values(?, ?, ?)',
                           (self.__name, self.__country, self.__life_years))
            db.commit()

class Book(IRecordable):
    def __init__(self, name, pages, publisher, publishing_year, authors_id):
        self.__name = name
        self.__pages = pages
        self.__publisher = publisher
        self.__publishing_year = publishing_year
        self.__authors_id = authors_id
    def add_to_db(self):
        if self.__name == '' or self.__pages == '' or self.__publisher == '' or self.__publishing_year is None or self.__authors_id is None or self.__pages < 1 or self.__publishing_year < 0:
            raise Exception
        self.__db = r'db/library.db'
        db = sqlite3.connect(self.__db)
        with db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO Books(authors_id, name, pages, publisher, [publishing_year]) Values(?, ?, ?, ?, ?)',
                           (self.__authors_id, self.__name, self.__pages, self.__publisher, self.__publishing_year))
            db.commit()