import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QVBoxLayout, QPushButton, QCheckBox


class MyVideoUI(QWidget):   # 사용자 정의 class, QWidget 을 상속
    def __init__(self):
        super().__init__()
        self.initUI() # 부모 클래스와 상관없는 초기화

    def initUI(self):           # 객체 생성시 이 함수 자동호출
        self.label = QLabel()   # 레이블 생성

        self.comboBox = QComboBox()     # 콤보박스 생성
        self.checkBox1 = QCheckBox("Horizontally Flip")
        self.checkBox2 = QCheckBox("Vertically Flip")
        self.saveBtn = QPushButton("&Save") # 버튼 생성

        self.comboBox.addItem("original")
        self.comboBox.addItem("blur")
        self.comboBox.addItem("medianBlur")
        self.comboBox.addItem("Gaussianbur")
        self.comboBox.addItem("threshold")
        self.comboBox.addItem("Sobel")
        self.comboBox.addItem("Laplacian")
        self.comboBox.addItem("reverse")

        self.vBox = QVBoxLayout()           # 수직 레이아웃
        self.vBox.addWidget(self.checkBox1)
        self.vBox.addWidget(self.checkBox2)
        self.vBox.addWidget(self.comboBox)  # 콤보박스랑 버튼 넣음
        self.vBox.addWidget(self.saveBtn)

        self.hBox = QHBoxLayout()           # 수평 레이아웃
        self.hBox.addWidget(self.label)     # 빈 레이블 넣음
        self.hBox.addLayout(self.vBox)      # 수직 박스 넣음, 여기서 이미 겹쳐짐

        self.setLayout(self.hBox)
        self.resize(1200, 800)
        self.show()
        
if __name__ == "__main__":                      # 테스트용 코드
    app = QtWidgets.QApplication(sys.argv)      # roscore 같은 존재 모든 qt 어플리케이션은 우선적으로 QApplication 객체를 생성해야 한다
    ex = MyVideoUI()
    sys.exit(app.exec_())
