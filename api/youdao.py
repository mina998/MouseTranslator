from urllib.parse import urlencode
import requests


class Youdao(object):
    #
    url = 'http://fanyi.youdao.com/translate'

    def __init__(self, translate_text, source_lang='auto', target_lang='zh-CN'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translate_text = translate_text
        self.trans = dict(
            to='{}->{}'.format(self.source_lang, self.target_lang),
            target=''
        )

    def init_data(self):
        return dict(
            doctype='json',
            type='AUTO',
            i=self.translate_text
        )

    def translate(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        uri = urlencode(self.init_data())
        url = '{}?{}'.format(self.url, uri)
        try:
            response = requests.get(url=url, headers=headers)
            result = response.json()
            self.trans['to'] = result['type']
            result = list(sub['tgt'] for item in result['translateResult'] for sub in item)
            self.trans['target'] = ''.join(result)
            return self.trans
        except requests.exceptions.RequestException as e:
            self.trans['target'] = str(e)
            return self.trans


if __name__ == '__main__':
    g = Youdao('你好吗?\n现在怎么样呀?', source_lang='zh-cn', target_lang='en')
    t = g.translate()
    print(t)
