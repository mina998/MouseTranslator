from PySide6.QtCore import Signal
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QMenu, QSystemTrayIcon


class Tray(QWidget):
    #
    signal_show = Signal(bool)
    signal_option = Signal(bool)
    signal_quit = Signal(bool)

    def __init__(self):
        """系统托盘菜单"""
        super().__init__()
        # 创建菜单
        self.menu = QMenu(self)
        # 显示主窗口菜单
        self.show_action = QAction("显示窗口")
        self.show_action.triggered.connect(self.show_signal)
        self.menu.addAction(self.show_action)
        # 设置菜单
        self.option_action = QAction("设置")
        self.option_action.triggered.connect(self.option_signal)
        self.menu.addAction(self.option_action)
        # 退出菜单
        self.quit_action = QAction("退出")
        self.quit_action.triggered.connect(self.quit_signal)
        self.menu.addAction(self.quit_action)

        # 设置托盘图标，图片必须为正方形
        self.icon_action = QSystemTrayIcon(QIcon(u":/images/icon/tray.png"))
        self.icon_action.setContextMenu(self.menu)
        # 在系统托盘显示此对象
        self.icon_action.show()

    def show_signal(self):
        self.signal_show.emit(True)

    def option_signal(self):
        self.signal_option.emit(True)

    def quit_signal(self):
        self.signal_quit.emit(True)
        self.quit_action = None
        self.icon_action = None
        self.menu = None

