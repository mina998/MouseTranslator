import requests
import random
from hashlib import md5


class Baidu(object):
    # API变量
    app_id = '20210414000778757'
    app_key = 'MS2GXGWnRJpMPGIHBAQN'
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

    langs = dict(
        cn='zh',
        en='en',
        de='de',
        fr='fra',
        ru='ru'
    )

    def __init__(self, translate_text, source_lang='auto', target_lang='auto'):
        self.source_lang = source_lang
        self.target_lang = self.langs[target_lang]
        self.translate_text = translate_text

    def init_data(self):
        salt = random.randint(32768, 65536)
        salt = str(salt)
        sign = self.make_md5(self.app_id + self.translate_text + salt + self.app_key)
        payload = dict(
            appid=self.app_id,
            q=self.translate_text,
            to=self.target_lang,
            salt=salt,
            sign=sign
        )
        payload['from'] = self.source_lang
        return payload

    @staticmethod
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            # 发送 POST 请求，并获取响应对象
            response = requests.post(self.url, params=self.init_data(), headers=headers)
            result = response.json()
            if 'error_code' in result:
                return '{}:{}'.format(result['error_code'], result['error_msg'])
            else:
                target = list(t['dst'] for t in result['trans_result'])
                return '\n'.join(target)
        except requests.exceptions.RequestException as e:
            return str(e)


if __name__ == '__main__':
    # bd = Baidu('When using the non-blocking version of the above, the current thread will continue to execute.')
    bd = Baidu('当使用上述非阻塞版本时，当前线程将继续执行.', 'auto', 'en')
    tr = bd.translate()
    print(tr)
