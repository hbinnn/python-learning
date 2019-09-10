from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mainFile
from urllib.parse import urlencode
import time
import os


class QComboBoxDemo(QWidget):
    def __init__(self, ip, node_ipv4, node_ipv6, protocol):
        super(QComboBoxDemo, self).__init__()
        self.ip = ip
        self.node_ipv4 = node_ipv4
        self.node_ipv6 = node_ipv6
        self.protocol = protocol
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IPIP脚本程序')
        self.resize(500, 100)
        self.setWindowIcon(QIcon('./logo.png'))
        layout = QFormLayout()

        self.label1 = QLabel('请选择IP版本')
        self.cb1 = QComboBox()

        self.label2 = QLabel('请选择节点')
        self.cb2 = QComboBox()
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()

        self.label3 = QLabel('请选择协议')
        self.cb3 = QComboBox()
        self.label4 = QLabel('请输入IP地址')
        self.lineEdit = QLineEdit()
        self.button = QPushButton('查询')
        self.button2 = QPushButton('查看查询结果')
        self.label5 = QLabel('请选择查询文件保存路径')
        self.button3 = QPushButton('选择路径')
        self.label6 = QLabel()

        self.cb2.setLineEdit(self.qLineEdit)
        self.cb2.setModel(self.qListWidget.model())
        self.cb2.setView(self.qListWidget)

        layout.addRow(self.label1, self.cb1)
        layout.addRow(self.label2, self.cb2)
        layout.addRow(self.label3, self.cb3)
        layout.addRow(self.label4, self.lineEdit)
        layout.addRow(self.label5, self.button3)
        layout.addRow(self.label6)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        self.setLayout(layout)

        for i in range(len(self.ip)):
            self.cb1.addItem(self.ip[i]['name'])

        self.row_num = len(self.node_ipv4)
        for i in range(self.row_num):
            self.qCheckBox.append(QCheckBox())
            qItem = QListWidgetItem(self.qListWidget)
            self.qCheckBox[i].setText(self.node_ipv4[i]['name'])
            self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])
            self.qCheckBox[i].stateChanged.connect(self.display)

        for i in range(len(self.protocol)):
            self.cb3.addItem(self.protocol[i]['name'])

        self.ip_code = '4' if self.cb1.currentText()=='IPv4' else '6'
        self.node_code = self.node_ipv4[0]['code']
        self.node_label = self.cb2.currentText()
        self.protocol_code = 'T' if self.cb3.currentText()=='TCP' else 'I'
        self.path = ''
        self.label6.setText(os.getcwd())

        self.cb1.currentIndexChanged.connect(self.selectionChangeIp_code)
        # self.cb2.currentIndexChanged.connect(self.selectionChangeNode_code)
        self.cb3.currentIndexChanged.connect(self.selectionChangeProtocol_code)
        self.lineEdit.textChanged.connect(self.textChange)
        self.button.clicked.connect(self.submit)
        self.button2.clicked.connect(self.openfile)
        self.button3.clicked.connect(self.selectpath)

    def selectionChangeIp_code(self):
        self.ip_code = '4' if self.cb1.currentText() == 'IPv4' else '6'
        if self.ip_code == '4':
            self.cb2.clear()
            self.qCheckBox = []
            self.row_num = len(self.node_ipv4)
            for i in range(self.row_num):
                self.qCheckBox.append(QCheckBox())
                qItem = QListWidgetItem(self.qListWidget)
                self.qCheckBox[i].setText(self.node_ipv4[i]['name'])
                self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])
                self.qCheckBox[i].stateChanged.connect(self.display)
        elif self.ip_code == '6':
            self.cb2.clear()
            self.qCheckBox = []
            self.row_num = len(self.node_ipv6)
            for i in range(self.row_num):
                self.qCheckBox.append(QCheckBox())
                qItem = QListWidgetItem(self.qListWidget)
                self.qCheckBox[i].setText(self.node_ipv6[i]['name'])
                self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])
                self.qCheckBox[i].stateChanged.connect(self.display)


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

    def display(self):
        self.node_label = ''
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in self.Selectlist():
            self.node_label += i + ';'
        self.qLineEdit.setText(self.node_label)
        self.qLineEdit.setReadOnly(True)

        self.node_code_list = []
        self.node_label_list = self.node_label.split(';')
        print(self.node_label_list)

        for node_label in self.node_label_list:
            if self.ip_code == '4':
                for i in range(len(self.node_ipv4)):
                    if node_label == self.node_ipv4[i]['name']:
                        self.node_code_list.append(self.node_ipv4[i]['code'])
            elif self.ip_code == '6':
                for i in range(len(self.node_ipv6)):
                    if node_label == self.node_ipv6[i]['name']:
                        self.node_code_list.append(self.node_ipv6[i]['code'])

        print(self.node_code_list)

    def submit(self):
        for index, node_code in enumerate(self.node_code_list):
            for address in self.ip_address.split(';'):
                dir = {'as': '1',
                       'v': self.ip_code,
                       'a': 'get',
                       'n': '1',
                       'id': node_code,
                       't': self.protocol_code,
                       'ip': address}

                url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
                html = mainFile.getRespondHTML(url)
                self.filename = 'TraceRoute ' + address + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.node_label_list[index] + '.csv'
                self.filename = self.filename.replace(':', '-').replace(' ', '_')
                self.filename = self.path + '/' + self.filename
                flag = 0
                for item in mainFile.praseRespond(html):
                    item = mainFile.operateRespond(item)
                    mainFile.writeRespond_to_file_csv(self.filename, item, flag)
                    flag = 1

    def openfile(self):
       dialog = QFileDialog()
       dialog.setFileMode(QFileDialog.AnyFile)
       dialog.setFilter(QDir.Files)

       if dialog.exec():
           filenames = dialog.selectedFiles()
           os.system(filenames[0])

    def selectpath(self):
        self.path = QFileDialog.getExistingDirectory(self, '请选择文件夹', os.getcwd())
        self.label6.setText(self.path)

    def Selectlist(self):
        Outputlist = []
        for i in range(self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        return Outputlist