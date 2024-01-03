
from PyQt6 import QtCore, QtGui, QtWidgets
import os
from user import User
from server import Server

class RegisterWindow():

    def __init__(self, server):
        super().__init__()
        self.wnd = QtWidgets.QMainWindow()
        self.server = server
        self.setupUi(self.wnd)

    def setupUi(self, RegWindow):
        RegWindow.setObjectName("Rakocrab Software")
        RegWindow.resize(600, 150)
        self.centralwidget = QtWidgets.QWidget(parent=RegWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbUsername = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbUsername.setGeometry(QtCore.QRect(25, 25, 250, 16))
        self.lbUsername.setObjectName("lbUsername")

        self.leUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.leUsername.setGeometry(QtCore.QRect(25, 51, 250, 16))
        self.leUsername.setObjectName("leUsername")

        self.teInfo= QtWidgets.QTextEdit(parent=self.centralwidget)
        self.teInfo.setGeometry(QtCore.QRect(285, 15, 305, 102))
        self.teInfo.setObjectName("teInfo")
        self.teInfo.setReadOnly(True)

        self.btnRegister = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(25, 75, 250, 41))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.register)

        RegWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=RegWindow)
        self.statusbar.setObjectName("statusbar")

        RegWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "Rakocrab Software"))
        RegWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/rakocrab.png"))
        self.btnRegister.setText(_translate("RegWindow", "Зарегистрироваться"))
        self.lbUsername.setText(_translate("MainWindow", "Имя пользователя"))


    def register(self):
        username = self.leUsername.text().strip()
        try:
            f = open(os.path.dirname(__file__) + "/pkl" + f'/{username}.pkl', 'rb')
        except FileNotFoundError:
            user = User(username)
            self.teInfo.setText(f"Вы успешно зарегистрированы!\nВаш публичный ключ: {user.y}\nВаш приватный ключ: {user.x}")
            return
        self.teInfo.setText("Ошибка!\nПользователь с данным именем уже существует!")