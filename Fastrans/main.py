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
        self.pushButton.clicked.connect(self.translate)
        self.textEdit.setReadOnly(True)

    # Translate function
    def translate(self):
        source = self.lineEdit.text()
        # Check the language of the source text
        pass
        # Translate
        translator = Bing()
        translation = translator.translate(source, "en", "zh")
        self.textEdit.setText(translation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='dark_cyan.xml', extra=extra, invert_secondary=True)
    win = Win()
    win.show()
    sys.exit(app.exec_())
