import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用画刷填充区域')
        self.resize(300, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(135, 15, 90, 60)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()
    sys.exit(app.exec_())