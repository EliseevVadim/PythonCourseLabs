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




















# import matplotlib.pyplot as plt
# import requests
# import threading
# import time
# from datetime import datetime

# def first_download():
#     first_start = datetime.now()
#     r = requests.get('https://github.com/ar1st0crat/PythonCourse/raw/master/labs/Lab04%20-%20Python%20libraries.pdf', stream=True)   
#     print(r.headers.get('content-length'))
#     # with open('data/1.pdf', 'wb') as f:
#     #     for chunk in r.iter_content(chunk_size=4096):
#     #         if chunk:
#     #             f.write(chunk)
#     #             print(f'Downloaded 4096 bytes')
#     first_finish = datetime.now()
# def second_download():
#     second_start = datetime.now()
#     r1 = requests.get('https://github.com/ar1st0crat/PythonCourse/raw/master/labs/Lab03%20-%20Python%20OOP%20and%20GUI.pdf', stream = True)    
#     # with open('data/2.pdf', 'wb') as f1:
#     #     for chunk1 in r1.iter_content(chunk_size=4096):
#     #         if chunk1:
#     #             f1.write(chunk1)
#     #             print('Second Downloaded 4096 bytes')
#     second_finish = datetime.now()
#     print(r1.headers.get('content-length'))
# def third_download():
#     third_start = datetime.now()
#     r2 = requests.get('https://github.com/ar1st0crat/PythonCourse/raw/master/labs/Lab02%20-%20Python%20files%20and%20OS.pdf', stream = True)    
#     # with open('data/3.pdf', 'wb') as f2:
#     #     for chunk2 in r2.iter_content(chunk_size=4096):
#     #         if chunk2:
#     #             f2.write(chunk2)
#     #             print('Third Downloaded 4096 bytes')
#     third_finish = datetime.now()
#     print(r2.headers.get('content-length'))
                


# # t1 = threading.Thread(target=first_download)    
# # t2 = threading.Thread(target=second_download)
# # t3 = threading.Thread(target=third_download)
# # t1.start()
# # t2.start()
# # t3.start()  
# # t1.join()
# # t2.join()
# # t3.join()  
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
# plt.subplot(121)
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.subplot(122)
# plt.bar(labels, sizes)
# plt.grid()
# # cfm.window.activateWindow()
# # cfm.window.raise_()
# #first_download('https://github.com/ar1st0crat/PythonCourse/raw/master/labs/Lab04%20-%20Python%20libraries.pdf')