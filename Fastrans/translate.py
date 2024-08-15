import urllib.request
import urllib.parse


# GitHub repo: https://github.com/neverneverendup/Translator
# Microsoft Bing
class Bing(object):
    def __init__(self):
        self.url = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?"

    def translate(self, content, from_lan, to_lan):
        data = {'from': '"' + from_lan + '"', 'to': '"' + to_lan + '"', 'texts': '["'}
        data['texts'] += content
        data['texts'] += '"]'
        data['options'] = "{}"
        data['oncomplete'] = 'onComplete_3'
        data['onerror'] = 'onError_3'
        data['_'] = '1430745999189'
        data = urllib.parse.urlencode(data).encode('utf-8')
        url = self.url + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"
        response = urllib.request.urlopen(url)
        str_data = response.read().decode('utf-8')
        if str_data.find('"TranslatedText":') != -1:
            tmp, str_data = str_data.split('"TranslatedText":')
            translate_data = str_data[1:str_data.find('"', 1)]
        else:
            translate_data = '翻译失败'
        return translate_data


if __name__ == '__main__':
    content = 'hello'
    bing = Bing()
    print(bing.translate(content, 'en', 'zh'))
