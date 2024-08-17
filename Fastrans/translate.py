# GitHub repo: https://github.com/UlionTse/translators
import translators as ts


# Microsoft Bing
class Translator:
    def __init__(self, content, from_lang, to_lang, source):
        self.translators = {
            "必应": "bing",
            "有道": "youdao",
            "搜狗": "sogou",
        }
        self.content = content
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.source = source

    def translate(self):
        self.translation = ts.translate_text(self.content, self.translators[self.source], self.from_lang, self.to_lang)
        return self.translation


if __name__ == "__main__":
    translation = Translator("你好", "zh", "en", "必应")
    translation = translation.translate()
    print(translation.translation)
