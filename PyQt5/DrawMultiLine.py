import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置pen的样式')
        self.resize(300, 200)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        size = self.size()
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 40)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 40)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 40)

        # 自定义点划线
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,10,5,4])
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 40)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())