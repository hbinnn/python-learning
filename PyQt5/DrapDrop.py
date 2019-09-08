"""
让控件支持拖拽
A.setDragEnabled(True)
B.setAcceptDrops(True)

B需要两个事件
1、dragEnterEvent
2、dropEvent
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyComboxBox(QComboBox):
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('拖拽案例')

        formlayout = QFormLayout()
        formlayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))

        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)

        combo = MyComboxBox()
        formlayout.addRow(lineEdit, combo)

        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())