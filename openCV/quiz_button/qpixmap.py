import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap

imgPath = "front.jpg"

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(imgPath)
        self.img = QLabel()
        self.img.setPixmap(self.pixmap)

        Button1 = QPushButton('앞')
        Button2 = QPushButton('뒤')
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.img)
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.setGeometry(300, 300, 400, 500)
        self.show()
        
        Button1.clicked.connect(self.button1_callback)
        Button2.clicked.connect(self.button2_callback)
    
    def button1_callback(self):
        global imgPath
        if imgPath == 'rear.jpg':
            imgPath = 'front.jpg'
            pixmap = QPixmap(imgPath)
            self.img.setPixmap(pixmap)

    def button2_callback(self):
        global imgPath
        if imgPath == 'front.jpg':
            imgPath = 'rear.jpg'
            pixmap = QPixmap(imgPath)
            self.img.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())