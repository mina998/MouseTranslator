# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 300)
        Form.setMinimumSize(QSize(300, 300))
        Form.setMaximumSize(QSize(300, 300))
        icon = QIcon()
        icon.addFile(u":/images/icon/tray.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 10, 4, 10)
        self.groupBox_1 = QGroupBox(Form)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMinimumSize(QSize(0, 100))
        self.groupBox_1.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout = QVBoxLayout(self.groupBox_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.youdao = QRadioButton(self.groupBox_1)
        self.youdao.setObjectName(u"youdao")
        self.youdao.setMinimumSize(QSize(80, 0))
        self.youdao.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.youdao)

        self.baidu = QRadioButton(self.groupBox_1)
        self.baidu.setObjectName(u"baidu")
        self.baidu.setMinimumSize(QSize(80, 0))
        self.baidu.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.baidu)

        self.google = QRadioButton(self.groupBox_1)
        self.google.setObjectName(u"google")
        self.google.setMinimumSize(QSize(80, 0))
        self.google.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.google)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deepl = QRadioButton(self.groupBox_1)
        self.deepl.setObjectName(u"deepl")
        self.deepl.setMinimumSize(QSize(80, 0))
        self.deepl.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.deepl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 60))
        self.groupBox_2.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.source_lang = QCheckBox(self.groupBox_2)
        self.source_lang.setObjectName(u"source_lang")
        self.source_lang.setChecked(True)

        self.horizontalLayout_4.addWidget(self.source_lang)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 60))
        self.groupBox_3.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.shortcut_key = QComboBox(self.groupBox_3)
        self.shortcut_key.addItem("")
        self.shortcut_key.addItem("")
        self.shortcut_key.setObjectName(u"shortcut_key")
        self.shortcut_key.setEnabled(False)
        self.shortcut_key.setDuplicatesEnabled(True)

        self.horizontalLayout_5.addWidget(self.shortcut_key)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout_4.addWidget(self.buttonBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u8bbe\u7f6e", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u7a0b\u5e8f", None))
        self.youdao.setText(QCoreApplication.translate("Form", u"\u6709\u9053", None))
        self.baidu.setText(QCoreApplication.translate("Form", u"\u767e\u5ea6", None))
        self.google.setText(QCoreApplication.translate("Form", u"\u8c37\u6b4c", None))
        self.deepl.setText(QCoreApplication.translate("Form", u"Deepl", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u663e\u793a\u9009\u9879", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u754c\u9762\uff1a", None))
        self.source_lang.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u539f\u6587", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5feb\u6377\u952e\u9009\u9879", None))
        self.shortcut_key.setItemText(0, QCoreApplication.translate("Form", u"Ctrl + \\", None))
        self.shortcut_key.setItemText(1, QCoreApplication.translate("Form", u"Ctrl + =", None))

    # retranslateUi

