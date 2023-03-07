import threading
import time
import pyperclip
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from misc.config import config
from views.ui.home import Ui_Form


class Home(QWidget, Ui_Form):

    def __init__(self):
        """
        构造函数
        """
        # 重载父类构造函数
        super().__init__()
        # 初始化界面 接收一个界面类
        self.setupUi(self)
        # 设置窗口置顶 必须放在显示窗口前面执行
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        #
        self.copy.clicked.connect(self.copy_trans)
        #
        self.label8.hide()
        # 显示界面
        self.apply()

    def apply(self):
        link = '<a style="text-decoration:none; color:#089185" href="https://fanyi.baidu.com">百度</a>'
        self.label5.setText(link)
        link = '<a style="text-decoration:none; color:#089185" href="https://translate.google.com">谷歌</a>'
        self.label6.setText(link)
        link = '<a style="text-decoration:none; color:#089185" href="https://www.deepl.com/translator">Deepl</a>'
        self.label7.setText(link)

        if not config.all['source_lang']:
            self.text1.hide()
            self.label2.hide()

    def copy_trans(self):
        text = self.text2.toPlainText()
        if not text:
            return False
        pyperclip.copy(text)
        self.label8.setText('复制成功')
        self.label8.show()
        t = threading.Thread(target=self.label8_hide)
        t.start()

    def label8_hide(self):
        time.sleep(1.5)
        self.label8.hide()

    def result_out(self, original, target, to):
        """更新UI界面内容"""
        self.text1.setText(original)
        self.text2.setText(target)
        self.label4.setText(to)
        self.show()

    def show2(self):
        self.show()
        if self.isMinimized():
            self.showNormal()

    def changeEvent(self, event):
        # 窗口最小化时 隐藏
        if self.windowState() == Qt.WindowMinimized:
            self.hide()

    #
    def closeEvent(self, event):
        """重写关闭窗口事件"""
        event.ignore()
        # 隐藏窗口
        self.hide()
