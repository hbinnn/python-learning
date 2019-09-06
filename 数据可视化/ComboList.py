from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mainFile
from urllib.parse import urlencode


class QComboBoxDemo(QWidget):
    def __init__(self, ip, node, protocol):
        super(QComboBoxDemo, self).__init__()
        self.initUI(ip, node, protocol)

    def initUI(self, ip, node, protocol):
        self.setWindowTitle('IPIP脚本程序')
        self.resize(500, 100)
        self.setWindowIcon(QIcon('./logo.png'))
        layout = QFormLayout()

        self.label1 = QLabel('请选择IP版本')
        self.cb1 = QComboBox()
        self.label2 = QLabel('请选择节点')
        self.cb2 = QComboBox()
        self.label3 = QLabel('请选择协议')
        self.cb3 = QComboBox()
        self.label4 = QLabel('请输入IP地址')
        self.lineEdit = QLineEdit()
        self.button = QPushButton('查询')
        self.label5 = QLabel('查询结果')
        self.text = QTextEdit()

        layout.addRow(self.label1, self.cb1)
        layout.addRow(self.label2, self.cb2)
        layout.addRow(self.label3, self.cb3)
        layout.addRow(self.label4, self.lineEdit)
        layout.addWidget(self.button)
        layout.addWidget(self.label5)
        layout.addWidget(self.text)

        self.setLayout(layout)

        for i in range(len(ip)):
            self.cb1.addItem(ip[i]['name'])
        for i in range(len(node)):
            self.cb2.addItem(node[i]['name'])
        for i in range(len(protocol)):
            self.cb3.addItem(protocol[i]['name'])

        self.cb1.currentIndexChanged.connect(self.selectionChangeIp_code)
        self.cb2.currentIndexChanged.connect(lambda:self.selectionChangeNode_code(node))
        self.cb3.currentIndexChanged.connect(self.selectionChangeProtocol_code)
        self.lineEdit.textChanged.connect(self.textChange)
        self.button.clicked.connect(lambda:self.submit(self.ip_code, self.node_code, self.protocol_code, self.ip_address))

    def selectionChangeIp_code(self):
        self.ip_label = self.cb1.currentText()
        if self.ip_label == 'IPv4':
            self.ip_code = '4'
        else:
            self.ip_code = '6'


    def selectionChangeNode_code(self, node):
        self.node_label = self.cb2.currentText()
        for i in range(len(node)):
            if self.node_label == node[i]['name']:
                self.node_code = node[i]['code']


    def selectionChangeProtocol_code(self):
        self.protocol_label = self.cb3.currentText()
        if self.protocol_label == 'TCP':
            self.protocol_code = 'T'
        else:
            self.protocol_code = 'I'


    def textChange(self, text):
        self.ip_address = text


    def submit(self, ip_code, node_code, protocol_code, ip_address):
        dir = {'as': '1',
               'v': ip_code,
               'a': 'get',
               'n': '1',
               'id': node_code,
               't': protocol_code,
               'ip': ip_address}

        url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
        html = mainFile.getRespondHTML(url)
        flag = 0
        for item in mainFile.praseRespond(html):
            item = mainFile.operateRespond(item)
            print(item)
