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

        font = QtGui.QFont("微软雅黑", 12)

        icon = QtGui.QIcon(QtGui.QPixmap("src/icon.ico"))
        self.setWindowIcon(icon)

        self.txt_input = LineEdit(self)
        self.txt_input.setFixedHeight(40)
        self.txt_input.setClearButtonEnabled(True)
        self.txt_input.setPlaceholderText("按下 Enter 翻译")
        self.txt_input.setFont(font)

        self.txt_result = TextEdit(self)
        self.txt_result.setFont(font)
        self.txt_result.setReadOnly(True)

        self.btn_trans = PushButton("翻译", self)
        self.btn_trans.setFixedSize(120, 40)
        self.btn_trans.setFont(font)

        self.combo_platform = ComboBox(self)
        self.combo_platform.addItems(["必应", "有道", "搜狗"])
        self.combo_platform.setFixedSize(120, 40)
        self.combo_platform.setFont(font)

        self.btn_theme = ToggleToolButton(FIF.CONSTRACT, self)
        self.btn_theme.setFixedSize(40, 40)
        self.btn_theme.setFont(font)

        self.btn_topmost = ToggleToolButton(FIF.PIN, self)
        self.btn_topmost.setFixedSize(40, 40)
        self.btn_topmost.setFont(font)

        self.btn_copy = ToolButton(FIF.COPY, self.txt_result)
        self.btn_copy.setFixedSize(40, 40)
        self.btn_copy.setFont(font)

        # 布局
        self.layout = QtWidgets.QVBoxLayout()

        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.combo_platform)
        self.layout1.addStretch(1)
        self.layout1.addWidget(self.btn_theme)
        self.layout1.addWidget(self.btn_topmost)

        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.addWidget(self.txt_input)
        self.layout2.addWidget(self.btn_trans)

        self.layout3 = QtWidgets.QHBoxLayout()
        self.layout3.addWidget(self.btn_copy)
        self.layout3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.txt_result.setLayout(self.layout3)

        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.layout.addWidget(self.txt_result)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Ui()
    win.show()
    sys.exit(app.exec_())
