import cv2
import threading
import time
import sys
from PyQtVideo import MyVideoUI
from cvVideo import Video
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)      # core 실행
ex = MyVideoUI()                            # 이미지 넣을 UI 생성
v = Video()                                 # 이미지 캡쳐한거 올리기

def run():                                  # 스래드 함수
    t = 0
    while t < 2000:                         # 새 필터로 업데이트 되는 동안 기다림
        ex.label.setPixmap(v.updateFrame())
        time.sleep(0.01)
        t += 1

    v.close()

def selectedFilter(text):
    v.filter.setFilter(text)        # video 객체의 멤버변수 filter 객체의 setfilter함수

def flip(a):
    if ex.checkBox1.isChecked() and ex.checkBox2.isChecked():
        v.flip.setFlip("case3")
    elif ex.checkBox1.isChecked() and not ex.checkBox2.isChecked():
        v.flip.setFlip("case1")
    elif not ex.checkBox1.isChecked() and ex.checkBox2.isChecked():
        v.flip.setFlip("case2")
    else:
        v.flip.setFlip("case0")


ex.comboBox.currentTextChanged.connect(selectedFilter) #콤보박스 옵션이 바뀔때 
ex.saveBtn.clicked.connect(v.saveImg) # 저장버튼 눌렸을때
ex.checkBox1.stateChanged.connect(flip)
ex.checkBox2.stateChanged.connect(flip)

th = threading.Thread(target=run)     # 쓰레드 생성 함수는 run
th.start()

sys.exit(app.exec_())