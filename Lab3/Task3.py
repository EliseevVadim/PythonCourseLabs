import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt.Task3Window import Ui_MainWindow
import re
import datetime
import os

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lines=[]
        self.needToClear=False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().addPermanentWidget(self.ui.leftLabel, 6)
        self.statusBar().addPermanentWidget(self.ui.rightLabel, 4)
        self.ui.action.triggered.connect(self.find_matches)
        self.ui.action_2.triggered.connect(self.export)
        self.ui.action_3.triggered.connect(self.add_to_log)
        self.ui.action_4.triggered.connect(self.display_log)       
        m = QStandardItemModel(self)
        self.ui.listView.setModel(m)
        if not os.path.exists('script18.log'):
            message = QMessageBox.information(self, 'PyQt5 message', 'Файл лога не найден. Файл будет создан автоматически', QMessageBox.Ok)
            open(r'script18.log', 'wt').close()
    def find_matches(self):
        if self.needToClear:
            self.ui.listView.model().removeRows(0, self.ui.listView.model().rowCount())
        fileName = QFileDialog.getOpenFileName(self,"Choose a file", "","All Files (*);")[0]
        with open(fileName, 'r') as file:
            lines=file.readlines()
            pattern=re.compile(r'\(\b\d{3}\)\d{3}\-?\d{2}\-?\d{2}\b')  
            timeLine = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            self.ui.listView.model().appendRow(QStandardItem('Файл {} был обработан {}:\n'.format(fileName, timeLine)))
            self.lines.append('Файл {} был обработан {}:\n'.format(fileName, timeLine))
            for i in range(len(lines)):
                for match in pattern.finditer(lines[i]):    
                    self.ui.listView.model().appendRow(QStandardItem('Строка {}, позиция {} : найдено \'{}\''.format(i+1, match.start()+1, match.group())))
                    self.lines.append('Строка {}, позиция {} : найдено \'{}\''.format(i+1, match.start()+1, match.group()))
            self.ui.rightLabel.setText('{:,}'.format(os.path.getsize(fileName)).replace(',', ' ') + ' байт')
            self.ui.leftLabel.setText('Обработан файл {}'.format(fileName))
    def export(self):
         fileName = QFileDialog.getOpenFileName(self, "Choose a file", "","All Files (*);")[0]
         with open(fileName, 'w') as file:
             for line in self.lines:
                 file.write(line + '\n')
    def add_to_log(self):
        with open(r'script18.log', 'a') as file:
            for line in self.lines:
                 file.write(line + '\n')
    def display_log(self):
        result = QMessageBox.question(self, 'Подтверждение', 'Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result==QMessageBox.Yes:
            self.lines.clear()
            with open(r'script18.log', 'r') as file:
                self.lines = [line.rstrip() for line in file.readlines()]
                self.ui.listView.model().removeRows(0, self.ui.listView.model().rowCount())
                for line in self.lines:
                    self.ui.listView.model().appendRow(QStandardItem(line))
                self.lines.clear()
                self.ui.leftLabel.setText('Открыт лог')
                self.ui.rightLabel.setText('{:,}'.format(os.path.getsize(r'script18.log')).replace(',', ' ') + ' байт')
                self.needToClear=True
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    try:
        sys.exit(app.exec_())
    except SystemExit as se:
        print('Program has exited with code {}'.format(se))    