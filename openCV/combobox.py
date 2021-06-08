import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.lbl = QLabel('fhasjkfhasklf', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Optionx')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QcomboBox')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
