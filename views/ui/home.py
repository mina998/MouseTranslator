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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 296)
        icon = QIcon()
        icon.addFile(u":/images/icon/tray.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 6)
        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")
        self.label2.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(9)
        font.setBold(False)
        self.label2.setFont(font)

        self.verticalLayout.addWidget(self.label2)

        self.text1 = QTextEdit(Form)
        self.text1.setObjectName(u"text1")

        self.verticalLayout.addWidget(self.text1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label3 = QLabel(Form)
        self.label3.setObjectName(u"label3")

        self.horizontalLayout_2.addWidget(self.label3)

        self.label8 = QLabel(Form)
        self.label8.setObjectName(u"label8")
        self.label8.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.horizontalLayout_2.addWidget(self.label8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label4 = QLabel(Form)
        self.label4.setObjectName(u"label4")
        self.label4.setMinimumSize(QSize(55, 0))
        font1 = QFont()
        font1.setPointSize(8)
        self.label4.setFont(font1)
        self.label4.setStyleSheet(u"color:rgb(255, 85, 0)")

        self.horizontalLayout_2.addWidget(self.label4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.text2 = QTextEdit(Form)
        self.text2.setObjectName(u"text2")

        self.verticalLayout.addWidget(self.text2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label5 = QLabel(Form)
        self.label5.setObjectName(u"label5")
        font2 = QFont()
        font2.setUnderline(False)
        self.label5.setFont(font2)
        self.label5.setStyleSheet(u"")
        self.label5.setLineWidth(1)
        self.label5.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label5)

        self.label6 = QLabel(Form)
        self.label6.setObjectName(u"label6")
        self.label6.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label6)

        self.label7 = QLabel(Form)
        self.label7.setObjectName(u"label7")
        self.label7.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label7)

        self.space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.space)

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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9009\u4e2d\u7ffb\u8bd1", None))
        self.label2.setText(QCoreApplication.translate("Form", u"\u539f\u6587", None))
        self.label3.setText(QCoreApplication.translate("Form", u"\u8bd1\u6587", None))
        self.label8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label4.setText(QCoreApplication.translate("Form", u"EN->ZH", None))
        self.label5.setText(QCoreApplication.translate("Form", u"\u767e\u5ea6", None))
        self.label6.setText(QCoreApplication.translate("Form", u"\u8c37\u6b4c", None))
        self.label7.setText(QCoreApplication.translate("Form", u"Deepl", None))
        self.copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u7ed3\u679c", None))
    # retranslateUi

