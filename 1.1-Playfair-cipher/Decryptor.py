# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGridLayout, QTableWidget, QTableWidgetItem
from qt_material import apply_stylesheet
import codecs
import random


class Ui_MainWindow(object):
    KEYWORD = "краб"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lbInitial = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbInitial.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.lbInitial.setObjectName("lbInitial")

        self.teInitial = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.teInitial.setGeometry(QtCore.QRect(10, 30, 501, 251))
        self.teInitial.setObjectName("teInitial")
        self.teInitial.setReadOnly(True)

        self.lbEncrypted = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbEncrypted.setGeometry(QtCore.QRect(10, 290, 161, 16))
        self.lbEncrypted.setObjectName("lbEncrypted")

        self.teEncrypted = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.teEncrypted.setGeometry(QtCore.QRect(10, 310, 501, 251))
        self.teEncrypted.setObjectName("teEncrypted")
        self.teEncrypted.setReadOnly(True)

        # self.imgTab = QtGui.QPixmap("table.png")

        self.imgTable = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.imgTable.setGeometry(QtCore.QRect(530, 30, 251, 251))
        self.imgTable.setObjectName("imgTable")

        self.lbTable = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbTable.setGeometry(QtCore.QRect(530, 10, 101, 16))
        self.lbTable.setObjectName("lbTable")
        # self.lbTable.setPixmap(self.imgTab)

        self.btnOpen = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(530, 450, 251, 41))
        self.btnOpen.setObjectName("btnOpen")
        self.btnOpen.clicked.connect(self.openFile)

        self.btnEncrypt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(530, 520, 141, 41))
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnEncrypt.clicked.connect(self.decrypt)

        self.btnExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(680, 520, 101, 41))
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(self.exit)

        self.lbKeyword = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbKeyword.setGeometry(QtCore.QRect(530, 310, 101, 16))
        self.lbKeyword.setObjectName("lbKeyword")

        self.leKeyword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.leKeyword.setGeometry(QtCore.QRect(530, 330, 251, 21))
        self.leKeyword.setObjectName("leKeyword")
        self.leKeyword.setText(self.KEYWORD)

        self.table = QTableWidget(parent=self.centralwidget)  # Create a table
        self.table.setGeometry(QtCore.QRect(530, 30, 681, 251))
        self.table.setColumnCount(6)  # Set three columns
        self.table.setRowCount(6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbInitial.setText(_translate("MainWindow", "Текст файла"))
        self.lbEncrypted.setText(_translate("MainWindow", "Расшифрованный текст"))
        self.lbTable.setText(_translate("MainWindow", "Таблица замен"))
        self.btnOpen.setText(_translate("MainWindow", "Открыть файл"))
        self.btnEncrypt.setText(_translate("MainWindow", "Расшифровать"))
        self.btnExit.setText(_translate("MainWindow", "Выход"))
        self.lbKeyword.setText(_translate("MainWindow", "Ключевое слово"))

    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "", "All Files(*);;Text Files(*.txt)")
        if filename:
            with codecs.open(filename, 'r', "utf-8") as file:
                text = file.read()
                file.close()
                self.teInitial.setText(text)

    def decrypt(self):
        def createTable():
            alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя "
            horizontal = [["й", "ц"], ["у", "к"], ["е", "н"], ["г", "ш"], ["щ", "з"], ["х", "ъ"]]
            vertical = [["ф", "ы"], ["в", "а"], ["п", "р"], ["о", "л"], ["д", "ж"], ["э", "я"]]
            keyword = self.leKeyword.text()

            newAlphabet = keyword + alphabet.translate({ord(i): None for i in keyword})
            values = []
            hashTable = {}

            for i in range(len(horizontal)):
                for j in range(len(vertical)):
                    value = combine(horizontal[i], vertical[j])
                    values.append(value.copy())

            for i in range(len(newAlphabet)):
                hashTable[newAlphabet[i]] = values[i]

                # print(hashTable)
            for i in range(0, len(horizontal)):
                self.table.setHorizontalHeaderItem(i, QTableWidgetItem(''.join(horizontal[i])))
            for i in range(0, len(vertical)):
                self.table.setVerticalHeaderItem(i, QTableWidgetItem(''.join(vertical[i])))

            print(list(hashTable.keys())[0*len(horizontal) + 0])
            index = 0
            for i in range(0, len(horizontal)):
                for j in range(0, len(vertical)):
                    if index >= len(hashTable.keys()):
                        break
                    self.table.setItem(i, j, QTableWidgetItem(list(hashTable.keys())[index]))
                    index+=1

            return hashTable

        def combine(array1, array2):
            res = []
            for k in range(len(array1)):
                for l in range(len(array2)):
                    res.append(array1[k] + array2[l])
                    res.append(array2[l] + array1[k])
            return res

        table = createTable()
        text = self.teInitial.toPlainText().strip().lower()
        decryptedText = ""

        textLength = len(text)
        currentIndex = 0
        while (currentIndex < textLength):
            symb = text[currentIndex] + text[currentIndex + 1]
            for i in table:
                if symb in table.get(i):
                    decryptedText += i
                    break
            currentIndex += 2

        with codecs.open("decrypted.txt", 'w', "utf-8") as file:
            file.write(decryptedText)
            file.close()
            self.teEncrypted.setText(decryptedText)

    def exit():
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
