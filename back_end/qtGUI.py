# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window_Qdialog(object):
    def setupUi(self, main_window_Qdialog):
        main_window_Qdialog.setObjectName("main_window_Qdialog")
        main_window_Qdialog.resize(1053, 1047)
        main_window_Qdialog.setSizeGripEnabled(False)
        main_window_Qdialog.setModal(False)
        self.console_QTextEdit = QtWidgets.QTextEdit(main_window_Qdialog)
        self.console_QTextEdit.setGeometry(QtCore.QRect(60, 60, 581, 931))
        self.console_QTextEdit.setReadOnly(True)
        self.console_QTextEdit.setObjectName("console_QTextEdit")
        self.widget = QtWidgets.QWidget(main_window_Qdialog)
        self.widget.setGeometry(QtCore.QRect(680, 70, 336, 418))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.compare_past_dates_QPushButton = QtWidgets.QPushButton(self.widget)
        self.compare_past_dates_QPushButton.setObjectName("compare_past_dates_QPushButton")
        self.horizontalLayout.addWidget(self.compare_past_dates_QPushButton)
        self.compare_past_dates_QSpinBox = QtWidgets.QSpinBox(self.widget)
        self.compare_past_dates_QSpinBox.setObjectName("compare_past_dates_QSpinBox")
        self.horizontalLayout.addWidget(self.compare_past_dates_QSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.monthly_maximum_delta_QPushButton = QtWidgets.QPushButton(self.widget)
        self.monthly_maximum_delta_QPushButton.setObjectName("monthly_maximum_delta_QPushButton")
        self.verticalLayout.addWidget(self.monthly_maximum_delta_QPushButton)
        self.max_delta_QPushButton = QtWidgets.QPushButton(self.widget)
        self.max_delta_QPushButton.setObjectName("max_delta_QPushButton")
        self.verticalLayout.addWidget(self.max_delta_QPushButton)
        self.reset_data_QPushButton = QtWidgets.QPushButton(self.widget)
        self.reset_data_QPushButton.setObjectName("reset_data_QPushButton")
        self.verticalLayout.addWidget(self.reset_data_QPushButton)
        self.clear_data_QPushButton = QtWidgets.QPushButton(self.widget)
        self.clear_data_QPushButton.setObjectName("clear_data_QPushButton")
        self.verticalLayout.addWidget(self.clear_data_QPushButton)
        self.monthly_maximum_delta_QPushButton.raise_()
        self.compare_past_dates_QPushButton.raise_()
        self.max_delta_QPushButton.raise_()
        self.reset_data_QPushButton.raise_()
        self.clear_data_QPushButton.raise_()
        self.compare_past_dates_QSpinBox.raise_()
        self.compare_past_dates_QSpinBox.raise_()
        self.console_QTextEdit.raise_()

        self.retranslateUi(main_window_Qdialog)
        QtCore.QMetaObject.connectSlotsByName(main_window_Qdialog)

    def retranslateUi(self, main_window_Qdialog):
        _translate = QtCore.QCoreApplication.translate
        main_window_Qdialog.setWindowTitle(_translate("main_window_Qdialog", "Stock Price Analysis"))
        self.compare_past_dates_QPushButton.setText(_translate("main_window_Qdialog", "Compare Past Dates"))
        self.monthly_maximum_delta_QPushButton.setText(_translate("main_window_Qdialog", "Monthly Maximum Delta"))
        self.max_delta_QPushButton.setText(_translate("main_window_Qdialog", "Max Delta"))
        self.reset_data_QPushButton.setText(_translate("main_window_Qdialog", "Reset Data"))
        self.clear_data_QPushButton.setText(_translate("main_window_Qdialog", "Clear"))


