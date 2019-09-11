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

        # 初始化界面
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

        # IP版本下拉菜单
        for i in range(len(self.ip)):
            self.cb1.addItem(self.ip[i]['name'])

        # 监控机节点下拉菜单
        self.row_num = len(self.node_ipv4)
        for i in range(self.row_num):
            self.qCheckBox.append(QCheckBox())
            qItem = QListWidgetItem(self.qListWidget)
            self.qCheckBox[i].setText(self.node_ipv4[i]['name'])
            self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])
            self.qCheckBox[i].stateChanged.connect(self.display)

        # 协议版本下拉菜单
        for i in range(len(self.protocol)):
            self.cb3.addItem(self.protocol[i]['name'])

        # url查询参数初始化，默认为ipv4，TCP，
        self.ip_code = '4' if self.cb1.currentText()=='IPv4' else '6'
        self.node_code = self.node_ipv4[0]['code']
        self.node_label = self.cb2.currentText()
        self.protocol_code = 'T' if self.cb3.currentText()=='TCP' else 'I'
        self.path = ''
        self.label6.setText(os.getcwd())

        # 槽函数
        self.cb1.currentIndexChanged.connect(self.selectionChangeIp_code)
        # self.cb2.currentIndexChanged.connect(self.selectionChangeNode_code)
        self.cb3.currentIndexChanged.connect(self.selectionChangeProtocol_code)
        self.lineEdit.textChanged.connect(self.textChange)
        self.button.clicked.connect(self.submit)
        self.button2.clicked.connect(self.openfile)
        self.button3.clicked.connect(self.selectpath)

    # 当IP版本变化时，关联监控机节点列表变化
    def selectionChangeIp_code(self):
        self.ip_code = '4' if self.cb1.currentText() == 'IPv4' else '6'
        # IP版本对应的监控机列表
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

    # 监控机节点变化，将对应的监控机节点代码赋值给self.node_code
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

    # 协议变化
    def selectionChangeProtocol_code(self):
        self.protocol_label = self.cb3.currentText()
        if self.protocol_label == 'TCP':
            self.protocol_code = 'T'
        else:
            self.protocol_code = 'I'

    # 显示输入的要查询的IP地址
    def textChange(self, text):
        self.ip_address = text

    # 监控机节点下拉菜单多选框
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

        for node_label in self.node_label_list:
            if self.ip_code == '4':
                for i in range(len(self.node_ipv4)):
                    if node_label == self.node_ipv4[i]['name']:
                        self.node_code_list.append(self.node_ipv4[i]['code'])
            elif self.ip_code == '6':
                for i in range(len(self.node_ipv6)):
                    if node_label == self.node_ipv6[i]['name']:
                        self.node_code_list.append(self.node_ipv6[i]['code'])

    # 向网站提交请求，self.node_code_list为要查询的监控机节点列表，self.ip_address为要查询的ip地址，查询多个ip时用';'隔开（半角符号）
    def submit(self):
        for index, node_code in enumerate(self.node_code_list):
            for address in self.ip_address.split(';'):
                # 构造提交的链接
                dir = {'as': '1',
                       'v': self.ip_code,
                       'a': 'get',
                       'n': '1',
                       'id': node_code,
                       't': self.protocol_code,
                       'ip': address}
                url = 'https://tools.ipip.net/traceroute.php?' + urlencode(dir)
                html = mainFile.getRespondHTML(url)

                # 查询结果保存的文件名，例如TraceRoute_8.8.8.8_2019-09-11_15-03-10内蒙古呼和浩特(天翼云).csv
                self.filename = 'TraceRoute ' + address + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.node_label_list[index] + '.csv'
                self.filename = self.filename.replace(':', '-').replace(' ', '_')
                self.filename = self.path + '/' + self.filename

                # flag仅仅是为了避免多次写入标题而设置的标识
                flag = 0
                for item in mainFile.praseRespond(html):
                    item = mainFile.operateRespond(item)
                    mainFile.writeRespond_to_file_csv(self.filename, item, flag)
                    flag = 1

    # 打开所选文件
    def openfile(self):
       dialog = QFileDialog()
       dialog.setFileMode(QFileDialog.AnyFile)
       dialog.setFilter(QDir.Files)

       if dialog.exec():
           filenames = dialog.selectedFiles()
           os.system(filenames[0])

    # 选择保存文件的路径self.path
    def selectpath(self):
        self.path = QFileDialog.getExistingDirectory(self, '请选择文件夹', os.getcwd())
        self.label6.setText(self.path)

    # 确认监控机节点下拉菜单中哪些节点被选中
    def Selectlist(self):
        Outputlist = []
        for i in range(self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        return Outputlist