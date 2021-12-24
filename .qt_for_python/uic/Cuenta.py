# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cuenta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Cuenta(object):
    def setupUi(self, Form_Cuenta):
        if not Form_Cuenta.objectName():
            Form_Cuenta.setObjectName(u"Form_Cuenta")
        Form_Cuenta.resize(550, 300)
        Form_Cuenta.setMinimumSize(QSize(550, 300))
        Form_Cuenta.setMaximumSize(QSize(550, 300))
        Form_Cuenta.setStyleSheet(u"QWidget{\n"
"background:rgb(42, 42, 42);\n"
"font: 75 italic 12pt \"Arial Narrow\";\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton{\n"
"background:rgb(0, 127, 21);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form_Cuenta)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form_Cuenta)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(529, 287))
        self.groupBox.setMaximumSize(QSize(550, 300))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 210))
        self.frame.setMaximumSize(QSize(400, 250))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_ok = QPushButton(self.frame)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(310, 210, 75, 23))
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-10, 0, 420, 170))
        self.tableWidget.setMinimumSize(QSize(420, 170))
        self.tableWidget.setMaximumSize(QSize(420, 160))
        self.tableWidget.setStyleSheet(u"background:white;\n"
"color:black;")
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 180, 101, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(150, 170, 111, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_Nombre = QLineEdit(self.verticalLayoutWidget_2)
        self.line_Nombre.setObjectName(u"line_Nombre")
        self.line_Nombre.setMaxLength(8)
        self.line_Nombre.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.line_Nombre)

        self.line_cantidad = QLineEdit(self.verticalLayoutWidget_2)
        self.line_cantidad.setObjectName(u"line_cantidad")
        self.line_cantidad.setMaxLength(5)
        self.line_cantidad.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.line_cantidad)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form_Cuenta)

        QMetaObject.connectSlotsByName(Form_Cuenta)
    # setupUi

    def retranslateUi(self, Form_Cuenta):
        Form_Cuenta.setWindowTitle(QCoreApplication.translate("Form_Cuenta", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_Cuenta", u"Cuenta", None))
        self.btn_ok.setText(QCoreApplication.translate("Form_Cuenta", u"ok", None))
        self.label.setText(QCoreApplication.translate("Form_Cuenta", u"Cliente:  ", None))
        self.label_2.setText(QCoreApplication.translate("Form_Cuenta", u"Acuenta  :   ", None))
        self.line_Nombre.setPlaceholderText(QCoreApplication.translate("Form_Cuenta", u"Nombre", None))
        self.line_cantidad.setPlaceholderText(QCoreApplication.translate("Form_Cuenta", u"$0000", None))
    # retranslateUi

