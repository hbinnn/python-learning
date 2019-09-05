"""
滑块控件
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSlider控件演示')
        self.resize(300, 300)

        layout = QVBoxLayout()

        self.label = QLabel('hello')
        self.label.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal)
        self.slider1 = QSlider(Qt.Vertical)
        # 设置最小值、最大值、步长、当前值
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        self.slider.setSingleStep(3)
        self.slider.setValue(18)
        # 设置刻度的位置，在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider.setTickInterval(6)
        self.slider.valueChanged.connect(self.valueChange)

        # 设置最小值、最大值、步长、当前值
        self.slider1.setMinimum(10)
        self.slider1.setMaximum(60)
        self.slider1.setSingleStep(5)
        self.slider1.setValue(30)
        # 设置刻度的位置，在下方
        self.slider1.setTickPosition(QSlider.TicksLeft)
        # 设置刻度的间隔
        self.slider1.setTickInterval(6)
        self.slider1.valueChanged.connect(self.valueChange)

        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)

        self.setLayout(layout)

    def valueChange(self):
        # sender当前操作的控件
        print('当前值：%s' % self.sender().value())
        size = self.sender().value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())