from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 700)
        self.screen = QtWidgets.QLabel(Form)
        self.screen.setGeometry(QtCore.QRect(100, 20, 600, 450))
        self.screen.setStyleSheet("background-color: black")
        self.screen.setObjectName("screen")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530-170, 530, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(530-170, 600, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(600-170, 600, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(460-170, 600, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(350-170-100, 600, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(670-170+100, 600, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "前"))
        self.pushButton_2.setText(_translate("Form", "後"))
        self.pushButton_3.setText(_translate("Form", "右"))
        self.pushButton_4.setText(_translate("Form", "左"))
        self.pushButton_5.setText(_translate("Form", "放"))
        self.pushButton_6.setText(_translate("Form", "抓"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
