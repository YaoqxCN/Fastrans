from PyQt5.QtWidgets import QApplication, QMainWindow
import qt_material
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
        self.pushButton_2.clicked.connect(self.translate)
        self.pushButton_2.setShortcut('Return')  # Shortcut key
        self.comboBox.setStyleSheet("QComboBox{color: white;}")

    # Translate function
    def translate(self):
        source = self.lineEdit.text()
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
        self.textEdit.setText(translation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='dark_cyan.xml', extra=extra, invert_secondary=True)
    win = Win()
    win.show()
    sys.exit(app.exec_())
