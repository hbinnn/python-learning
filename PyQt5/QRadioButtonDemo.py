"""
单选按钮
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')

        layout = QHBoxLayout()

        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)

        self.button2 = QRadioButton('单选按钮2')

        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print('<' + radioButton.text() + '>被选中')
        else:
            print('<' + radioButton.text() + '>未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())