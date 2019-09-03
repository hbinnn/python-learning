import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

"""
窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用
QApplication中的setWindowIcon方法用于设置主窗口和应用程序图标，但如果调用了窗口的setWindowIcon方法，
QApplication中的setWindowIcon方法就只能用于程序图标了
"""
class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,250)
        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')

        # 设置窗口图标
        # self.setWindowIcon(QIcon('./'))


# 防止别的脚本调用
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置图标
    # app.setWindowIcon(QIcon('./'))

    main = FirstMainWin()
    main.show()

    # 进入程序主循环
    sys.exit(app.exec_())