from PyQt5 import QtWidgets
from spat import qtGUI, functions
import sys

app = QtWidgets.QApplication(sys.argv)
main_window_Qdialog = QtWidgets.QDialog()
ui = qtGUI.Ui_main_window_Qdialog()
ui.setupUi(main_window_Qdialog)
ui.compare_past_dates_QPushButton.setEnabled(False)
ui.monthly_maximum_delta_QPushButton.setEnabled(False)
ui.max_delta_QPushButton.setEnabled(False)
ui.calculate_price_delta_QPushButton.setEnabled(False)
ui.clear_data_QPushButton.setEnabled(False)
ui.get_data_QPushButton.setEnabled(False)
ui.start_date_dateEdit.setDate(functions.get_date_today_plus_num_days(0))
ui.stop_date_dateEdit.setDate(functions.get_date_today_plus_num_days(1))


def get_data_button_event():
    functions.clear_data()
    ui.get_data_QPushButton.setEnabled(False)
    ui.clear_data_QPushButton.setEnabled(True)
    if not ui.symbol_QLineEdit.text():
        ui.console_QTextEdit.setText("Please Enter a Symbol")
        return
    reset_return = functions.reset(ui.symbol_QLineEdit.text().upper())
    if not reset_return:
        ui.console_QTextEdit.setText("SYMBOL UNAVAILABLE"
                                     "\nEnsure API has access to the internet and Symbol provided is valid")
        ui.compare_past_dates_QPushButton.setEnabled(False)
        ui.monthly_maximum_delta_QPushButton.setEnabled(False)
        ui.max_delta_QPushButton.setEnabled(False)
        ui.calculate_price_delta_QPushButton.setEnabled(False)
    else:
        ui.console_QTextEdit.setText(str(reset_return))
        ui.compare_past_dates_QPushButton.setEnabled(True)
        ui.monthly_maximum_delta_QPushButton.setEnabled(True)
        ui.max_delta_QPushButton.setEnabled(True)
        ui.calculate_price_delta_QPushButton.setEnabled(True)


def clear_button_event():
    ui.get_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText("")
    ui.clear_data_QPushButton.setEnabled(False)
    ui.compare_past_dates_QPushButton.setEnabled(False)
    ui.monthly_maximum_delta_QPushButton.setEnabled(False)
    ui.max_delta_QPushButton.setEnabled(False)
    ui.calculate_price_delta_QPushButton.setEnabled(False)


def compare_past_dates_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    start_date = ui.start_date_dateEdit.date()
    stop_date = ui.stop_date_dateEdit.date()
    ui.console_QTextEdit.setText(functions.compare_past_dates(start_date, stop_date))


def calculate_price_delta_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    start_date = ui.start_date_dateEdit.date()
    stop_date = ui.stop_date_dateEdit.date()
    ui.console_QTextEdit.setText(functions.calculate_price_delta(start_date, stop_date))


def monthly_max_delta_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText(functions.monthly_max_delta())


def max_delta_button_event():
    ui.clear_data_QPushButton.setEnabled(True)
    ui.console_QTextEdit.setText(functions.max_delta(None))


def set_today_button_event():
    ui.start_date_dateEdit.setDate(functions.get_date_today_plus_num_days(0))


def set_tomorrow_button_event():
    ui.stop_date_dateEdit.setDate(functions.get_date_today_plus_num_days(1))


ui.symbol_QLineEdit.textChanged.connect(clear_button_event)
ui.get_data_QPushButton.clicked.connect(get_data_button_event)
ui.clear_data_QPushButton.clicked.connect(clear_button_event)
ui.compare_past_dates_QPushButton.clicked.connect(compare_past_dates_button_event)
ui.monthly_maximum_delta_QPushButton.clicked.connect(monthly_max_delta_button_event)
ui.max_delta_QPushButton.clicked.connect(max_delta_button_event)
ui.set_today_QPushButton.clicked.connect(set_today_button_event)
ui.set_tomorrow_QPushButton.clicked.connect(set_tomorrow_button_event)
ui.calculate_price_delta_QPushButton.clicked.connect(calculate_price_delta_button_event)

main_window_Qdialog.show()
sys.exit(app.exec_())

