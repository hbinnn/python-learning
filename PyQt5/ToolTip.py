import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QFont


class ToolTipFrom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSefif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('Button')
        self.button1.setToolTip('这是一个按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolTipFrom()
    main.show()
    sys.exit(app.exec_())