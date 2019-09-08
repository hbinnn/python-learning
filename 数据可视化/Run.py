import ComboList
import mainFile
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
ip, node, protocol = mainFile.run_getRespond_main(4)
main = ComboList.QComboBoxDemo(ip, node, protocol)
main.show()

sys.exit(app.exec_())
