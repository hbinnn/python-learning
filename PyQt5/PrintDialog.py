"""
显示打印对话框
"""

import sys
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('打印对话框')
        self.resize(300, 300)
