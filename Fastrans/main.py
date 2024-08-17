from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet
import sys

from ui import Ui_Form
from translate import Bing

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

        # Switch theme
        self.themes = ['dark_cyan.xml', 'light_blue.xml']
        self.theme_name = ['深色', '浅色']
        self.theme_index = 0
        self.pushButton_theme.clicked.connect(self.switch_theme)

    # Translate function
    def translate(self):
        source = self.lineEdit_input.text()
        # Check if source is empty
        if source == "":
            return
        # Detect language
        if source[0] < '\u4e00' or source[0] > '\u9fff':
            from_lang = 'en'
            to_lang = 'zh-Hans'
        else:
            from_lang = 'zh-Hans'
            to_lang = 'en'
        # Translate
        translator = Bing()
        translation = translator.process(source, from_lang, to_lang)
        self.textEdit_result.setText(translation)

    def switch_theme(self):
        self.theme_index = 1 - self.theme_index
        apply_stylesheet(self, theme=self.themes[self.theme_index], extra=extra, invert_secondary=True)
        self.pushButton_theme.setText(self.theme_name[self.theme_index])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml', extra=extra, invert_secondary=True)
    win = Win()
    win.show()
    sys.exit(app.exec_())
