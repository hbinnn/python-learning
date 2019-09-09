"""
创建工具栏
工具栏默认按钮只显示图标，将文本作为悬停提示

工具栏按钮有3种显示方式：
1、只显示图标
2、只显示文本
3、同时显示文本和图标
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('创建工具栏')
        self.resize(300, 300)

        tb1 = self.addToolBar("File")
        new = QAction(QIcon('./logo.png'), "new", self)
        tb1.addAction(new)

        # open = QAction(QIcon(''), "open", self)
        # tb1.addAction(open)
        # 同时显示文本和图标
        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print(a.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBar()
    main.show()
    sys.exit(app.exec_())