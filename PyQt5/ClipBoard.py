"""
使用剪贴板
"""

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用剪贴板')

        textCopyButton = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')
        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')
        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textlabel = QLabel('默认文本')
        self.imagelabel = QLabel()
        # self.imagelabel.setPixmap(QPixmap('./logo.png'))

        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(textPasteButton, 0, 1)
        layout.addWidget(htmlCopyButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imageCopyButton, 2, 0)
        layout.addWidget(imagePasteButton, 2, 1)
        layout.addWidget(self.textlabel, 3, 0, 1, 2)
        layout.addWidget(self.imagelabel, 4, 2)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHTML)
        htmlPasteButton.clicked.connect(self.pasteHTML)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setLayout(layout)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('hello world')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textlabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./logo.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imagelabel.setPixmap(clipboard.pixmap())

    def copyHTML(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHTML(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textlabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())