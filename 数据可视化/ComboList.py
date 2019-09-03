from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self, ip, node, protocol):
        super(QComboBoxDemo, self).__init__()
        self.initUI(ip, node, protocol)

    def initUI(self, ip, node, protocol):
        self.setWindowTitle('IPIP脚本程序')
        self.resize(500, 100)

        layout = QVBoxLayout()

        self.label1 = QLabel('请选择IP版本')
        self.cb1 = QComboBox()

        for i in range(len(ip)):
            self.cb1.addItem(ip[i]['name'])

        self.cb1.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label1)
        layout.addWidget(self.cb1)

        self.label2 = QLabel('请选择节点')
        self.cb2 = QComboBox()

        for i in range(len(node)):
            self.cb2.addItem(node[i]['name'])

        self.cb2.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label2)
        layout.addWidget(self.cb2)

        self.label3 = QLabel('请选择协议')
        self.cb3 = QComboBox()

        for i in range(len(protocol)):
            self.cb3.addItem(protocol[i]['name'])

        self.cb3.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label3)
        layout.addWidget(self.cb3)

        self.setLayout(layout)

    def selectionChange(self, i):

        self.label1.adjustSize()
        self.label2.adjustSize()
        self.label3.adjustSize()
