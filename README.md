# Fastrans

当前版本 / Now Version: 0.0.0

## 简介 / Introduction

Fastrans 是一个美观、简约的翻译工具，支持多种语言。
目前只支持微软必应翻译，已经中英互译。

Fastrans is a pretty and simple translation tool, which supports multiple languages.
Now it only supports Microsoft Bing translation and Chinese-English translation.

## 技术 / Technology

- Python 3.12
- 使用 cn_bing_translator 库获取必应翻译结果 / Use cn_bing_translator to get Bing translation results
- 使用 PyQt5 构建 GUI / Use PyQt5 to build GUI
- 使用 qt-material 主题美化界面 / Use qt-material to beautify the GUI

## 使用 / Usage

```cmd
git clone https://github.com/YaoqxCN/Fastrans.git
cd Fastrans
pip install -r requirements.txt
python Fastrans/main.py
```

## 待办 / Todo

**欢迎 PR！**

- ENTER 进行翻译 / Use ENTER to translate
- 自动检测语言 / Auto detect language
- 选择语言 / Select language by users
- 翻译历史记录 / Translation history