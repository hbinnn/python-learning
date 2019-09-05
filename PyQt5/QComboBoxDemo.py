"""
下拉列表控件
1、如何将列表项添加到QComboBox
2、如何获取选中的列表项
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300, 100)

        layout = QHBoxLayout()

        self.label = QLabel('请选择编程语言')
        self.cb = QComboBox()
        self.cb.addItems(['C++', 'JAVA', 'C#', 'Python', 'Ruby'])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self, index):
        # self.label.setText(self.cb.currentText())
        # self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index', index, 'selection change', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())