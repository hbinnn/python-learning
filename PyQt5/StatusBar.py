"""
创建状态栏
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('创建状态栏')
        self.resize(300, 300)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered.connect(self.processTrigger)

        self.statusBar = QStatusBar()

        self.setStatusBar(self.statusBar)


    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())