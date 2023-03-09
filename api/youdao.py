from urllib.parse import urlencode
import requests


class Youdao(object):
    #
    url = 'http://fanyi.youdao.com/translate'

    langs = dict(
        auto='AUTO',
        cn='ZH_CN',
        en='EN',
        de='DE',
        fr='FR',
        ru='RU'
    )

    def __init__(self, translate_text, source_lang, target_lang):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translate_text = translate_text

    def init_data(self):
        return dict(
            doctype='json',
            type='AUTO',
            i=self.translate_text
        )

    def translate(self):
        uri = urlencode(self.init_data())
        url = '{}?{}'.format(self.url, uri)
        try:
            response = requests.get(url=url)
            result = response.json()
            if result['errorCode']:
                return 'error: {} {}'.format(result['errorCode'], '不支持的翻译类型')
            result = list(sub['tgt'] for item in result['translateResult'] for sub in item)
            return ''.join(result)
        except requests.exceptions.RequestException as e:
            return str(e)


if __name__ == '__main__':
    g = Youdao('你好吗?\n现在怎么样呀?', source_lang='zh-cn', target_lang='en')
    t = g.translate()
    print(t)
