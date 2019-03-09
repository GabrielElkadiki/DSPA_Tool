from PyQt5 import QtCore, QtGui, QtWidgets
from back_end import qtGUI, functionList
import sys

app = QtWidgets.QApplication(sys.argv)
main_window_Qdialog = QtWidgets.QDialog()
ui = qtGUI.Ui_main_window_Qdialog()
ui.setupUi(main_window_Qdialog)


def reset_button_event():
    ui.reset_data_QPushButton.setEnabled(False)
    ui.console_QTextEdit.setText(functionList.reset())


def clear_button_event():
    ui.reset_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText("")


def compare_past_dates_button_event():
    ui.console_QTextEdit.setText("WOWOWOW")


ui.reset_data_QPushButton.clicked.connect(reset_button_event)
ui.clear_data_QPushButton.clicked.connect(clear_button_event)
ui.compare_past_dates_QPushButton.clicked.connect(compare_past_dates_button_event)

main_window_Qdialog.show()
sys.exit(app.exec_())
