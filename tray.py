from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction


class Tray(QSystemTrayIcon):

    def __init__(self, app=None, parent=None):
        super().__init__()
        self.app = app
        self.parent = parent

        # 设置托盘图标
        self.setIcon(QIcon(u":/images/icon/tray.png"))
        # 创建菜单项
        item_show = QAction("显示", self)
        item_quit = QAction("退出", self)
        item_show.triggered.connect(self.parent.show2)
        item_quit.triggered.connect(self.app.quit)
        # 设置菜单
        menu = QMenu()
        menu.addAction(item_show)
        menu.addAction(item_quit)
        self.setContextMenu(menu)

        # 捕获托盘菜单图标的双击事件
        self.activated.connect(self.on_tray_icon_activated)
        self.show()

    def on_tray_icon_activated(self, reason):
        # DoubleClick 双击  Trigger 单击
        if reason == QSystemTrayIcon.Trigger:
            self.parent.show2()
