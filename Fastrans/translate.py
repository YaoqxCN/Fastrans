# GitHub repo: https://github.com/minibear2021/cn_bing_translator
from cn_bing_translator import Translator


# Microsoft Bing
class Bing(Translator):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    content = 'hello'
    bing = Bing()
    print(bing.process(content, 'en', 'zh-Hans'))
