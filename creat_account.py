# Form implementation generated from reading ui file 'Tasarım/creat_account.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_create(object):
    def setupUi(self, MainWindow_create):
        MainWindow_create.setObjectName("MainWindow_create")
        MainWindow_create.resize(459, 471)
        MainWindow_create.setMinimumSize(QtCore.QSize(459, 471))
        MainWindow_create.setMaximumSize(QtCore.QSize(459, 471))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_create)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"  background: #2d2d2d;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.password_again = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_again.setGeometry(QtCore.QRect(90, 260, 245, 43))
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
        self.create_register = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_register.setGeometry(QtCore.QRect(200, 315, 130, 45))
        self.create_register.setMinimumSize(QtCore.QSize(130, 45))
        self.create_register.setMaximumSize(QtCore.QSize(130, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_register.setFont(font)
        self.create_register.setStyleSheet("QPushButton {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 10px 20px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"   font: 16px \"Times New Roman\";\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/register_beyaz.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.create_register.setIcon(icon)
        self.create_register.setIconSize(QtCore.QSize(30, 30))
        self.create_register.setFlat(False)
        self.create_register.setObjectName("create_register")
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(90, 150, 245, 43))
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
        self.generate_password_create = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_password_create.setGeometry(QtCore.QRect(340, 260, 105, 51))
        self.generate_password_create.setMinimumSize(QtCore.QSize(105, 51))
        self.generate_password_create.setMaximumSize(QtCore.QSize(105, 51))
        self.generate_password_create.setStyleSheet("QPushButton {\n"
"  background-color: #4A4A4A;\n"
"  color: #fff;\n"
"  padding: 10px 20px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"   font: 16px \"Times New Roman\";\n"
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
        self.generate_password_create.setObjectName("generate_password_create")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 205, 245, 43))
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
        self.eye_password_account = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eye_password_account.setGeometry(QtCore.QRect(290, 210, 30, 30))
        self.eye_password_account.setMinimumSize(QtCore.QSize(30, 30))
        self.eye_password_account.setMaximumSize(QtCore.QSize(30, 30))
        self.eye_password_account.setMouseTracking(True)
        self.eye_password_account.setStyleSheet("QPushButton:pressed { background-color: transparent; }\n"
"")
        self.eye_password_account.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.eye_password_account.setIcon(icon1)
        self.eye_password_account.setIconSize(QtCore.QSize(30, 30))
        self.eye_password_account.setShortcut("")
        self.eye_password_account.setFlat(True)
        self.eye_password_account.setObjectName("eye_password_account")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 561, 621))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Tasarım\\../Resimler/user_beyaz.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-430, 30, 721, 631))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Tasarım\\../Resimler/smoke_beyaz.png"))
        self.label_3.setObjectName("label_3")
        self.back_frost_create = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_frost_create.setGeometry(QtCore.QRect(10, 20, 62, 58))
        self.back_frost_create.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Tasarım\\../Resimler/points_beyaz.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_frost_create.setIcon(icon2)
        self.back_frost_create.setIconSize(QtCore.QSize(50, 50))
        self.back_frost_create.setFlat(True)
        self.back_frost_create.setObjectName("back_frost_create")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setStyleSheet("font: 75 36pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.layoutWidget.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.password_again.raise_()
        self.create_register.raise_()
        self.username.raise_()
        self.generate_password_create.raise_()
        self.password.raise_()
        self.eye_password_account.raise_()
        self.back_frost_create.raise_()
        MainWindow_create.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_create)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_create.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_create)
        self.statusbar.setObjectName("statusbar")
        MainWindow_create.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_create)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_create)
        MainWindow_create.setTabOrder(self.username, self.password)
        MainWindow_create.setTabOrder(self.password, self.password_again)
        MainWindow_create.setTabOrder(self.password_again, self.generate_password_create)
        MainWindow_create.setTabOrder(self.generate_password_create, self.create_register)
        MainWindow_create.setTabOrder(self.create_register, self.eye_password_account)
        MainWindow_create.setTabOrder(self.eye_password_account, self.back_frost_create)

    def retranslateUi(self, MainWindow_create):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_create.setWindowTitle(_translate("MainWindow_create", "MainWindow"))
        self.password_again.setPlaceholderText(_translate("MainWindow_create", "Password Repeat"))
        self.create_register.setText(_translate("MainWindow_create", "Register"))
        self.username.setPlaceholderText(_translate("MainWindow_create", "Username"))
        self.generate_password_create.setText(_translate("MainWindow_create", "Generate\n"
"Password"))
        self.password.setPlaceholderText(_translate("MainWindow_create", "Password"))
        self.label.setText(_translate("MainWindow_create", "Create Account"))
