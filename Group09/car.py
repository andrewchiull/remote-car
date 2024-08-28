from car_ui import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow
from camera import Camera
import serial

import sys
import cv2

class Car(QMainWindow, Ui_Form):
    def __init__(self,parent = None):
        QMainWindow.__init__(self, parent = parent)
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.setFocus()
        self.startThread()

        self.pushButton_3.setShortcut(QtGui.QKeySequence(Qt.Key_D))
        self.pushButton_3.clicked.connect(self.right)

        self.pushButton.setShortcut(QtGui.QKeySequence(Qt.Key_W))
        self.pushButton.clicked.connect(self.up)

        self.pushButton_2.setShortcut(QtGui.QKeySequence(Qt.Key_S))
        self.pushButton_2.clicked.connect(self.down)

        self.pushButton_4.setShortcut(QtGui.QKeySequence(Qt.Key_A))
        self.pushButton_4.clicked.connect(self.left)

        self.pushButton_5.setShortcut(QtGui.QKeySequence(Qt.Key_Q))
        self.pushButton_5.clicked.connect(self.open)

        self.pushButton_6.setShortcut(QtGui.QKeySequence(Qt.Key_E))
        self.pushButton_6.clicked.connect(self.close)

    def open(self):
        print("放")

    def close(self):
        print("抓")

    def left(self):
        print("左")

    def down(self):
        print("後")

    def up(self):
        self.ser.write(b'hello')
        print("前")

    def right(self):
        print("右")

    def img2pyqt(self,img,label):
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def showImage(self, image):
        self.screen.setPixmap(self.img2pyqt(image,self.screen))

    def failConnect(self, condition):
        if condition == False:
            bg = cv2.imread('bg.jpg')
            self.screen.setPixmap(self.img2pyqt(bg,self.screen))
            print('Failed to connect to Camera ....')

    def startThread(self):

        self.thread = QtCore.QThread()
        self.worker = Camera()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.picdone.connect(self.showImage)
        self.worker.fail.connect(self.failConnect)

        self.thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Car()
    ui.show()
    sys.exit(app.exec_())

