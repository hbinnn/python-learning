""""
输入各种风格的日期和时间
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateTimeDemo(QDialog):
    def __init__(self):
        super(DateTimeDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置不同风格的日期和时间')
        self.resize(300, 300)

        layout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        # 设置最大、小日期
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        self.dateTimeEdit = dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd  HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd  HH:mm:ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:dd")

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        self.btn = QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    # 日期变化
    def onDateChanged(self, date):
        print(date)

    def onTimeChanged(self, time):
        print(time)

    def onDateTimeChanged(self, datetime):
        print(datetime)

    def onButtonClick(self):
        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)
        print(self.dateTimeEdit.maximumDate())
        print(self.dateTimeEdit.minimumDate())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeDemo()
    main.show()
    sys.exit(app.exec_())