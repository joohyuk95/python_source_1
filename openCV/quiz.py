import cv2
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        label = QLabel()
        firstButton = QPushButton('1')
        secondButton = QPushButton('2')

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(firstButton)
        vbox.addWidget(secondButton)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('image change')
        self.setGeometry(300, 300, 400, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    
    sys.exit(app.exec_())