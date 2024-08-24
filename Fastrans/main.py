from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, Qt
from qt_material import apply_stylesheet
from qtawesome import font
import eng_to_ipa as ipa
import pyperclip
import sys

from ui import Ui_Form
from translate import Translator

# Extra theme setting
extra = {
    'font_family': '微软雅黑',
    'font_size': '12'
}


# Main window class
class Win(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_trans.clicked.connect(self.translate)
        self.pushButton_trans.setShortcut('Return')  # Shortcut key
        self.now_translation = ""

        # Copy button
        self.pushButton_copy.setFont(font('fa', 16))
        self.pushButton_copy.setText("")
        self.pushButton_copy.clicked.connect(lambda: pyperclip.copy(self.now_translation))

        # Switch theme
        self.themes = ['dark_cyan.xml', 'light_blue.xml']
        self.theme_name = ['深色', '浅色']
        self.theme_index = 1
        self.pushButton_theme.clicked.connect(self.switch_theme)

        # Topmost
        self.is_topmost = False
        self.pushButton_topmost.clicked.connect(self.topmost)

    # Translate function
    def translate(self):
        content = self.lineEdit_input.text()

        # Check if source is empty
        if content == "":
            return

        # Detect language
        if 'a' <= content[0] <= 'z' or 'A' <= content[0] <= 'Z':
            from_lang = 'en'
            to_lang = 'zh'
        elif content[0] < '\u4e00' or content[0] > '\u9fff':
            from_lang = 'auto'
            to_lang = 'zh'
        else:
            from_lang = 'zh'
            to_lang = 'en'

        # Translate
        source = self.comboBox.currentText()
        translator = Translator(content=content, from_lang=from_lang, to_lang=to_lang, source=source)
        translation = translator.translate()
        self.textEdit_result.setText(translation)
        self.now_translation = translation

        # 音标
        if from_lang == 'zh':
            result = ipa.convert(translation)
            self.textEdit_result.append('\n['+result+']')
        elif from_lang == 'en':
            result = ipa.convert(content)
            self.textEdit_result.append('\n['+result+']')

    # Switch theme function
    def switch_theme(self):
        self.theme_index = 1 - self.theme_index
        apply_stylesheet(self, theme=self.themes[self.theme_index], extra=extra, invert_secondary=True)
        self.pushButton_theme.setText(self.theme_name[self.theme_index])
        if self.theme_index == 0:
            self.comboBox.setStyleSheet("QComboBox{color: white;}")
        else:
            self.comboBox.setStyleSheet("QComboBox{color: black;}")

    # Topmost
    def topmost(self):
        if self.is_topmost:
            self.setWindowFlags(QtCore.Qt.Widget)
            self.show()
        else:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        self.is_topmost = not self.is_topmost


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml', extra=extra, invert_secondary=True)
    win = Win()
    win.show()
    sys.exit(app.exec_())
