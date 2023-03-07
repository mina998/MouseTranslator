from urllib.parse import urlencode
import requests


class Google(object):
    #
    url = 'http://translate.google.com/translate_a/single'

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
            client='gtx',
            dt='t',
            dj=1,
            ie='UTF-8',
            sl=self.source_lang,
            tl=self.target_lang,
            q=self.translate_text
        )

    def translate(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        uri = urlencode(self.init_data())
        url = '{}?{}'.format(self.url, uri)
        try:
            response = requests.get(url=url, headers=headers)
            result = response.json()
            result = list(s['trans'] for s in result['sentences'])

            self.trans['target'] = ''.join(result)
            return self.trans
        except requests.exceptions.RequestException as e:
            self.trans['target'] = str(e)
            return self.trans


if __name__ == '__main__':
    g = Google('你好吗? 现在怎么样呀?', source_lang='zh-cn', target_lang='en')
    t = g.translate()
    print(t)
