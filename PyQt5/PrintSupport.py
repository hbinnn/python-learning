"""
使用打印机
"""

import sys
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用打印机')
        self.resize(300, 300)

        self.button = QPushButton("打印QTextEdit控件中的内容", self)
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit('默认文本', self)
        self.editor.setGeometry(20, 60, 260, 200)

        self.button.clicked.connect(self.print)

    def print(self):
        printer = QPrinter()
        painter = QPainter()
        # 将绘制目标重定向到打印机
        painter.begin(printer)

        screen = self.editor.grab()
        painter.drawPixmap(10, 10, screen)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PrintSupport()
    main.show()
    sys.exit(app.exec_())