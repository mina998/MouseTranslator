from PySide6.QtWidgets import QButtonGroup, QMessageBox, QWidget

from misc.config import config
from views.ui.option import Ui_Form


class Option(QWidget, Ui_Form):

    def __init__(self):
        """
        构造函数
        """
        # 重载父类构造函数
        super().__init__()
        # 初始化界面 接收一个界面类
        self.setupUi(self)

        buttons = QButtonGroup(self.groupBox_1)
        buttons.addButton(self.baidu, 1)
        buttons.addButton(self.deepl, 2)
        buttons.addButton(self.google, 3)
        buttons.addButton(self.youdao, 4)
        self.trs_engine = buttons

        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.hide)
        self.apply()

    def save(self):
        # 获取翻译平台
        trs = self.trs_engine.checkedButton()
        # 配置信息
        save_dict = dict(
            trs=trs.objectName(),
            source_lang=self.source_lang.isChecked()
        )
        config.save(save_dict)
        QMessageBox.information(self, '保存成功', '重启软件生效')

    #
    def apply(self):
        trs = getattr(self, config.all['trs'])
        trs.setChecked(True)
        self.source_lang.setChecked(config.all['source_lang'])

    def closeEvent(self, event):
        """重写关闭窗口事件"""
        event.ignore()
        # 隐藏窗口
        self.hide()
