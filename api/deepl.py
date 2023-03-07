import openai


class Deepl(object):
    # 这个名字虽然是Deepl 但用的是OpenAI 来做的翻译
    openai.api_key = "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"

    def __init__(self, translate_text, source_lang='auto', target_lang='Chinese'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translate_text = translate_text
        self.trans = dict(
            to='{}->{}'.format(self.source_lang, self.target_lang),
            target=''
        )

    def init_data(self):
        return dict(
            model="text-davinci-003",
            prompt="Translate this into {}:\n\n{}\n\n".format(self.target_lang, self.translate_text),
            temperature=0.3,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

    def translate(self):
        keyword = self.init_data()
        try:
            response = openai.Completion.create(**keyword)
            self.trans['target'] = response.choices[0].text
            print(self.trans['target'])
            return self.trans
        except Exception as e:
            self.trans['target'] = str(e)
            return self.trans


if __name__ == '__main__':
    d = Deepl('Enter an instruction or select a preset, and watch the API respond with a completion that attempts to match the context')
    t = d.translate()
    # print(t)