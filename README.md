# Fastrans

当前版本 / Now Version: 0.0.0 （开发中 / Developing）

## 📄 简介 / Introduction

Fastrans 是一个美观、简约的翻译工具，支持多种语言。
目前支持微必应、有道、搜狗翻译，以及中英互译，显示音标等。

Fastrans is a pretty and simple translation tool, which supports multiple languages.
Now it supports Bing, Youdao, Sogou translation, English-Chinese translation, phonetic symbol and so on.

## ✨ 功能 / Features

- 英汉互译 / English-Chinese translation
- 其他语种自动翻译中文 / Automatically translate other languages to Chinese
- 明暗主题切换 / Switch between light and dark mode
- 可选不同翻译平台（支持必应、有道、搜狗）/ Optional different translation platforms (support Bing, Youdao, Sogou)
- 可显示音标 / Available to show phonetic symbol

## ✒ 技术 / Technology

- Python 3.12
- 使用 translators 库获取不同平台翻译结果 / Use translators to get results from different platforms
- 使用 PyQt5 构建 GUI / Use PyQt5 to build GUI
- 使用 qt-material 主题美化界面 / Use qt-material to beautify the GUI
- 使用 eng_to_ipa 显示音标 / Use eng_to_ipa to show phonetic symbol

## 🔍 使用 / Usage

```cmd
git clone https://github.com/YaoqxCN/Fastrans.git
cd Fastrans
pip install -r requirements.txt
python Fastrans/main.py
```

## 📝 待办 / Todo

**欢迎 PR！**

- ~~ENTER 进行翻译 / Use ENTER to translate~~
- ~~英汉互译 / English-Chinese translation~~
- ~~切换翻译引擎 / Switch translation engine~~
- ~~明暗模式转换 / Switch between light and dark mode~~
- ~~翻译结果复制到剪贴板 / Copy translation results to clipboard~~
- 翻译历史记录 / Translation history
- ~~显示音标 / Show phonetic symbols~~
- 快捷键弹出窗口 / Pop up window with shortcut keys