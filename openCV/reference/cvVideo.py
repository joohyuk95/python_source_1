import cv2
import numpy as np
from PyQt5 import QtGui     # openCV 이미지 Qt 이미지로 변환
from cvFilter import Filter # 필터 모듈 사용
from cvFlip import Flip

# self가 붙으면 class 내의 멤버함수 또는  멤버변수를 의미
class Video:    # v = Video(), v.updateFrame(), 
    def __init__(self, device=0):
        self.cap = cv2.VideoCapture(device)             # 노트북 카메라 캡쳐
        retval, self.frame = self.cap.read()            # 캡쳐 읽어들임
        self.filter = Filter()                          # 필터 인스턴스 생성
        self.flip = Flip()

    def updateFrame(self):
        retval, self.frame = self.cap.read()            # 다시 원본 읽어들임
        self.frame = self.flip.applyFlip(self.frame)
        self.filteredImg = self.filter.applyFilter(self.frame)  # 원본 필터 씌워서 저장
        result = self.convertCVImgToQtPixmap(self.filteredImg)  # 필터 씌운 이미지 Qt로 변환
        return result   # 이미지 반환

    def convertCVImgToQtPixmap(self, cvImg):
        if type(cvImg[0][0]) == np.uint8:
            h, w = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w , QtGui.QImage.Format_Grayscale8)
        else:
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
            h, w, c = cvImg.shape
            qImg = QtGui.QImage(cvImg.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)

        return pixmap

    def saveImg(self):
        cv2.imwrite("C:\\Users\\user\\Desktop\\image.jpg", self.filteredImg)
        print(234)

    def close(self):
        if self.cap.isOpened():
            self.cap.release()

        print("Finish Capture")
        