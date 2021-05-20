import sys
from PyQt5.QtWidgets import *
from ui.DownloadWindow import Ui_MainWindow

class MyForm(QMainWindow):
     def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
         







if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))      
