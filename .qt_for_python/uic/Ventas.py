# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Ventas(object):
    def setupUi(self, Form_Ventas):
        if not Form_Ventas.objectName():
            Form_Ventas.setObjectName(u"Form_Ventas")
        Form_Ventas.resize(418, 330)
        Form_Ventas.setMinimumSize(QSize(418, 330))
        Form_Ventas.setMaximumSize(QSize(418, 330))
        Form_Ventas.setStyleSheet(u"QWidget{\n"
"background:rgb(42, 42, 42);\n"
"font: 75 italic 12pt \"Arial Narrow\";\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton{\n"
"background:rgb(0, 127, 21);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form_Ventas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form_Ventas)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 300))
        self.groupBox.setMaximumSize(QSize(400, 300))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 3, 1, 1)

        self.label_deuda = QLabel(self.frame)
        self.label_deuda.setObjectName(u"label_deuda")

        self.gridLayout_2.addWidget(self.label_deuda, 1, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_Cambio = QLabel(self.frame)
        self.label_Cambio.setObjectName(u"label_Cambio")

        self.gridLayout_2.addWidget(self.label_Cambio, 8, 2, 1, 1)

        self.line_nombre = QLineEdit(self.frame)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setMaxLength(8)
        self.line_nombre.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_nombre, 0, 2, 1, 2)

        self.btnOk = QPushButton(self.frame)
        self.btnOk.setObjectName(u"btnOk")

        self.gridLayout_2.addWidget(self.btnOk, 8, 4, 1, 1)

        self.lineCantidad = QLineEdit(self.frame)
        self.lineCantidad.setObjectName(u"lineCantidad")
        self.lineCantidad.setMinimumSize(QSize(100, 0))
        self.lineCantidad.setMaximumSize(QSize(50, 16777215))
        self.lineCantidad.setFocusPolicy(Qt.StrongFocus)
        self.lineCantidad.setMaxLength(5)
        self.lineCantidad.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineCantidad, 4, 2, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 2)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_Total = QLabel(self.frame)
        self.label_Total.setObjectName(u"label_Total")

        self.gridLayout_2.addWidget(self.label_Total, 6, 2, 1, 1)

        self.line_Recivo = QLineEdit(self.frame)
        self.line_Recivo.setObjectName(u"line_Recivo")
        self.line_Recivo.setFocusPolicy(Qt.StrongFocus)
        self.line_Recivo.setMaxLength(5)
        self.line_Recivo.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_Recivo, 7, 2, 1, 1)

        self.radioCorazon = QRadioButton(self.frame)
        self.radioCorazon.setObjectName(u"radioCorazon")

        self.gridLayout_2.addWidget(self.radioCorazon, 2, 3, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.linePrecio = QLineEdit(self.frame)
        self.linePrecio.setObjectName(u"linePrecio")
        self.linePrecio.setFocusPolicy(Qt.StrongFocus)
        self.linePrecio.setMaxLength(2)
        self.linePrecio.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.linePrecio, 4, 4, 1, 1)

        self.radioTripa = QRadioButton(self.frame)
        self.radioTripa.setObjectName(u"radioTripa")

        self.gridLayout_2.addWidget(self.radioTripa, 2, 2, 1, 1)

        self.calcular = QRadioButton(self.frame)
        self.calcular.setObjectName(u"calcular")

        self.gridLayout_2.addWidget(self.calcular, 5, 4, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form_Ventas)

        QMetaObject.connectSlotsByName(Form_Ventas)
    # setupUi

    def retranslateUi(self, Form_Ventas):
        Form_Ventas.setWindowTitle(QCoreApplication.translate("Form_Ventas", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_Ventas", u"Ventas", None))
        self.label_2.setText(QCoreApplication.translate("Form_Ventas", u"$", None))
        self.label_deuda.setText(QCoreApplication.translate("Form_Ventas", u"0", None))
        self.label.setText(QCoreApplication.translate("Form_Ventas", u"Cantidad:  KG / Pz", None))
        self.label_4.setText(QCoreApplication.translate("Form_Ventas", u"Cambio:    $", None))
        self.label_3.setText(QCoreApplication.translate("Form_Ventas", u"Total  :", None))
        self.label_Cambio.setText(QCoreApplication.translate("Form_Ventas", u"             0", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("Form_Ventas", u"Nom Cliente", None))
        self.btnOk.setText(QCoreApplication.translate("Form_Ventas", u"Ok", None))
        self.lineCantidad.setText("")
        self.lineCantidad.setPlaceholderText(QCoreApplication.translate("Form_Ventas", u"0", None))
        self.label_8.setText(QCoreApplication.translate("Form_Ventas", u"Cuenta Anterior: ", None))
        self.label_10.setText(QCoreApplication.translate("Form_Ventas", u"Producto : ", None))
        self.label_7.setText(QCoreApplication.translate("Form_Ventas", u"Cliente : ", None))
        self.label_Total.setText(QCoreApplication.translate("Form_Ventas", u"0", None))
        self.line_Recivo.setPlaceholderText(QCoreApplication.translate("Form_Ventas", u"0", None))
        self.radioCorazon.setText(QCoreApplication.translate("Form_Ventas", u"Corazon", None))
        self.label_5.setText(QCoreApplication.translate("Form_Ventas", u"Recivo :      $", None))
        self.linePrecio.setText("")
        self.linePrecio.setPlaceholderText(QCoreApplication.translate("Form_Ventas", u"0", None))
        self.radioTripa.setText(QCoreApplication.translate("Form_Ventas", u"Tripa", None))
        self.calcular.setText(QCoreApplication.translate("Form_Ventas", u"calcular", None))
    # retranslateUi

