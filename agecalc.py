from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from datetime import date
import sys


class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dob = QDateEdit()
        self.label = QLabel(" <b>Select Your Date Of Birth :</b> ")
        self.dob.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dob.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dob.setCalendarPopup(True)
        self.layout = QFormLayout()
        self.layout.addRow(self.label)
        self.answer = QLabel()
        self.answer.setStyleSheet("color:#DCE2F0")
        self.label.setStyleSheet("color:#DCE2F0")
        self.dob.setStyleSheet("background-color:#DCE2F0")
        self.answer.setText("")
        self.layout.addRow(self.dob)
        self.layout.addRow(self.answer)
        self.setLayout(self.layout)
        self.dob.dateChanged.connect(self.onDateChanged)

    def onDateChanged(self, qDate):
        text = '<b>You are {0} years old. </b>' .format(date.today().year - qDate.year(
        ) - ((date.today().month, date.today().day) < (qDate.month(), qDate.day())))
        self.answer.setText(text)


    

app = QApplication([])
app.setApplicationName('Age Calculator')
app.setWindowIcon(QtGui.QIcon('logo.png'))
main = MyMainWindow()
main.setWindowTitle("Age Calculator")
main.setGeometry(600, 300, 400, 200)
main.setStyleSheet("background-color:#50586C")
main.show()
sys.exit(app.exec())
