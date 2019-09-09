from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mainFile
from urllib.parse import urlencode
import time


class QComboBoxDemo(QWidget):
    def __init__(self, ip, node_ipv4, node_ipv6, protocol):
        super(QComboBoxDemo, self).__init__()
        self.initUI(ip, node_ipv4, node_ipv6, protocol)

    def initUI(self, ip, node_ipv4, node_ipv6, protocol):
        self.setWindowTitle('IPIP脚本程序')
        self.resize(500, 100)
        self.setWindowIcon(QIcon('./logo.png'))
        layout = QFormLayout()

        self.ip = ip
        self.node_ipv4 = node_ipv4
        self.node_ipv6 = node_ipv6
        self.protocol = protocol

        self.label1 = QLabel('请选择IP版本')
        self.cb1 = QComboBox()
        self.label2 = QLabel('请选择节点')
        self.cb2 = QComboBox()
        self.label3 = QLabel('请选择协议')
        self.cb3 = QComboBox()
        self.label4 = QLabel('请输入IP地址')
        self.lineEdit = QLineEdit()
        self.button = QPushButton('查询')

        layout.addRow(self.label1, self.cb1)
        layout.addRow(self.label2, self.cb2)
        layout.addRow(self.label3, self.cb3)
        layout.addRow(self.label4, self.lineEdit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        for i in range(len(self.ip)):
            self.cb1.addItem(self.ip[i]['name'])
        for i in range(len(self.node_ipv4)):
            self.cb2.addItem(self.node_ipv4[i]['name'])
        for i in range(len(self.protocol)):
            self.cb3.addItem(self.protocol[i]['name'])

        self.ip_code = '4' if self.cb1.currentText()=='IPv4' else '6'
        self.node_code = self.node_ipv4[0]['code']
        self.protocol_code = 'T' if self.cb3.currentText()=='TCP' else 'I'

        self.cb1.currentIndexChanged.connect(self.selectionChangeIp_code)
        self.cb2.currentIndexChanged.connect(self.selectionChangeNode_code)
        self.cb3.currentIndexChanged.connect(self.selectionChangeProtocol_code)
        self.lineEdit.textChanged.connect(self.textChange)
        self.button.clicked.connect(self.submit)

    def selectionChangeIp_code(self):
        self.ip_code = '4' if self.cb1.currentText() == 'IPv4' else '6'
        if self.ip_code == '4':
            self.cb2.clear()
            for i in range(len(self.node_ipv4)):
                self.cb2.addItem(self.node_ipv4[i]['name'])
        elif self.ip_code == '6':
            self.cb2.clear()
            for i in range(len(self.node_ipv6)):
                self.cb2.addItem(self.node_ipv6[i]['name'])

    def selectionChangeNode_code(self):
        self.node_label = self.cb2.currentText()
        if self.ip_code == '4':
            for i in range(len(self.node_ipv4)):
                if self.node_label == self.node_ipv4[i]['name']:
                    self.node_code = self.node_ipv4[i]['code']
        elif self.ip_code == '6':
            for i in range(len(self.node_ipv6)):
                if self.node_label == self.node_ipv6[i]['name']:
                    self.node_code = self.node_ipv6[i]['code']

    def selectionChangeProtocol_code(self):
        self.protocol_label = self.cb3.currentText()
        if self.protocol_label == 'TCP':
            self.protocol_code = 'T'
        else:
            self.protocol_code = 'I'

    def textChange(self, text):
        self.ip_address = text

    def submit(self):
        dir = {'as': '1',
               'v': self.ip_code,
               'a': 'get',
               'n': '1',
               'id': self.node_code,
               't': self.protocol_code,
               'ip': self.ip_address}

        url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
        html = mainFile.getRespondHTML(url)
        filename = 'TraceRoute ' + '8.8.8.8 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.csv'
        filename = filename.replace(':', '-')
        flag = 0
        for item in mainFile.praseRespond(html):
            item = mainFile.operateRespond(item)
            mainFile.writeRespond_to_file_csv(filename, item, flag)
            flag = 1
