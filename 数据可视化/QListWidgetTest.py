"""
https://blog.csdn.net/LJX4ever/article/details/78039318
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ComboCheckBox(QWidget):
    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        layout = QFormLayout()
        self.items = items
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        qListWidget = QListWidget()
        self.cb = QComboBox()

        self.row_num = len(self.items)
        for i in range(self.row_num):
            self.qCheckBox.append(QCheckBox())
            qItem = QListWidgetItem(qListWidget)
            self.qCheckBox[i].setText(self.items[i])
            qListWidget.setItemWidget(qItem, self.qCheckBox[i])
            self.qCheckBox[i].stateChanged.connect(self.show1)

        self.cb.setLineEdit(self.qLineEdit)
        self.cb.setModel(qListWidget.model())
        self.cb.setView(qListWidget)

        layout.addWidget(self.cb)
        self.setLayout(layout)

    def Selectlist(self):
        Outputlist = []
        for i in range(self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        return Outputlist

    def show1(self):
        show = ''
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in self.Selectlist():
            show += i + ';'
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)
