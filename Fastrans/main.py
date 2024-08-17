from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet
from qtawesome import icon, font
import sys

from ui import Ui_Form
from translate import Translator

# Extra theme setting
extra = {
    'font_family': '微软雅黑',
    'font_size': '10'
}


# Main window class
class Win(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_trans.clicked.connect(self.translate)
        self.pushButton_trans.setShortcut('Return')  # Shortcut key

        # Copy button
        self.pushButton_copy.setFont(font('fa', 16))
        self.pushButton_copy.setText("")
        self.pushButton_copy.clicked.connect(self.copy)

        # Switch theme
        self.themes = ['dark_cyan.xml', 'light_blue.xml']
        self.theme_name = ['深色', '浅色']
        self.theme_index = 1
        self.pushButton_theme.clicked.connect(self.switch_theme)

    # Translate function
    def translate(self):
        content = self.lineEdit_input.text()
        # Check if source is empty
        if content == "":
            return
        # Detect language
        if content[0] < '\u4e00' or content[0] > '\u9fff':
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

    # Switch theme function
    def switch_theme(self):
        self.theme_index = 1 - self.theme_index
        apply_stylesheet(self, theme=self.themes[self.theme_index], extra=extra, invert_secondary=True)
        self.pushButton_theme.setText(self.theme_name[self.theme_index])
        if self.theme_index == 0:
            self.comboBox.setStyleSheet("QComboBox{color: white;}")
        else:
            self.comboBox.setStyleSheet("QComboBox{color: black;}")

    # Copy function
    def copy(self):
        self.textEdit_result.selectAll()
        self.textEdit_result.copy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml', extra=extra, invert_secondary=True)
    win = Win()
    win.show()
    sys.exit(app.exec_())
