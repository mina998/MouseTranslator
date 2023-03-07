import json
import os


class Config(object):
    # 配置文件
    file_path = './configs'
    all = {}

    def __init__(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.all = json.load(f)

    def save(self, content: dict):
        with open(self.file_path, 'w') as f:
            json.dump(content, f)


config = Config()
