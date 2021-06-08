import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)       # button 객체 생성 (text, button location object)
      btn.move(100, 100)                    # location of button in window 
      btn.resize(btn.sizeHint())            # 적절한 크기 알아서 맞추기
      btn.clicked.connect(QCoreApplication.instance().quit) # 버튼 누르면 quit() 메소드로 연결

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)  # x좌표, y좌표, 가로, 세로
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()        # 변수에 저장 안하면 바로꺼짐
    sys.exit(app.exec_())