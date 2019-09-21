# coding=gbk
import ComboList
import mainFile
from PyQt5.QtWidgets import *
import sys

# 获取IP版本,监控机节点，可用协议
url1 = 'https://tools.ipip.net/traceroute.php?v=4'
url2 = 'https://tools.ipip.net/traceroute.php?v=6'
html1 = mainFile.getWatchNodeHTML(url1)
html2 = mainFile.getWatchNodeHTML(url2)

ip=[]
node_ipv4=[]
node_ipv6=[]
protocol=[]

for item in mainFile.praseWatchNode_ip(html1):
    ip.append(item)
for item in mainFile.praseWatchNode_asn_ipv4(html1):
    node_ipv4.append(item)
for item in mainFile.praseWatchNode_asn_ipv6(html2):
    node_ipv6.append(item)
for item in mainFile.praseWatchNode_protocol(html1):
    protocol.append(item)

app = QApplication(sys.argv)
main = ComboList.QComboBoxDemo(ip, node_ipv4, node_ipv6, protocol)
main.show()
sys.exit(app.exec_())
