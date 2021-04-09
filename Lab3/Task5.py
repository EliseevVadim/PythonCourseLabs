import sys
from PyQt5.QtWidgets import *
from qt.Task5Window import Ui_MainWindow
from classes.stringTools import StringFormatter

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.formatText)
        self.ui.checkBox_4.clicked.connect(self.box_click)
    def formatText(self):
        formatter=StringFormatter(self.ui.lineEdit.text())
        if self.ui.checkBox.isChecked():
            formatter.delete_short_words(self.ui.spinBox.value())
        if self.ui.checkBox_2.isChecked():
            formatter.replace_digits_by_stars()
        if self.ui.checkBox_4.isChecked():
            if self.ui.radioButton.isChecked():
                formatter.sort_by_size()
            else:
                formatter.sort_in_lexis_order()
        if self.ui.checkBox_3.isChecked():
            formatter.insert_spaces()
        self.ui.lineEdit_2.setText(formatter.line)
    def box_click(self):
        if self.ui.checkBox_4.isChecked():
            self.ui.radioButton.setChecked(True)
            self.ui.radioButton.setDisabled(False)
            self.ui.radioButton_2.setDisabled(False)
        else:
            self.ui.radioButton.setDisabled(True)
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton_2.setDisabled(True)
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))    