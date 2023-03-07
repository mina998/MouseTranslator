import sys

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication

from views.home import Home
from views.option import Option
from views.tray import Tray
from misc.listener import KeyListener
import resource_rc
# 创建键盘监听器
listen = KeyListener()

if __name__ == '__main__':
    #
    app = QApplication(sys.argv)
    # 翻译右键菜单
    translator = QTranslator()
    translator.load('zh_CN.qm')
    app.installTranslator(translator)

    # 主窗口
    home = Home()
    # 设置窗口
    option = Option()
    # 托盘菜单
    tray = Tray()
    # 显示主窗口
    tray.signal_show.connect(home.show2)
    # 显示设置窗口
    tray.signal_option.connect(option.show)
    # 退出程序
    tray.signal_quit.connect(app.quit)
    # 链接到槽
    listen.signal.connect(home.result_out)
    # 开启键盘监听
    listen.run()

    sys.exit(app.exec())
