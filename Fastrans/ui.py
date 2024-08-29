from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import (PushButton, ComboBox, LineEdit, TextEdit, ToggleToolButton, ToolButton, SwitchButton,
                            FluentIcon as FIF)
import sys


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fastrans")
        self.resize(700, 400)
        self.setMaximumSize(QtCore.QSize(700, 400))
        self.setMinimumSize(QtCore.QSize(700, 400))

        font = QtGui.QFont("微软雅黑", 12)

        icon = QtGui.QIcon(QtGui.QPixmap("src/icon.ico"))
        self.setWindowIcon(icon)

        self.txt_input = LineEdit(self)
        self.txt_input.setClearButtonEnabled(True)
        self.txt_input.setPlaceholderText("按下 Enter 翻译")
        self.txt_input.setGeometry(QtCore.QRect(20, 80, 500, 40))
        self.txt_input.setFont(font)

        self.txt_result = TextEdit(self)
        self.txt_result.setGeometry(QtCore.QRect(20, 140, 660, 240))
        self.txt_result.setFont(font)
        self.txt_result.setReadOnly(True)

        self.btn_trans = PushButton("翻译", self)
        self.btn_trans.setGeometry(QtCore.QRect(540, 80, 140, 40))
        self.btn_trans.setFont(font)

        self.combo_platform = ComboBox(self)
        self.combo_platform.addItems(["必应", "有道", "搜狗"])
        self.combo_platform.setGeometry(QtCore.QRect(20, 20, 130, 40))
        self.combo_platform.setFont(font)

        self.btn_theme = ToggleToolButton(FIF.CONSTRACT, self)
        self.btn_theme.setGeometry(QtCore.QRect(580, 20, 40, 40))
        self.btn_theme.setFont(font)

        self.btn_topmost = ToggleToolButton(FIF.PIN, self)
        self.btn_topmost.setGeometry(QtCore.QRect(640, 20, 40, 40))
        self.btn_topmost.setFont(font)

        self.btn_copy = ToolButton(FIF.COPY, self)
        self.btn_copy.setGeometry(QtCore.QRect(610, 150, 60, 30))
        self.btn_copy.setFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Ui()
    win.show()
    sys.exit(app.exec_())
