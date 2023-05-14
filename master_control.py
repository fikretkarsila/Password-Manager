import sys
import time
from random import choice
from threading import Thread
from random import randint
import mysql.connector # Veritabanı bağlantı
from mysql.connector.locales.eng import client_error

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QLineEdit,QTableWidgetItem
from PyQt6.QtCore import Qt,QUrl
from PyQt6.QtGui import QDesktopServices,QIcon

from login_panel import Ui_MainWindow_login
from reset_password import Ui_MainWindow_reset_password
from main import Ui_MainWindow_main
from about import Ui_MainWindow_about
from creat_account import Ui_MainWindow_create

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
            self.login.eye_password_login.clicked.connect(self.view_hide)
            self.login.create_account.clicked.connect(self.create_account)

            self.login.login.setShortcut('Return')

            self.login_connectDb_password()
            self.change = True

        @staticmethod
        def condition_box(Title, Contents, Signal, Picture_Path):
            message = QMessageBox()
            message.setWindowTitle(Title)
            message.setText(Contents)
            message.setIcon(Signal)
            message.setWindowIcon(QIcon(Picture_Path))

            message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            message.setDefaultButton(QMessageBox.StandardButton.No)

            message_yes = message.button(QMessageBox.StandardButton.Yes)
            message_no = message.button(QMessageBox.StandardButton.No)

            message.exec()

            if message.clickedButton() == message_yes:
                return True
            else:
                return False
        @staticmethod
        def message_box(Title, Contents, Signal, Picture_Path):  # Mesaj Bildirim Kutusu
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


        def view_hide(self):  # Ortak kullanılan fonksiyon

            try:

                variable_name = self.sender().objectName()

                if variable_name == 'eye_password_login':

                    if self.change:
                        self.login.password.setEchoMode(QLineEdit.EchoMode.Normal)
                        self.login.eye_password_login.setIcon(QIcon("Resimler/hide.png"))
                        self.change = False
                    else:
                        self.login.password.setEchoMode(QLineEdit.EchoMode.Password)
                        self.login.eye_password_login.setIcon(QIcon("Resimler/view.png"))
                        self.change = True

                elif variable_name == 'eye_password_account':

                    if self.change:
                        self.create.password.setEchoMode(QLineEdit.EchoMode.Normal)
                        self.create.password_again.setEchoMode(QLineEdit.EchoMode.Normal)
                        self.create.eye_password_account.setIcon(QIcon("Resimler/hide.png"))
                        self.change = False
                    else:
                        self.create.password.setEchoMode(QLineEdit.EchoMode.Password)
                        self.create.password_again.setEchoMode(QLineEdit.EchoMode.Password)
                        self.create.eye_password_account.setIcon(QIcon("Resimler/view.png"))
                        self.change = True

                elif variable_name == 'eye_password_reset':

                    if self.change:
                        self.login_main.password.setEchoMode(QLineEdit.EchoMode.Normal)
                        self.login_main.password_again.setEchoMode(QLineEdit.EchoMode.Normal)
                        self.login_main.eye_password_reset.setIcon(QIcon("Resimler/hide.png"))
                        self.change = False
                    else:
                        self.login_main.password.setEchoMode(QLineEdit.EchoMode.Password)
                        self.login_main.password_again.setEchoMode(QLineEdit.EchoMode.Password)
                        self.login_main.eye_password_reset.setIcon(QIcon("Resimler/view.png"))
                        self.change = True



            except Exception as ex:
                print(f"Hata Mesajı : {ex}")
        def back_frost(self):   # Ortak kullanılan fonksiyon

            variable_name = self.sender().objectName()

            for widget in self.findChildren(QLineEdit):
                widget.clear()

            if variable_name == 'back_frost_create':

                self.main_create.close()
                self.show()

            elif variable_name == 'back_frost_reset':

                self.login_window.close()
                self.show()
        def generate_password(self):  # Ortak kullanılan fonksiyon

            variable_name = self.sender().objectName()
            def produce():

                passwords, sifre, character, random_key = [], '', "abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&", randint(10, 16)

                for x in range(10):

                    for y in range(random_key):
                        sifre += choice(character)

                    passwords.append(sifre)
                    sifre = ''

                for x in range(10):
                    sifre = choice(passwords)

                    if variable_name == 'generate_password_reset':

                        self.login_main.password.setText(sifre)
                        self.login_main.password_again.setText(sifre)

                    elif variable_name == 'generate_password_create':

                        self.create.password.setText(sifre)
                        self.create.password_again.setText(sifre)

                    elif variable_name == 'generate_password_new':
                        self.main.password_new.setText(sifre)
                        self.main.password_repeat_new.setText(sifre)
                    else:
                        self.main.password_edit.setText(sifre)
                        self.main.password_repeat_edit.setText(sifre)

                    time.sleep(0.01)

            threading_1 = Thread(target=produce)
            threading_1.start()

        def create_account(self):

            def save():

                try:

                    username = self.create.username.text().strip()
                    password = self.create.password.text().strip()
                    password_again = self.create.password_again.text().strip()

                    if len(username) == 0 or len(password) == 0 or len(password_again) == 0:
                        raise SyntaxError(self.message_box("Info", "Fill in all fields.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))
                    elif password != password_again:
                        raise SyntaxError(self.message_box("Info", "Passwords do not match.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT username FROM login_password")
                    users,control = self.cursor.fetchall(),False

                    for user in users:
                        if user[0] == username:
                            control = True
                            break

                    if control:
                        raise SyntaxError(self.message_box("Info", "There is already such a user.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))
                    else:

                        self.cursor.execute("INSERT INTO login_password(username,password) VALUES (%s,%s)",(username,password))
                        self.connect.commit()

                        for widget in self.findChildren(QLineEdit):
                            widget.clear()

                        self.message_box("Info", f"Your registration has been successfully created. Please make a note of your username and password.\n\nUsername :  {username}\nPassword : {password}", QMessageBox.Icon.Information,"Resimler/information-button_beyaz.png")

                        self.main_create.close()
                        self.show()

                except Exception as ex:
                    print(ex)

            self.close()

            self.main_create = QMainWindow()
            self.create = Ui_MainWindow_create()
            self.create.setupUi(self.main_create)

            self.create.back_frost_create.clicked.connect(self.back_frost)
            self.create.generate_password_create.clicked.connect(self.generate_password)
            self.create.eye_password_account.clicked.connect(self.view_hide)
            self.create.create_register.clicked.connect(save)

            self.create.create_register.setShortcut("Return")

            self.main_create.setWindowTitle('New Account')
            self.main_create.setWindowIcon(QIcon('Resimler/user_beyaz.png'))

            self.change = True
            self.create.password.setEchoMode(QLineEdit.EchoMode.Password)
            self.create.password_again.setEchoMode(QLineEdit.EchoMode.Password)
            self.create.eye_password_account.setIcon(QIcon("Resimler/view.png"))

            self.main_create.show()
        def login_reset(self,username_K = ''):

            try:

                self.login.username.clear()
                self.login.password.clear()

                def forgot_password():
                    try:

                        username_app = self.login_main.username.text().strip()
                        password_app = self.login_main.password.text().strip()
                        password_repeat_app = self.login_main.password_again.text().strip()
                        # Texlerini aldık.

                        if len(username_app) == 0 or len(password_app) == 0 or len(password_repeat_app) == 0:
                            raise SyntaxError(self.message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                        self.cursor.execute("SELECT id,username FROM login_password") # Sorgu ile id ve kullanıcı adını çekildi.
                        users = self.cursor.fetchall() # users olan kullanıcıları gönderildi.

                        Id,control_user = False,'' # Kontrol değişkenleri oluşturuldu.
                        for Id,username in users:
                            if username == username_app:
                                control_user = True
                                break
                        else:
                            raise SyntaxError(self.message_box("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                           "Resimler/information-button_beyaz.png"))

                        if control_user:

                            if password_app == password_repeat_app:
                                self.cursor.execute(f"UPDATE login_password SET password = '{password_app}' WHERE id = %s",(Id,))
                                self.connect.commit()

                                self.message_box("Info","Password change successful.",QMessageBox.Icon.Information,"Resimler/notification_beyaz.png")

                                self.login_window.close()
                                self.show()

                            else:
                                self.message_box("Info", "Passwords do not match.", QMessageBox.Icon.Warning,
                                             "Resimler/notification_beyaz.png")

                    except Exception as ex:
                        print(ex)

                self.close()

                self.login_window = QMainWindow()

                self.login_main = Ui_MainWindow_reset_password()
                self.login_main.setupUi(self.login_window)

                self.login_main.back_frost_reset.clicked.connect(self.back_frost)
                self.login_main.reset_password.clicked.connect(forgot_password)
                self.login_main.generate_password_reset.clicked.connect(self.generate_password)
                self.login_main.eye_password_reset.clicked.connect(self.view_hide)

                self.login_main.reset_password.setShortcut("Return")

                self.login_window.setWindowTitle("Reset Password")
                self.login_window.setWindowIcon(QIcon("Resimler/refresh_siyah.png"))

                self.change = True
                self.login_main.password.setEchoMode(QLineEdit.EchoMode.Password)
                self.login_main.password_again.setEchoMode(QLineEdit.EchoMode.Password)
                self.login_main.eye_password_reset.setIcon(QIcon("Resimler/view.png"))

                if username_K:

                    self.login_main.username.setText(username_K)
                    self.login_main.username.setEnabled(False)

                self.login_window.show()
            except Exception as ex:
                print(ex)
        def login_connectDb_password(self):

            try:

                self.connect = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='2023',
                    auth_plugin='mysql_native_password',
                    database='password_manager'
                )

                self.cursor = self.connect.cursor()

            except:

                self.connect = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='2023',
                    auth_plugin='mysql_native_password'
                )

                self.cursor = self.connect.cursor()

                self.cursor.execute("CREATE SCHEMA IF NOT EXISTS password_manager")

                self.connect.close()

                self.connect = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='2023',
                    auth_plugin='mysql_native_password',
                    database='password_manager'
                )

                self.cursor = self.connect.cursor()


            self.cursor.execute("""CREATE TABLE IF NOT EXISTS `login_password` (
                                  `id` int NOT NULL AUTO_INCREMENT,
                                  `username` varchar(200) NOT NULL,
                                  `password` varchar(200) NOT NULL,
                                  PRIMARY KEY (`id`),
                                  UNIQUE KEY `id_UNIQUE` (`id`),
                                  UNIQUE KEY `username_UNIQUE` (`username`)
                                ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
                                """)

            self.connect.commit()

        def login_entrance(self): # Yanlış yapıldı düzeltilecek

            try:

                username = self.login.username.text().strip()
                password = self.login.password.text().strip()

                if len(username) == 0 or len(password) == 0:
                    raise SyntaxError(self.message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                self.cursor.execute("SELECT username,password FROM login_password")
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
                        raise SyntaxError(self.message_box("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                       "Resimler/information-button_beyaz.png"))

                    self.message_box("Info","Username and/or password are incorrect.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png")

                if control_2:

                    self.login.username.clear()
                    self.login.password.clear()

                    self.main(username)

            except Exception as ex:
                print(ex)
        def main(self,username_K):

            def delete_db():

                try:
                    id = self.main.id_del.text().strip()

                    if len(id) == 0:
                        raise SyntaxError(self.message_box("Info", "Fill in all fields.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT id FROM user_data")
                    control_id, users_id = False, self.cursor.fetchall()

                    for user_id in users_id:
                        if str(user_id[0]) == id:
                            control_id = True
                            break

                    if not control_id:
                        raise SyntaxError(self.message_box("Info", "No record found with this id.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))


                    result = self.condition_box("Info","Are you sure you want to delete ?",QMessageBox.Icon.Critical,"Resimler/information-button_beyaz.png")

                    if result:
                        self.cursor.execute("DELETE FROM user_data WHERE id = %s",(id,))
                        self.connect.commit()

                        self.message_box('Info', 'The deletion was successful.', QMessageBox.Icon.Information,'Resimler/info-button_beyaz.png')

                        all_show()

                    self.main.id_del.clear()


                except Exception as ex:
                    print(ex)

            def edit_information(): # Bakılacak unutma !

                try:

                    id = self.main.id_edit.text().strip()
                    website = self.main.website_edit.text().strip()
                    username = self.main.username_edit.text().strip()
                    password = self.main.password_edit.text().strip()
                    password_repeat = self.main.password_repeat_edit.text().strip()

                    if len(id) == 0 or len(website) == 0 or len(username) == 0 or len(password) == 0 or len(password_repeat) == 0:
                        raise SyntaxError(self.message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT id FROM user_data")
                    control_id,users_id = False,self.cursor.fetchall()

                    for user_id in users_id:
                        if str(user_id[0]) == id:
                            control_id = True
                            break

                    if control_id:

                        self.cursor.execute("SELECT * FROM username_data")
                        users_control = self.cursor.fetchall()

                        for x,y in users_control:
                            if y == username:
                                ok = True
                                break
                        else:
                            ok = False

                        if ok:
                            self.cursor.execute("UPDATE user_data SET website_name = %s,username_id = %s,password = %s WHERE id = %s",(website,x,password,id))
                            self.connect.commit()

                            for widget in self.main.groupBox_2.findChildren(QLineEdit):
                                widget.clear()

                        else:

                            self.cursor.execute("INSERT INTO username_data(username) VALUES (%s)",(username,))
                            self.connect.commit()

                            self.cursor.execute("UPDATE user_data SET website_name = %s,username_id = %s,password = %s WHERE id = %s",(website, self.cursor.lastrowid, password,id))
                            self.connect.commit()

                            for widget in self.main.groupBox_2.findChildren(QLineEdit):
                                widget.clear()


                        self.message_box('Info', 'Registration successfully added.', QMessageBox.Icon.Information,
                                     'Resimler/info-button_beyaz.png')

                        all_show()
                    else:
                        raise SyntaxError(self.message_box("Info","No record found with this id.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))


                except Exception as ex:
                    print(ex)

            def username_search():

                try:

                    username = self.main.username_search.text().strip()

                    if len(username) == 0:
                        raise SyntaxError(self.message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute(f"""SELECT id,website_name,username_data.username,password FROM user_data 
                                        INNER JOIN username_data ON user_data.username_id = username_data.username_id
                                        WHERE username_data.username LIKE '%{username}%'
                                         """)

                    infos, rowIndex = self.cursor.fetchall(), 0  # Bilgilerimizi değişkene attık.

                    if len(infos) == 0:
                        raise SyntaxError(self.message_box("Info","No Records Found.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.main.girdiler.setRowCount(0)

                    for write in infos:
                        rowCount = self.main.girdiler.rowCount()

                        self.main.girdiler.insertRow(rowCount)

                        self.main.girdiler.setItem(rowIndex, 0, QTableWidgetItem(str(write[0])))
                        self.main.girdiler.setItem(rowIndex, 1, QTableWidgetItem(str(write[1])))
                        self.main.girdiler.setItem(rowIndex, 2, QTableWidgetItem(str(write[2])))
                        self.main.girdiler.setItem(rowIndex, 3, QTableWidgetItem(str(write[3])))

                        rowIndex += 1

                    for widget in self.main.groupBox_3.findChildren(QLineEdit):
                        widget.clear()

                except Exception as ex:
                    print(ex)

            def add_new():

                try:

                    website_name = self.main.website_new.text().strip()
                    username = self.main.username_new.text().strip()
                    password = self.main.password_new.text().strip()
                    password_repeat = self.main.password_repeat_new.text().strip()

                    if len(website_name) == 0 or len(username) == 0 or len(password) == 0 or len(password_repeat) == 0:
                        raise SyntaxError(self.message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT * FROM username_data")
                    users,user_control = self.cursor.fetchall(),False

                    for Id,user in users:
                        if user == username:
                            user_control = True
                            break

                    if user_control:
                        self.cursor.execute(f"INSERT INTO user_data (website_name,username_id,password) VALUES (%s,'{Id}',%s)",(website_name,password))
                        self.connect.commit()

                        self.message_box('Info','Registration successfully added.',QMessageBox.Icon.Information,'Resimler/info-button_beyaz.png')

                        for widget in self.main.groupBox.findChildren(QLineEdit):
                            widget.clear()
                    else:
                        self.cursor.execute("INSERT INTO username_data (username) VALUES (%s)",(username,))
                        self.connect.commit()

                        Id = self.cursor.lastrowid

                        self.cursor.execute(f"INSERT INTO user_data (website_name,username_id,password) VALUES (%s,'{Id}',%s)",(website_name,password))
                        self.connect.commit()

                        self.message_box('Info', 'Registration successfully added.', QMessageBox.Icon.Information,
                                     'Resimler/info-button_beyaz.png')

                        for widget in self.main.groupBox.findChildren(QLineEdit):
                            widget.clear()

                    all_show()
                except Exception as ex:
                    print(ex)

            def all_show():

                self.main.girdiler.clearContents() # Tabloları temizledim.

                time.sleep(0.2)

                self.cursor.execute("SELECT id,website_name,username_data.username,password FROM user_data inner join username_data ON user_data.username_id = username_data.username_id")
                infos,rowIndex = self.cursor.fetchall(),0 # Bilgilerimizi değişkene attık.

                self.main.girdiler.setRowCount(0)

                for write in infos:
                    rowCount = self.main.girdiler.rowCount()

                    self.main.girdiler.insertRow(rowCount)

                    self.main.girdiler.setItem(rowIndex,0,QTableWidgetItem(str(write[0])))
                    self.main.girdiler.setItem(rowIndex,1, QTableWidgetItem(str(write[1])))
                    self.main.girdiler.setItem(rowIndex, 2, QTableWidgetItem(str(write[2])))
                    self.main.girdiler.setItem(rowIndex,3,QTableWidgetItem(str(write[3])))

                    rowIndex += 1

            def user_settings():

                self.main_window.close()
                self.connect.close()

                del self.main  # Bellekte yer edindiği için 2 kere aynı şeyi çağırıyormuşuz gibi oluyor o yüzden çöküyordu silince sorun kalmadı.

                self.login_connectDb_password()
                self.login_reset(username_K)

            def change_user():

                for widget in self.findChildren(QLineEdit):
                    widget.clear()

                self.main.database_control.setStyleSheet("""
                                                        border-radius: 25px;
                                                        background-color: red;
                                                        color: white;
                                                        width: 50px;
                                                        height: 50px; 
                                                    """)

                self.main.label_control.setText("Database Not Connected")

                self.connect.close()
                self.main_window.close()

                del self.main     # Bellekte yer edindiği için 2 kere aynı şeyi çağırıyormuşuz gibi oluyor o yüzden çöküyordu silince sorun kalmadı.

                self.login_connectDb_password()
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

                    QDesktopServices.openUrl(QUrl(url))


                self.about_window = QMainWindow()
                about = Ui_MainWindow_about()
                about.setupUi(self.about_window)

                about.github.clicked.connect(git)
                about.linkedin.clicked.connect(git)
                about.bionluk.clicked.connect(git)
                about.twitch.clicked.connect(git)
                about.instagram.clicked.connect(git)

                self.about_window.setWindowTitle("About")
                self.about_window.setWindowIcon(QIcon("Resimler/information-button_beyaz.png"))

                self.about_window.show()

            def connection():

                try:

                    time.sleep(1.5)

                    try:

                        self.connect = mysql.connector.connect(
                            host = 'localhost',
                            user = 'root',
                            password = '2023',
                            database = f'password_managerdb_{username_K}',
                            auth_plugin='mysql_native_password'
                        )

                        self.cursor = self.connect.cursor()

                    except:

                        self.connect = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='2023',
                            auth_plugin='mysql_native_password'
                        )

                        self.cursor = self.connect.cursor()
                        self.cursor.execute(f"CREATE SCHEMA IF NOT EXISTS password_manager_{username_K}")
                        self.connect.commit()

                        self.connect.close()

                        self.connect = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='2023',
                            database=f'password_manager_{username_K}',
                            auth_plugin='mysql_native_password'
                        )

                        self.cursor = self.connect.cursor()

                        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `username_data` (
                                               `username_id` int NOT NULL AUTO_INCREMENT,
                                               `username` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
                                               PRIMARY KEY (`username_id`)
                                               ) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci""")

                        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `user_data` (
                                               `id` int NOT NULL AUTO_INCREMENT,
                                               `website_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
                                               `username_id` int NOT NULL,
                                               `password` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
                                               PRIMARY KEY (`id`),
                                               UNIQUE KEY `id_UNIQUE` (`id`),
                                               KEY `username_id_idx` (`username_id`),
                                               CONSTRAINT `username_id` FOREIGN KEY (`username_id`) REFERENCES `username_data` (`username_id`)
                                               ) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci""")

                        self.connect.commit()

                    self.main.database_control.setStyleSheet("""border-radius: 25px;
                                                           background-color: green;
                                                           color: white;
                                                           width: 50px;
                                                           height: 50px; """)

                    self.main.label_control.setText("Database Connected")

                    self.main.all_show.setEnabled(True)
                    self.main.save_new.setEnabled(True)
                    self.main.search.setEnabled(True)
                    self.main.save_change.setEnabled(True)
                    self.main.data_delete.setEnabled(True)

                except Exception as ex:
                    print(f"Hata : {ex}") #---------------------------------------------------------------------> Bakılacak yer.

                    self.main.database_control.setStyleSheet("""
                                        border-radius: 25px;
                                        background-color: red;
                                        color: white;
                                        width: 50px;
                                        height: 50px; """)

                    self.main.label_control.setText("Database Not Connected")

            self.close() # Login penceresini kapattım.
            self.connect.close() # Login database kapattım.

            self.main_window = QMainWindow()
            self.main = Ui_MainWindow_main()

            self.main.setupUi(self.main_window)

            self.main_window.setWindowTitle("Password Manager")
            self.main_window.setWindowIcon(QIcon("Resimler/key_siyah.png"))

            self.main.about.clicked.connect(about_func)

            self.main.generate_password_new.clicked.connect(self.generate_password)
            self.main.generate_password_edit.clicked.connect(self.generate_password)

            self.main.user_settings.clicked.connect(user_settings)
            self.main.change_user.clicked.connect(change_user)

            self.main.all_show.clicked.connect(all_show)
            self.main.save_new.clicked.connect(add_new)
            self.main.search.clicked.connect(username_search)
            self.main.save_change.clicked.connect(edit_information)
            self.main.data_delete.clicked.connect(delete_db)

            self.main.all_show.setEnabled(False)
            self.main.save_new.setEnabled(False)
            self.main.search.setEnabled(False)
            self.main.save_change.setEnabled(False)
            self.main.data_delete.setEnabled(False)

            connect_thread = Thread(target=connection)
            connect_thread.start()

            # Tablo Ayarları -- >
            self.main.girdiler.setColumnWidth(0,50)
            self.main.girdiler.setColumnWidth(1, 215)
            self.main.girdiler.setColumnWidth(2, 215)
            self.main.girdiler.setColumnWidth(3, 215)
            self.main.girdiler.setColumnWidth(4, 215)

            self.main_window.show()

        def __del__(self):

            self.connect.close()
            #self.message_box("Bilgi","İYİ GÜNLER",QMessageBox.Icon.Information,"Resimler/information-button_beyaz.png")



    if __name__ == "__main__":
        app = QApplication([])
        window = Password_Manager()  # doğru şekilde MainWindow sınıfı kullanılıyor
        window.show()
        app.exec()

    del window

except Exception as ex:
    self.message_box("Info",f"Hata Mesajı : {ex}",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png")      # --------------------------------> 10 DaKİKA ARA YEMEK-WC