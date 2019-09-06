"""
绘图API:绘制文本

1、文本
2、图形
3、图像

painter = QPainter
painter.begin()
painter.drawText()
painter.end()

必须在paintEvent事件方法中绘制各种元素
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 200)
        self.text = 'python'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSun', 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())