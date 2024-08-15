from PyQt5.QtWidgets import QApplication, QMainWindow
import qt_material
import translate
import sys

from ui import Ui_Form


# Main window class
class Win(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.translate)

    # Translate function
    def translate(self):
        sentence = self.lineEdit.text()
        print(sentence)
        translator = translate.Translator(to_lang="zh")
        result = translator.translate(sentence)
        self.textEdit.setText(result)
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='dark_teal.xml', extra={'font_family': '微软雅黑', 'font_size': '10'})
    win = Win()
    win.show()
    sys.exit(app.exec_())
