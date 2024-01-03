# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGridLayout, QTableWidget, QTableWidgetItem
from qt_material import apply_stylesheet
import codecs
import random
import os
import pickle
from user import User
from server import Server
from register_wnd import RegisterWindow
from login_wnd import LoginWindow


class Ui_MainWindow(object):

    server = Server()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Rakocrab Software")
        MainWindow.resize(300, 150)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(25, 25, 251, 41))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.show_login)

        self.btnRegister = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(25, 75, 251, 41))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.show_register)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        import os
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rakocrab Software"))
        MainWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/rakocrab.png"))
        self.btnLogin.setText(_translate("MainWindow", "Вход"))
        self.btnRegister.setText(_translate("MainWindow", "Регистрация"))

    def show_login(self):
        self.log_wnd = LoginWindow(self.server)
        self.log_wnd.wnd.show()
    
    def show_register(self):
        self.reg_wnd = RegisterWindow(self.server)
        self.reg_wnd.wnd.show()

    def exit(self):
        MainWindow.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())