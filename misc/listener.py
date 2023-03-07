import time
import pyperclip
from importlib import import_module
from PySide6.QtCore import QObject, Signal
from pynput.keyboard import Controller, Key, Listener
from misc.config import config


class KeyListener(QObject):
    # 定义一个信号 向外部发送信息
    signal = Signal(str, str, str)

    def __init__(self):
        super().__init__()
        self.trs = self.import_api_module()
        self.listen = Listener(on_press=self.on_press)

    def on_press(self, key):
        """发送信号"""
        if str(key) != r"'\x1c'":
            return None
        text = self.get()
        if not text:
            return None
        self.api(text)

    def run(self):
        self.listen.start()

    def api(self, text):
        trs = self.trs(text)
        res = trs.translate()
        self.signal.emit(text, res['target'], res['to'].upper())

    @staticmethod
    def import_api_module():
        trs = config.all['trs']
        api = import_module('api')
        return getattr(api, trs.capitalize())

    @staticmethod
    def get():
        # 剪贴板原有内容
        temp = pyperclip.paste()
        # 清空剪贴板内容
        pyperclip.copy('')
        # 发送按键 ctrl + c
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        time.sleep(0.2)
        # 获取剪贴板内容
        text = pyperclip.paste()
        # 还原剪贴板内容
        pyperclip.copy(temp)
        return text
