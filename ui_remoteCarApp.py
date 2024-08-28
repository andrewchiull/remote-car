# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/andrewchiu/Documents/NTU/111-1/5_Mechatronics/FinalProject/remoteCarApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color:#333")
        self.pushButton_forward = QtWidgets.QPushButton(Form)
        self.pushButton_forward.setGeometry(QtCore.QRect(530, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_forward.setFont(font)
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.pushButton_backward = QtWidgets.QPushButton(Form)
        self.pushButton_backward.setGeometry(QtCore.QRect(530, 500, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_backward.setFont(font)
        self.pushButton_backward.setObjectName("pushButton_backward")
        self.pushButton_right = QtWidgets.QPushButton(Form)
        self.pushButton_right.setGeometry(QtCore.QRect(600, 500, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_right.setFont(font)
        self.pushButton_right.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_left = QtWidgets.QPushButton(Form)
        self.pushButton_left.setGeometry(QtCore.QRect(460, 500, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_left.setFont(font)
        self.pushButton_left.setObjectName("pushButton_left")
        self.pushButton_open = QtWidgets.QPushButton(Form)
        self.pushButton_open.setGeometry(QtCore.QRect(350, 430, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(670, 430, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.logging = QtWidgets.QWidget(Form)
        self.logging.setGeometry(QtCore.QRect(30, 20, 251, 391))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.logging.setFont(font)
        self.logging.setStyleSheet("background-color:#222")
        self.logging.setObjectName("logging")
        self.pushButton_sendCommand = QtWidgets.QPushButton(Form)
        self.pushButton_sendCommand.setGeometry(QtCore.QRect(150, 540, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sendCommand.setFont(font)
        self.pushButton_sendCommand.setObjectName("pushButton_sendCommand")
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(290, 20, 20, 391))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 500, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:#222")
        self.lineEdit.setObjectName("lineEdit")
        self.screen = QtWidgets.QLabel(Form)
        self.screen.setGeometry(QtCore.QRect(340, 20, 400, 300))
        self.screen.setStyleSheet("background-color: gray")
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName("screen")
        self.pushButton_detectColor = QtWidgets.QPushButton(Form)
        self.pushButton_detectColor.setGeometry(QtCore.QRect(590, 330, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_detectColor.setFont(font)
        self.pushButton_detectColor.setObjectName("pushButton_detectColor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_forward.setText(_translate("Form", "^"))
        self.pushButton_backward.setText(_translate("Form", "v"))
        self.pushButton_right.setText(_translate("Form", ">"))
        self.pushButton_left.setText(_translate("Form", "<"))
        self.pushButton_open.setText(_translate("Form", "OPEN"))
        self.pushButton_close.setText(_translate("Form", "CLOSE"))
        self.pushButton_sendCommand.setText(_translate("Form", "SEND COMMAND"))
        self.screen.setText(_translate("Form", "webcam"))
        self.pushButton_detectColor.setText(_translate("Form", "DETECT COLOR"))