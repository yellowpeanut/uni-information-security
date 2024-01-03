
from PyQt6 import QtCore, QtGui, QtWidgets
import pickle
import os
from user import User
from server import Server

class LoginWindow():

    def __init__(self, server):
        super().__init__()
        self.wnd = QtWidgets.QMainWindow()
        self.server = server
        self.setupUi(self.wnd)

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("Rakocrab Software")
        LoginWindow.resize(600, 275)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbUsername = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbUsername.setGeometry(QtCore.QRect(25, 25, 250, 16))
        self.lbUsername.setObjectName("lbUsername")

        self.leUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.leUsername.setGeometry(QtCore.QRect(25, 51, 250, 16))
        self.leUsername.setObjectName("leUsername")

        self.lbPubKey = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbPubKey.setGeometry(QtCore.QRect(25, 75, 250, 16))
        self.lbPubKey.setObjectName("lbPubKey")

        self.lePubKey = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lePubKey.setGeometry(QtCore.QRect(25, 101, 250, 16))
        self.lePubKey.setObjectName("lePubKey")

        self.lbPrivKey = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbPrivKey.setGeometry(QtCore.QRect(25, 125, 250, 16))
        self.lbPrivKey.setObjectName("lbPrivKey")

        self.lePrivKey = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lePrivKey.setGeometry(QtCore.QRect(25, 151, 250, 16))
        self.lePrivKey.setObjectName("lePrivKey")

        self.teInfo= QtWidgets.QTextEdit(parent=self.centralwidget)
        self.teInfo.setGeometry(QtCore.QRect(285, 15, 305, 227))
        self.teInfo.setObjectName("teInfo")
        self.teInfo.setReadOnly(True)

        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(25, 200, 250, 41))
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.login)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")

        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Rakocrab Software"))
        LoginWindow.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__) + "/rakocrab.png"))
        self.btnLogin.setText(_translate("LoginWindow", "Войти"))
        self.lbUsername.setText(_translate("MainWindow", "Имя пользователя"))
        self.lbPubKey.setText(_translate("MainWindow", "Публичный ключ"))
        self.lbPrivKey.setText(_translate("MainWindow", "Приватный ключ"))


    def login(self):
        username = self.leUsername.text().strip()
        pub_key = self.lePubKey.text().strip()
        priv_key = self.lePrivKey.text().strip()
        try:
            with open(os.path.dirname(__file__) + "/pkl" + f'/{username}.pkl', 'rb') as file:
                target_user = pickle.load(file)
            with open(os.path.dirname(__file__) + "/pkl" + f'/{pub_key}{priv_key}.pkl', 'rb') as file:
                found_user = pickle.load(file)
            
            r = found_user.start_authentication()
            target_user.k = found_user.k
            if self.server.authenticate(target_user, r):
                self.teInfo.setText("Аутентификация прошла успешно.")
            else:
                self.teInfo.setText("Ошибка аутентификации: введенные данные не верны.")
            return
        except FileNotFoundError:
            self.teInfo.setText("Ошибка аутентификации: введенные данные не верны.")
            return
