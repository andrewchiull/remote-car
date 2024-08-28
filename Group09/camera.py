import time
from PyQt5.QtCore import QObject
from PyQt5 import QtCore
import cv2
import numpy as np

class Camera(QObject):
    picdone = QtCore.pyqtSignal(np.ndarray)
    fail = QtCore.pyqtSignal(bool)

    def run(self):
        self.vid = cv2.VideoCapture(0)

        while True:
            ret, frame = self.vid.read()
            time.sleep(1/5)
            self.picdone.emit(frame)

            if ret == False:
                self.fail.emit(False)
