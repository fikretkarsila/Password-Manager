import sys
import time
from random import choice
from threading import Thread
from random import randint

import mysql.connector #Veritabanı bağlantı

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QLineEdit,QTableWidgetItem
from PyQt6.QtCore import Qt,QUrl
from PyQt6.QtGui import QDesktopServices,QIcon

from login_panel import Ui_MainWindow_login
from reset_password import Ui_MainWindow_reset_password
from main import Ui_MainWindow_main
from about import Ui_MainWindow_about


def mesaj_kutusu(Title, Contents, Signal, Picture_Path):  # Mesaj Bildirim Kutusu
    message = QMessageBox()
    message.setWindowIcon(QIcon(Picture_Path))
    message.setWindowTitle(Title)
    message.setText(Contents)
    message.setIcon(Signal)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    message.setDefaultButton(QMessageBox.StandardButton.Cancel)

    button_ok = message.button(QMessageBox.StandardButton.Yes)
    button_ok.setText("Ok")

    message.exec()

try:

    class Password_Manager(QMainWindow):
        def __init__(self):
            super().__init__()

            self.login = Ui_MainWindow_login()
            self.login.setupUi(self)

            self.setWindowTitle("LogIn")
            self.setWindowIcon(QIcon("Resimler/login_siyah.png"))


            self.login.login.clicked.connect(self.login_entrance)
            self.login.reset_password.clicked.connect(self.login_reset)

            self.login_connectDb()

        def login_reset(self,window = 'login',username_K = ''):

            self.login.username.clear()
            self.login.password.clear()

            def generate_password():

                def uret():

                    passwords,sifre,character,random_key = [],'',"abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&",randint(10,16)

                    for x in range(10):

                        for y in range(random_key):
                            sifre += choice(character)

                        passwords.append(sifre)
                        sifre = ''

                    for x in range(10):

                        sifre = choice(passwords)

                        login_main.password.setText(sifre)
                        login_main.password_again.setText(sifre)

                        time.sleep(0.01)

                threading_1 = Thread(target=uret)
                threading_1.start()

            def back_frost():
                try:

                    for widget in self.findChildren(QLineEdit):
                        widget.clear()

                    self.login_window.close()

                    if window == 'login':
                        self.show()
                    else:
                        self.main_window.show()

                except Exception as ex:
                    print(ex)

            def forgot_password():
                try:

                    username_app = login_main.username.text().strip()
                    password_app = login_main.password.text().strip()
                    password_repeat_app = login_main.password_again.text().strip()
                    # Texlerini aldık.

                    if len(username_app) == 0 or len(password_app) == 0 or len(password_repeat_app) == 0:
                        raise SyntaxError(mesaj_kutusu("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT id,username FROM users") # Sorgu ile id ve kullanıcı adını çekildi.
                    users = self.cursor.fetchall() # users olan kullanıcıları gönderildi.

                    Id,control_user = False,'' # Kontrol değişkenleri oluşturuldu.
                    for Id,username in users:
                        if username == username_app:
                            control_user = True
                            break
                    else:
                        raise SyntaxError(mesaj_kutusu("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                       "Resimler/information-button_beyaz.png"))

                    if control_user:
                        if password_app == password_repeat_app:
                            self.cursor.execute(f"UPDATE users SET password = '{password_app}' WHERE id = %s",(Id,))
                            self.connect.commit()

                            mesaj_kutusu("Info","Password change successful.",QMessageBox.Icon.Information,"Resimler/notification_beyaz.png")

                            self.login_window.close()

                            if window == 'login':
                                self.show()
                            else:
                                self.main_window.show()
                        else:
                            mesaj_kutusu("Info", "Passwords do not match.", QMessageBox.Icon.Warning,
                                         "Resimler/notification_beyaz.png")

                except Exception as ex:
                    print(ex)

            def gorunur():

                if self.change:
                    login_main.password.setEchoMode(QLineEdit.EchoMode.Normal)
                    login_main.password_again.setEchoMode(QLineEdit.EchoMode.Normal)
                    login_main.eye_password.setIcon(QIcon("Resimler/hide.png"))
                    self.change = False
                else:
                    login_main.password.setEchoMode(QLineEdit.EchoMode.Password)
                    login_main.password_again.setEchoMode(QLineEdit.EchoMode.Password)
                    login_main.eye_password.setIcon(QIcon("Resimler/view.png"))
                    self.change = True

            self.close()

            self.login_window = QMainWindow()

            login_main = Ui_MainWindow_reset_password()
            login_main.setupUi(self.login_window)

            self.change = True

            login_main.back_frost.clicked.connect(back_frost)
            login_main.reset_password.clicked.connect(forgot_password)
            login_main.generate_password.clicked.connect(generate_password)
            login_main.eye_password.clicked.connect(gorunur)

            self.login_window.setWindowTitle("Reset Password")
            self.login_window.setWindowIcon(QIcon("Resimler/refresh_siyah.png"))

            if not window:
                window = 'login'

            if len(username_K) != 0:
                login_main.username.setText(username_K)
                login_main.username.setEnabled(False)

            self.login_window.show()
        def login_connectDb(self):

            self.connect = mysql.connector.connect(
                host='localhost',
                user='root',
                password='n3D2uMF3',
                database='password_managerdb'
            )

            self.cursor = self.connect.cursor()
        def login_entrance(self):

            try:

                username = self.login.username.text().strip()
                password = self.login.password.text().strip()

                if len(username) == 0 or len(password) == 0:
                    raise SyntaxError(mesaj_kutusu("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                self.cursor.execute("SELECT username,password FROM users")
                users = self.cursor.fetchall()

                control,control_2 = False,False
                for x,y in users:
                    if x == username:
                        control = True
                        if y == password:
                            control_2 = True
                            break
                else:

                    if not control:
                        raise SyntaxError(mesaj_kutusu("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                       "Resimler/information-button_beyaz.png"))

                    mesaj_kutusu("Info","Username and/or password are incorrect.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png")

                if control_2:

                    self.login.username.clear()
                    self.login.password.clear()

                    return self.main(username)



            except Exception as ex:
                print(ex)
        def main(self,username_K):

            def all_show():

                main.girdiler.clearContents() # Tabloları temizledim.

                time.sleep(0.2)

                self.cursor.execute("SELECT * FROM users")
                infos,rowIndex = self.cursor.fetchall(),0 # Bilgilerimizi değişkene attık.

                main.girdiler.setRowCount(0)

                for write in infos:
                    rowCount = main.girdiler.rowCount()

                    main.girdiler.insertRow(rowCount)

                    main.girdiler.setItem(rowIndex,0,QTableWidgetItem(str(write[0])))
                    main.girdiler.setItem(rowIndex,1, QTableWidgetItem(str(write[1])))
                    main.girdiler.setItem(rowIndex, 2, QTableWidgetItem(str(write[2])))

                    rowIndex += 1

            def user_settings():

                self.main_window.close()

                self.login_reset('main',username_K)

            def login_go():

                for widget in self.findChildren(QLineEdit):
                    widget.clear()

                main.database_control.setStyleSheet("""
                                                        border-radius: 25px;
                                                        background-color: red;
                                                        color: white;
                                                        width: 50px;
                                                        height: 50px; """)

                main.label_control.setText("Database Not Connected")

                self.main_window.close()

                self.show()

            def about_func():

                def git(): # Web Site Linklerine gitmesini sağladığım fonksiyon

                    sender,links,url = about.centralwidget.sender().objectName(),['www.linkedin.com/in/fikretkarsila/','www.bionluk.com/fikretkarsila',
                            'www.twitch.tv/fikretkarsila','www.github.com/fikretkarsila',
                             'www.instagram.com/fikretkarsila/'],''

                    for link in links:
                        if sender in link:
                            url = link
                            break

                    QDesktopServices.openUrl(QUrl(url))s


                self.about_window = QMainWindow()
                about = Ui_MainWindow_about()
                about.setupUi(self.about_window)

                about.github.clicked.connect(git)
                about.linkedin.clicked.connect(git)
                about.bionluk.clicked.connect(git)
                about.twitch.clicked.connect(git)
                about.instagram.clicked.connect(git)

                self.about_window.setWindowTitle("About")

                self.about_window.show()

            def connection():

                try:
                    time.sleep(1.5)

                    self.connect = mysql.connector.connect(
                        host = 'localhost',
                        user = 'root',
                        password = 'n3D2uMF3',
                        database = 'password_managerdb'
                    )

                    self.cursor = self.connect.cursor()

                    main.database_control.setStyleSheet("""
                            border-radius: 25px;
                            background-color: green;
                            color: white;
                            width: 50px;
                            height: 50px; """)

                    main.label_control.setText("Database Connected")

                except Exception as ex:
                    print(f"Hata : {ex}") #---------------------------------------------------------------------> Bakılacak yer.

                    main.database_control.setStyleSheet("""
                                        border-radius: 25px;
                                        background-color: red;
                                        color: white;
                                        width: 50px;
                                        height: 50px; """)

                    main.label_control.setText("Database Not Connected")

            def generate_password():

                sender = main.centralwidget.sender().objectName()

                def uret():

                    passwords,sifre,character,random_key = [],'',"abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&",randint(10,16)

                    for x in range(10):

                        for y in range(random_key):
                            sifre += choice(character)

                        passwords.append(sifre)
                        sifre = ''

                    for x in range(10):

                        sifre = choice(passwords)

                        if sender == 'generate_password_new':
                            main.password_new.setText(sifre)
                            main.password_repeat_new.setText(sifre)
                        else:
                            main.password_edit.setText(sifre)
                            main.password_repeat_edit.setText(sifre)

                        time.sleep(0.01)

                threading_1 = Thread(target=uret)
                threading_1.start()

            self.close() # Login penceresini kapattım.
            self.connect.close() # Login database kapattım.

            self.main_window = QMainWindow()

            main = Ui_MainWindow_main()
            main.setupUi(self.main_window)

            self.main_window.setWindowTitle("Password Manager")
            self.main_window.setWindowIcon(QIcon("Resimler/key_siyah.png"))

            main.about.clicked.connect(about_func)

            main.generate_password_new.clicked.connect(generate_password)
            main.generate_password_edit.clicked.connect(generate_password)
            main.user_settings.clicked.connect(user_settings)
            main.change_user.clicked.connect(login_go)
            main.all_show.clicked.connect(all_show)

            connect_thread = Thread(target=connection)
            connect_thread.start()

            self.main_window.show()


    application = QApplication(sys.argv)
    window = Password_Manager()
    window.show()
    sys.exit(application.exec())

except Exception as ex:
    print(ex)
