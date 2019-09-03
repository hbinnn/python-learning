import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle('退出应用程序')

        # 添加Button
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(QCoreApplication.instance().quit())

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def OneClick_Button(self):
        sender = self.sender()

        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())