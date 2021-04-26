import sys
import sqlite3
from PyQt5.QtWidgets import *
from ui.AuthorizationWindow import Ui_MainWindow



class AuthorizationForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.test)
    def test(self):
        dbname = r'db/DataBase.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()             
        # perfID = input('Performer ID: ')
        # albumname = input('Album name: ')
        # albumyear = int(input('Album year: '))
        # cursor.execute('INSERT INTO albums VALUES(NULL, ?, ?, ?)',
        #                    (albumname, albumyear, perfID))
        # print('done')
        cursor.execute('SELECT id, name from albums')
        performers = cursor.fetchall()
        print(performers)
        
        db.close()
        









if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AuthorizationForm()
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))  