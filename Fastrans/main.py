from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5 import QtCore
from qfluentwidgets import Theme, setTheme
import eng_to_ipa as ipa
import pyperclip
import sys
import ctypes
import keyboard

from ui import Ui
from translate import Translator


# 主窗口
class Win(Ui):
    def __init__(self):
        super().__init__()
        self.txt_input.setFocus()
        self.btn_trans.clicked.connect(self.translate)
        self.btn_trans.setShortcut('Return')  # 绑定快捷键
        self.now_translation = ""
        self.btn_copy.clicked.connect(lambda: pyperclip.copy(self.now_translation))
        self.btn_theme.toggled.connect(self.switch_theme)
        self.btn_topmost.toggled.connect(self.topmost)

        self.tray_icon.activated.connect(self.activate)  # 打开窗口
        self.closeEvent = self.close_to_tray  # 关闭程序

        keyboard.add_hotkey('alt+w', self.show_win)  # 绑定快捷键

    # 翻译函数
    def translate(self):
        content = self.txt_input.text()

        # 检查输入是否为空
        if not content:
            return

        # 检查语言
        if content[0] < '\u4e00' or content[0] > '\u9fff':
            from_lang = 'auto'
            to_lang = 'zh'
        else:
            from_lang = 'zh'
            to_lang = 'en'

        # 翻译
        source = self.combo_platform.currentText()
        translator = Translator(content=content, from_lang=from_lang, to_lang=to_lang, source=source)
        translation = translator.translate()
        self.txt_result.setText(translation)
        self.now_translation = translation

        # 音标
        result = ipa.convert(translation if from_lang == 'zh' else content)
        self.txt_result.append('\n[' + result + ']')

    # 切换主题
    def switch_theme(self, is_toggled):
        self.setStyleSheet("background-color: #272727" if is_toggled else "background-color: #f7f9fc")
        setTheme(Theme.DARK if is_toggled else Theme.LIGHT)

    # 置顶
    def topmost(self, is_toggled):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint if is_toggled else QtCore.Qt.Widget)
        self.show()

    # 关闭到托盘
    def close_to_tray(self, event):
        event.ignore()
        self.hide()

    # 双击打开
    def activate(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show()

    # 包装函数，确保在主线程中调用 self.show
    def show_win(self):
        QtCore.QMetaObject.invokeMethod(self, 'show', QtCore.Qt.QueuedConnection)
        QtCore.QMetaObject.invokeMethod(self, 'showNormal', QtCore.Qt.QueuedConnection)
        self.txt_input.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    win = Win()
    win.show()
    sys.exit(app.exec_())
