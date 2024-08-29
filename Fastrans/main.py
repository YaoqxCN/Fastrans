from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from qfluentwidgets import Theme, setTheme
import eng_to_ipa as ipa
import pyperclip
import sys
import ctypes

from ui import Ui
from translate import Translator


# Main window class
class Win(QMainWindow, Ui):
    def __init__(self):
        super().__init__()
        self.btn_trans.clicked.connect(self.translate)
        self.btn_trans.setShortcut('Return')  # Shortcut key
        self.now_translation = ""
        self.btn_copy.clicked.connect(lambda: pyperclip.copy(self.now_translation))
        self.btn_theme.toggled.connect(self.switch_theme)
        self.btn_topmost.toggled.connect(self.topmost)

    # Translate function
    def translate(self):
        content = self.txt_input.text()

        # Check if source is empty
        if not content:
            return

        # Detect language
        if content[0] < '\u4e00' or content[0] > '\u9fff':
            from_lang = 'auto'
            to_lang = 'zh'
        else:
            from_lang = 'zh'
            to_lang = 'en'

        # Translate
        source = self.combo_platform.currentText()
        translator = Translator(content=content, from_lang=from_lang, to_lang=to_lang, source=source)
        translation = translator.translate()
        self.txt_result.setText(translation)
        self.now_translation = translation

        # 音标
        result = ipa.convert(translation if from_lang == 'zh' else content)
        self.txt_result.append('\n[' + result + ']')

    # Switch theme function
    def switch_theme(self, is_toggled):
        self.setStyleSheet("background-color: #272727" if is_toggled else "background-color: #f7f9fc")
        setTheme(Theme.DARK if is_toggled else Theme.LIGHT)

    # Topmost
    def topmost(self, is_toggled):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint if is_toggled else QtCore.Qt.Widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    win = Win()
    win.show()
    sys.exit(app.exec_())
