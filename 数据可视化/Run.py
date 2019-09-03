import ComboList
import PraseWatchNode
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
ip, node, protocol = PraseWatchNode.run_main(4)
main = ComboList.QComboBoxDemo(ip, node, protocol)
main.show()

sys.exit(app.exec_())
