# Form implementation generated from reading ui file 'Tasarım/reset_password.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_reset_password(object):
    def setupUi(self, MainWindow_reset_password):
        MainWindow_reset_password.setObjectName("MainWindow_reset_password")
        MainWindow_reset_password.resize(512, 479)
        MainWindow_reset_password.setMinimumSize(QtCore.QSize(512, 479))
        MainWindow_reset_password.setMaximumSize(QtCore.QSize(512, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_reset_password)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"  background: #2d2d2d;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -40, 512, 512))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Tasarım\\../Resimler/refresh.png"))
        self.label.setObjectName("label")
        self.back_frost_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_frost_reset.setGeometry(QtCore.QRect(0, 10, 62, 58))
        self.back_frost_reset.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/points_beyaz.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_frost_reset.setIcon(icon)
        self.back_frost_reset.setIconSize(QtCore.QSize(50, 50))
        self.back_frost_reset.setFlat(True)
        self.back_frost_reset.setObjectName("back_frost_reset")
        self.eye_password_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eye_password_reset.setGeometry(QtCore.QRect(320, 163, 30, 30))
        self.eye_password_reset.setMinimumSize(QtCore.QSize(30, 30))
        self.eye_password_reset.setMaximumSize(QtCore.QSize(30, 30))
        self.eye_password_reset.setMouseTracking(True)
        self.eye_password_reset.setStyleSheet("QPushButton:pressed { background-color: transparent; }\n"
"")
        self.eye_password_reset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.eye_password_reset.setIcon(icon1)
        self.eye_password_reset.setIconSize(QtCore.QSize(30, 30))
        self.eye_password_reset.setShortcut("")
        self.eye_password_reset.setFlat(True)
        self.eye_password_reset.setObjectName("eye_password_reset")
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(110, 100, 245, 43))
        self.username.setMinimumSize(QtCore.QSize(245, 43))
        self.username.setMaximumSize(QtCore.QSize(245, 43))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.username.setFont(font)
        self.username.setStyleSheet("#username {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font: 18px \"Times New Roman\";\n"
"}\n"
"\n"
"#username:focus {\n"
"border: 2px solid #fff;\n"
"  outline: none;\n"
"}\n"
"\n"
"\n"
"")
        self.username.setInputMask("")
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.password_again = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_again.setGeometry(QtCore.QRect(110, 210, 245, 43))
        self.password_again.setMinimumSize(QtCore.QSize(245, 43))
        self.password_again.setMaximumSize(QtCore.QSize(245, 43))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password_again.setFont(font)
        self.password_again.setStyleSheet("#password_again {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font: 18px \"Times New Roman\";\n"
"}\n"
"\n"
"#password_again:focus {\n"
"border: 2px solid #fff;\n"
"  outline: none;\n"
"}\n"
"\n"
"\n"
"")
        self.password_again.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.password_again.setClearButtonEnabled(False)
        self.password_again.setObjectName("password_again")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 155, 245, 43))
        self.password.setMinimumSize(QtCore.QSize(245, 43))
        self.password.setMaximumSize(QtCore.QSize(245, 43))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setStyleSheet("#password {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 5px 10px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font: 18px \"Times New Roman\";\n"
"}\n"
"\n"
"#password:focus {\n"
"border: 2px solid #fff;\n"
"  outline: none;\n"
"}\n"
"\n"
"\n"
"")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.generate_password_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_password_reset.setGeometry(QtCore.QRect(370, 210, 105, 51))
        self.generate_password_reset.setMinimumSize(QtCore.QSize(105, 51))
        self.generate_password_reset.setMaximumSize(QtCore.QSize(105, 51))
        self.generate_password_reset.setStyleSheet("QPushButton {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 10px 20px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font: 16px \"Times New Roman\";\n"
"\n"
"  letter-spacing: 1px;\n"
"  transition: background-color 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #333;\n"
"}\n"
"")
        self.generate_password_reset.setObjectName("generate_password_reset")
        self.reset_password = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reset_password.setGeometry(QtCore.QRect(175, 265, 180, 45))
        self.reset_password.setMinimumSize(QtCore.QSize(180, 45))
        self.reset_password.setMaximumSize(QtCore.QSize(180, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reset_password.setFont(font)
        self.reset_password.setStyleSheet("QPushButton {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 10px 20px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font: 16px \"Times New Roman\";\n"
"\n"
"  letter-spacing: 1px;\n"
"  transition: background-color 0.2s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #333;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/lock_beyaz_.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reset_password.setIcon(icon2)
        self.reset_password.setIconSize(QtCore.QSize(30, 30))
        self.reset_password.setFlat(False)
        self.reset_password.setObjectName("reset_password")
        self.label.raise_()
        self.back_frost_reset.raise_()
        self.username.raise_()
        self.password_again.raise_()
        self.password.raise_()
        self.generate_password_reset.raise_()
        self.reset_password.raise_()
        self.eye_password_reset.raise_()
        MainWindow_reset_password.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_reset_password)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_reset_password.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_reset_password)
        self.statusbar.setObjectName("statusbar")
        MainWindow_reset_password.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_reset_password)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_reset_password)
        MainWindow_reset_password.setTabOrder(self.username, self.password)
        MainWindow_reset_password.setTabOrder(self.password, self.password_again)
        MainWindow_reset_password.setTabOrder(self.password_again, self.reset_password)
        MainWindow_reset_password.setTabOrder(self.reset_password, self.generate_password_reset)
        MainWindow_reset_password.setTabOrder(self.generate_password_reset, self.eye_password_reset)
        MainWindow_reset_password.setTabOrder(self.eye_password_reset, self.back_frost_reset)

    def retranslateUi(self, MainWindow_reset_password):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_reset_password.setWindowTitle(_translate("MainWindow_reset_password", "MainWindow"))
        self.username.setPlaceholderText(_translate("MainWindow_reset_password", "Username"))
        self.password_again.setPlaceholderText(_translate("MainWindow_reset_password", "Password Repeat"))
        self.password.setPlaceholderText(_translate("MainWindow_reset_password", "Password"))
        self.generate_password_reset.setText(_translate("MainWindow_reset_password", "Generate\n"
"Password"))
        self.reset_password.setText(_translate("MainWindow_reset_password", "Reset Password"))
