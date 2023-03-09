import threading
import time

import pyperclip
from PySide6.QtCore import Qt, QThread, Signal, Slot, QEvent
from PySide6.QtWidgets import QWidget, QButtonGroup
from pynput.keyboard import Controller, Key

from ui.home import Ui_Form


class Translator(QThread):
    # 定义一个信号 向外部发送信息
    signal = Signal(str, str)

    def __init__(self, engine, lang_to, translate_text=None):
        super().__init__()
        # 目标语言
        self.source_lang = 'auto'
        self.target_lang = lang_to
        self.translate_text = translate_text
        self.engine = self.import_class(engine)

    @staticmethod
    def import_class(engine):
        if engine == 'Google':
            from api.google import Google
            return Google
        if engine == 'Youdao':
            from api.youdao import Youdao
            return Youdao
        return None

    def run(self):
        target = self.engine(self.translate_text, source_lang=self.source_lang, target_lang=self.target_lang)
        result = target.translate()
        self.signal.emit(self.translate_text, result)


class Home(QWidget, Ui_Form):
    #
    langs = dict(cn='简体中文', auto='自动翻译', en='英语', de='德语', fr='法语', ru='俄语')

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
        # 把界面所有翻译引擎添加到一个组
        self.trs_engine = self.engines_create_group()
        # 是否显示原文
        self.lang_sl.clicked.connect(self.source_lang_toggle)
        # 为界面翻译语言添加选项
        self.lang_to_add()
        # 复制结果
        self.copy.clicked.connect(self.copy_trans)
        # 设置链接
        self.setup_links()
        # 默认隐藏提示
        self.msg.hide()
        # 定义翻译引擎
        self.translator = None

    def setup_links(self):
        # 设置链接
        link = '<a style="text-decoration:none; color:#089185" href="https://fanyi.baidu.com">百度</a>'
        self.link1.setText(link)
        link = '<a style="text-decoration:none; color:#089185" href="https://translate.google.com">谷歌</a>'
        self.link2.setText(link)
        link = '<a style="text-decoration:none; color:#089185" href="https://www.deepl.com/translator">Deepl</a>'
        self.link3.setText(link)

    def lang_to_add(self):
        # 为界面翻译语言添加选项
        for item in self.langs.keys():
            self.lang_to.addItem(self.langs[item], item)
        self.lang_to.currentIndexChanged.connect(self.thread_tr)

    def engines_create_group(self):
        # 为UI界面翻译按键创建一个组
        tr_engines = QButtonGroup(self.hLayout2)
        tr_engines.addButton(self.youdao, 1)
        tr_engines.addButton(self.google, 2)
        # 翻译引擎改变时
        tr_engines.buttonClicked.connect(self.thread_tr)
        return tr_engines

    def selected_text(self):
        # 剪贴板原有内容
        temp = pyperclip.paste()
        # 清空剪贴板内容
        pyperclip.copy('')
        # 发送按键 ctrl + c
        keyboard = Controller()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        time.sleep(0.1)
        # 获取剪贴板内容
        text = pyperclip.paste()
        # 还原剪贴板内容
        pyperclip.copy(temp)
        # 添加文本框
        self.sl_text.setText(text)
        return text

    @Slot()
    def source_lang_toggle(self):
        if self.lang_sl.isChecked():
            self.sl_text.show()
            self.label.show()
        else:
            self.sl_text.hide()
            self.label.hide()

    @Slot()
    def copy_trans(self):
        text = self.tl_text.toPlainText()
        if not text:
            return False
        pyperclip.copy(text)
        self.msg.setText('复制成功')
        self.msg.show()
        t = threading.Thread(target=self.msg_label_hide)
        t.start()

    @Slot()
    def msg_label_hide(self):
        time.sleep(1.5)
        self.msg.hide()

    @Slot()
    def result_out(self, source, target):
        """更新UI界面内容"""
        if self.isHidden():
            self.show()
        self.sl_text.setText(source)
        self.tl_text.setText(target)

    @Slot()
    def show2(self):
        self.show()
        if self.isMinimized():
            self.showNormal()

    @Slot()
    def thread_tr(self, who=None):
        if who == 'hotkey':
            translate_text = self.selected_text()
        else:
            translate_text = self.sl_text.toPlainText()
        if not translate_text:
            return None
        # 获取参数
        engine = self.trs_engine.checkedButton().objectName().capitalize()
        lang_to = self.lang_to.currentData()
        # 创建线程
        self.translator = Translator(engine, lang_to, translate_text)
        self.translator.signal.connect(self.result_out)
        self.translator.start()
        self.show2()

    @Slot()
    def show2(self):
        self.show()
        if self.isMinimized():
            self.showNormal()

    def changeEvent(self, event):
        # """捕获窗口改变事件"""
        if event.type() == QEvent.WindowStateChange:
            # 最小化
            if self.windowState() & Qt.WindowMinimized:
                self.hide()
        super().changeEvent(event)

    #
    def closeEvent(self, event):
        """重写关闭窗口事件"""
        event.ignore()
        # 隐藏窗口
        self.hide()
