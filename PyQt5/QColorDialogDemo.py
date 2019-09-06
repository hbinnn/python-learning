"""
颜色对话框
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('颜色对话框')
        layout = QVBoxLayout()

        self.colorbutton = QPushButton('选择颜色')
        self.colorbutton.clicked.connect(self.getColor)
        self.colorlabel = QLabel('测试颜色')

        self.colorbutton1 = QPushButton('选择背景颜色')
        self.colorbutton1.clicked.connect(self.getBGColor)


        layout.addWidget(self.colorbutton)
        layout.addWidget(self.colorbutton1)
        layout.addWidget(self.colorlabel)
        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorlabel.setPalette(p)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorlabel.setAutoFillBackground(True)
        self.colorlabel.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())