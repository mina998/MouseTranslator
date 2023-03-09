import sys

from PySide6.QtCore import QTranslator, QObject, Signal
from PySide6.QtWidgets import QApplication
from pynput.keyboard import Listener

from home import Home
from tray import Tray


class KeyListener(QObject):
    # 定义一个信号 向外部发送信息
    signal = Signal(str)

    def on_press(self, key):
        """发送信号"""
        if str(key) == r"'\x1c'":
            self.signal.emit('hotkey')

    def __init__(self):
        super().__init__()
        self.hotkey = Listener(on_press=self.on_press)


if __name__ == '__main__':
    #
    listen = KeyListener()
    #
    app = QApplication(sys.argv)
    # 翻译右键菜单
    translator = QTranslator()
    translator.load('zh_CN.qm')
    app.installTranslator(translator)

    # 主窗口
    home = Home()
    # 托盘菜单
    tray = Tray(app, home)
    # 链接到槽
    listen.signal.connect(home.thread_tr)
    # 开启键盘监听
    listen.hotkey.start()

    sys.exit(app.exec())
