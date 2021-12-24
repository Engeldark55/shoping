# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Producto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Producto(object):
    def setupUi(self, Form_Producto):
        if not Form_Producto.objectName():
            Form_Producto.setObjectName(u"Form_Producto")
        Form_Producto.resize(180, 172)
        Form_Producto.setMinimumSize(QSize(180, 172))
        Form_Producto.setMaximumSize(QSize(180, 172))
        Form_Producto.setStyleSheet(u"QWidget{\n"
"background:rgb(22, 52, 136);\n"
"font: 75 italic 10pt \"Arial\";\n"
"color:white;\n"
"}\n"
"QPushButton{\n"
"background:rgb(98, 153, 255);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form_Producto)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form_Producto)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(180, 172))
        self.groupBox.setMaximumSize(QSize(180, 172))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton)


        self.gridLayout_3.addWidget(self.frame, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form_Producto)

        QMetaObject.connectSlotsByName(Form_Producto)
    # setupUi

    def retranslateUi(self, Form_Producto):
        Form_Producto.setWindowTitle(QCoreApplication.translate("Form_Producto", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_Producto", u"Producto", None))
        self.label.setText(QCoreApplication.translate("Form_Producto", u"Numero:", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"socio", None))
        self.label_2.setText(QCoreApplication.translate("Form_Producto", u"Tripa", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form_Producto", u"Corazon", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form_Producto", u"ok", None))
    # retranslateUi

