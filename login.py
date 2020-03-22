import sqlite3
from mainApp import Mainapp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Login(QMainWindow, object):
    db = sqlite3.connect('ohms.db')
    cur = db.cursor()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 239)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/authentication.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("color: rgb(0, 0, 127);")
        self.login_pushButton = QtWidgets.QPushButton(Form)
        self.login_pushButton.setGeometry(QtCore.QRect(210, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 140, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.database()
        self.login_pushButton.clicked.connect(self.Handel_Login)

    def database(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
            idusers       INTEGER      PRIMARY KEY AUTOINCREMENT
            NOT NULL,
            user_name     VARCHAR(45) UNIQUE,
            user_email    VARCHAR(60),
            user_password VARCHAR(45)
            )"""
        self.cur.execute(sql)

        username = 'mujiboladeji'
        email = 'oladejimujib.com'
        password = '12345'
         
        self.cur.execute(''' REPLACE INTO users  (user_name, user_email, user_password) VALUES (?,?,?)''',
                            (username, email, password))
        self.db.commit()


    def Handel_Login(self):
       username = self.lineEdit.text()
       password = self.lineEdit_2.text()

       self.cur.execute('''SELECT * FROM users ''')
       data = self.cur.fetchall()
       for row in data:

           if username == row[1] and password == row[3]:
               #print('user match')
               self.app = QtWidgets.QMainWindow()
               self.ui = Mainapp()
               Form.close()
               self.ui.setupUi(self.app)
               self.app.show()
           else:
               self.label.setText('Please Enter Correct Username and Password')
               


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.login_pushButton.setText(_translate("Form", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

