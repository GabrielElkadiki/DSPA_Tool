from PyQt5 import QtCore, QtGui, QtWidgets
from back_end import qtGUI, functionList
import sys

app = QtWidgets.QApplication(sys.argv)
main_window_Qdialog = QtWidgets.QDialog()
ui = qtGUI.Ui_main_window_Qdialog()
ui.setupUi(main_window_Qdialog)
ui.compare_past_dates_QPushButton.setEnabled(False)
ui.monthly_maximum_delta_QPushButton.setEnabled(False)
ui.max_delta_QPushButton.setEnabled(False)
ui.compare_past_dates_QSpinBox.setEnabled(False)


def reset_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.reset_data_QPushButton.setEnabled(False)
    ui.console_QTextEdit.setText(functionList.reset())
    ui.compare_past_dates_QPushButton.setEnabled(True)
    ui.monthly_maximum_delta_QPushButton.setEnabled(True)
    ui.max_delta_QPushButton.setEnabled(True)
    ui.compare_past_dates_QSpinBox.setEnabled(True)


def clear_button_event():
    ui.reset_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText("")
    ui.clear_data_QPushButton.setEnabled(False)


def compare_past_dates_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText(functionList.compare_past_dates(ui.compare_past_dates_QSpinBox.value()))


def monthly_maximum_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText(functionList.monthly_maximum_delta())


def max_delta_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText(functionList.max_delta(None))


ui.reset_data_QPushButton.clicked.connect(reset_button_event)
ui.clear_data_QPushButton.clicked.connect(clear_button_event)
ui.compare_past_dates_QPushButton.clicked.connect(compare_past_dates_button_event)
ui.monthly_maximum_delta_QPushButton.clicked.connect(monthly_maximum_button_event)
ui.max_delta_QPushButton.clicked.connect(max_delta_button_event)

main_window_Qdialog.show()
sys.exit(app.exec_())
