from urllib.parse import urlencode
import requests


class Google(object):
    #
    url = 'http://translate.google.com/translate_a/single'

    langs = dict(
        auto='auto',
        cn='zh-CN',
        en='en',
        de='de',
        fr='fr',
        ru='ru'
    )

    def __init__(self, translate_text, source_lang, target_lang):
        self.source_lang = source_lang
        self.target_lang = self.langs[target_lang]
        self.translate_text = translate_text

    def init_data(self):
        return dict(
            client='gtx',
            dt='t',
            dj=1,
            ie='UTF-8',
            sl=self.source_lang,
            tl=self.target_lang,
            q=self.translate_text
        )

    def translate(self):

        uri = urlencode(self.init_data())
        url = '{}?{}'.format(self.url, uri)
        try:
            response = requests.get(url=url)
            result = response.json()
            result = list(s['trans'] for s in result['sentences'])
            return ''.join(result)
        except requests.exceptions.RequestException as e:
            return str(e)


if __name__ == '__main__':
    g = Google('你好吗? 现在怎么样呀?', source_lang='zh-cn', target_lang='ru')
    t = g.translate()
    print(t)
