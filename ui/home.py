# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 380)
        icon = QIcon()
        icon.addFile(u":/images/icon/tray.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 8, 3, 6)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(99999, 16777215))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.sl_text = QTextEdit(Form)
        self.sl_text.setObjectName(u"sl_text")

        self.verticalLayout.addWidget(self.sl_text)

        self.hLayout2 = QHBoxLayout()
        self.hLayout2.setSpacing(5)
        self.hLayout2.setObjectName(u"hLayout2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout2.addItem(self.horizontalSpacer)

        self.lang_sl = QCheckBox(Form)
        self.lang_sl.setObjectName(u"lang_sl")
        self.lang_sl.setChecked(True)

        self.hLayout2.addWidget(self.lang_sl)

        self.lang_to = QComboBox(Form)
        self.lang_to.setObjectName(u"lang_to")
        self.lang_to.setMinimumSize(QSize(80, 0))

        self.hLayout2.addWidget(self.lang_to)


        self.verticalLayout.addLayout(self.hLayout2)

        self.tl_text = QTextEdit(Form)
        self.tl_text.setObjectName(u"tl_text")

        self.verticalLayout.addWidget(self.tl_text)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.link1 = QLabel(Form)
        self.link1.setObjectName(u"link1")
        font1 = QFont()
        font1.setUnderline(False)
        self.link1.setFont(font1)
        self.link1.setStyleSheet(u"")
        self.link1.setLineWidth(1)
        self.link1.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.link1)

        self.link2 = QLabel(Form)
        self.link2.setObjectName(u"link2")
        self.link2.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.link2)

        self.link3 = QLabel(Form)
        self.link3.setObjectName(u"link3")
        self.link3.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.link3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.msg = QLabel(Form)
        self.msg.setObjectName(u"msg")
        self.msg.setEnabled(True)
        self.msg.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.horizontalLayout.addWidget(self.msg)

        self.copy = QPushButton(Form)
        self.copy.setObjectName(u"copy")
        self.copy.setMinimumSize(QSize(62, 28))
        self.copy.setMaximumSize(QSize(62, 30))

        self.horizontalLayout.addWidget(self.copy)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1-\u5b8f\u70ed\u952e \u3010Ctrl+\\\u3011 ", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u539f\u6587  [\u6709\u9053\u4ec5\u652f\u6301\u81ea\u52a8\u7ffb\u8bd1]", None))
        self.lang_sl.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u539f\u6587", None))
        self.link1.setText(QCoreApplication.translate("Form", u"\u767e\u5ea6", None))
        self.link2.setText(QCoreApplication.translate("Form", u"\u8c37\u6b4c", None))
        self.link3.setText(QCoreApplication.translate("Form", u"Deepl", None))
        self.msg.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
    # retranslateUi

