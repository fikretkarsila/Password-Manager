import sys
import time
from random import choice
from threading import Thread
from random import randint
import mysql.connector #Veritabanı bağlantı
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

def condition_box(Title,Contents,Signal,Picture_Path):
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
            self.login.eye_password.clicked.connect(self.view_hide)
            self.login.create_account.clicked.connect(self.create_account)

            self.login.login.setShortcut('Return')

            self.login_connectDb_password()
            self.change = True

        def create_account(self):

            self.change = True

            def save():

                try:

                    username = create.username.text().strip()
                    password = create.password.text().strip()
                    password_again = create.password_again.text().strip()

                    if len(username) == 0 or len(password) == 0 or len(password_again) == 0:
                        raise SyntaxError(message_box("Info", "Fill in all fields.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))
                    elif password != password_again:
                        raise SyntaxError(message_box("Info", "Passwords do not match.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT username FROM login_password")
                    users,control = self.cursor.fetchall(),False

                    print(username)

                    for user in users:
                        if user[0] == username:
                            control = True
                            break

                    if control:
                        raise SyntaxError(message_box("Info", "There is already such a user.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))
                    else:

                        self.cursor.execute("INSERT INTO login_password(username,password) VALUES (%s,%s)",(username,password))
                        self.connect.commit()

                        for widget in self.findChildren(QLineEdit):
                            widget.clear()

                        message_box("Info", f"Your registration has been successfully created. Please make a note of your username and password.\n\nUsername :  {username}\nPassword : {password}", QMessageBox.Icon.Information,"Resimler/information-button_beyaz.png")

                        self.main_create.close()
                        self.show()

                except Exception as ex:
                    print(ex)

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

                        create.password.setText(sifre)
                        create.password_again.setText(sifre)

                        time.sleep(0.01)

                threading_1 = Thread(target=uret)
                threading_1.start()

            def back_frost():
                try:

                    for widget in self.findChildren(QLineEdit):
                        widget.clear()

                    self.main_create.close()
                    self.show()

                except Exception as ex:
                    print(ex)

            def view_hide():

                if self.change:
                    create.password.setEchoMode(QLineEdit.EchoMode.Normal)
                    create.password_again.setEchoMode(QLineEdit.EchoMode.Normal)
                    create.eye_password.setIcon(QIcon("Resimler/hide.png"))
                    self.change = False
                else:
                    create.password.setEchoMode(QLineEdit.EchoMode.Password)
                    create.password_again.setEchoMode(QLineEdit.EchoMode.Password)
                    create.eye_password.setIcon(QIcon("Resimler/view.png"))
                    self.change = True

            self.close()

            self.main_create = QMainWindow()
            create = Ui_MainWindow_create()
            create.setupUi(self.main_create)

            create.back_frost.clicked.connect(back_frost)
            create.generate_password.clicked.connect(generate_password)
            create.eye_password.clicked.connect(view_hide)
            create.create_register.clicked.connect(save)

            create.create_register.setShortcut("Return")

            self.main_create.setWindowTitle('New Account')
            self.main_create.setWindowIcon(QIcon('Resimler/user_beyaz.png'))

            self.main_create.show()

        def view_hide(self):

            if self.change:
                self.login.password.setEchoMode(QLineEdit.EchoMode.Normal)
                self.login.eye_password.setIcon(QIcon("Resimler/hide.png"))
                self.change = False
            else:
                self.login.password.setEchoMode(QLineEdit.EchoMode.Password)
                self.login.eye_password.setIcon(QIcon("Resimler/view.png"))
                self.change = True

        def login_reset(self,window = 'login',username_K = ''):

            self.change = True

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

                        self.main(username_K).connection()

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
                        raise SyntaxError(message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT id,username FROM login_password") # Sorgu ile id ve kullanıcı adını çekildi.
                    users = self.cursor.fetchall() # users olan kullanıcıları gönderildi.

                    Id,control_user = False,'' # Kontrol değişkenleri oluşturuldu.
                    for Id,username in users:
                        if username == username_app:
                            control_user = True
                            break
                    else:
                        raise SyntaxError(message_box("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                       "Resimler/information-button_beyaz.png"))

                    if control_user:
                        if password_app == password_repeat_app:
                            self.cursor.execute(f"UPDATE login_password SET password = '{password_app}' WHERE id = %s",(Id,))
                            self.connect.commit()

                            message_box("Info","Password change successful.",QMessageBox.Icon.Information,"Resimler/notification_beyaz.png")

                            self.login_window.close()

                            if window == 'login':
                                self.show()
                            else:

                                self.main(username_K).connection()

                                self.main_window.show()
                        else:
                            message_box("Info", "Passwords do not match.", QMessageBox.Icon.Warning,
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

            login_main.back_frost.clicked.connect(back_frost)
            login_main.reset_password.clicked.connect(forgot_password)
            login_main.generate_password.clicked.connect(generate_password)
            login_main.eye_password.clicked.connect(gorunur)

            login_main.reset_password.setShortcut("Return")

            self.login_window.setWindowTitle("Reset Password")
            self.login_window.setWindowIcon(QIcon("Resimler/refresh_siyah.png"))

            if not window:
                window = 'login'

            if len(username_K) != 0:
                login_main.username.setText(username_K)
                login_main.username.setEnabled(False)

            self.login_window.show()
        def login_connectDb_password(self):

            try:
                self.connect = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    passwd='2023',
                    database='password_manager',
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

                self.cursor.execute("CREATE SCHEMA IF NOT EXISTS password_manager")

                self.connect.close()

                self.connect = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='2023',
                    database='password_manager',
                    auth_plugin='mysql_native_password'
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
                    raise SyntaxError(message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

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
                        raise SyntaxError(message_box("Info", "No such user was found.", QMessageBox.Icon.Critical,
                                                       "Resimler/information-button_beyaz.png"))

                    message_box("Info","Username and/or password are incorrect.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png")

                if control_2:

                    self.login.username.clear()
                    self.login.password.clear()

                    return self.main(username)



            except Exception as ex:
                print(ex)
        def main(self,username_K):

            def delete_db():

                try:
                    id = main.id_del.text().strip()

                    if len(id) == 0:
                        raise SyntaxError(message_box("Info", "Fill in all fields.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT id FROM user_data")
                    control_id, users_id = False, self.cursor.fetchall()

                    for user_id in users_id:
                        if str(user_id[0]) == id:
                            control_id = True
                            break

                    if not control_id:
                        raise SyntaxError(message_box("Info", "No record found with this id.", QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))


                    result = condition_box("Info","Are you sure you want to delete ?",QMessageBox.Icon.Critical,"Resimler/information-button_beyaz.png")

                    if result:
                        self.cursor.execute("DELETE FROM user_data WHERE id = %s",(id,))
                        self.connect.commit()

                        message_box('Info', 'The deletion was successful.', QMessageBox.Icon.Information,'Resimler/info-button_beyaz.png')

                        all_show()

                    main.id_del.clear()


                except Exception as ex:
                    print(ex)

            def edit_information(): # Bakılacak unutma !

                try:

                    id = main.id_edit.text().strip()
                    website = main.website_edit.text().strip()
                    username = main.username_edit.text().strip()
                    password = main.password_edit.text().strip()
                    password_repeat = main.password_repeat_edit.text().strip()

                    if len(id) == 0 or len(website) == 0 or len(username) == 0 or len(password) == 0 or len(password_repeat) == 0:
                        raise SyntaxError(message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

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

                            for widget in main.groupBox_2.findChildren(QLineEdit):
                                widget.clear()

                        else:

                            self.cursor.execute("INSERT INTO username_data(username) VALUES (%s)",(username,))
                            self.connect.commit()

                            self.cursor.execute("UPDATE user_data SET website_name = %s,username_id = %s,password = %s WHERE id = %s",(website, self.cursor.lastrowid, password,id))
                            self.connect.commit()

                            for widget in main.groupBox_2.findChildren(QLineEdit):
                                widget.clear()


                        message_box('Info', 'Registration successfully added.', QMessageBox.Icon.Information,
                                     'Resimler/info-button_beyaz.png')

                        all_show()
                    else:
                        raise SyntaxError(message_box("Info","No record found with this id.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))


                except Exception as ex:
                    print(ex)

            def username_search():

                try:

                    username = main.username_search.text().strip()

                    if len(username) == 0:
                        raise SyntaxError(message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute(f"""SELECT id,website_name,username_data.username,password FROM user_data 
                                        INNER JOIN username_data ON user_data.username_id = username_data.username_id
                                        WHERE username_data.username LIKE '%{username}%'
                                         """)

                    infos, rowIndex = self.cursor.fetchall(), 0  # Bilgilerimizi değişkene attık.

                    if len(infos) == 0:
                        raise SyntaxError(message_box("Info","No Records Found.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    main.girdiler.setRowCount(0)

                    for write in infos:
                        rowCount = main.girdiler.rowCount()

                        main.girdiler.insertRow(rowCount)

                        main.girdiler.setItem(rowIndex, 0, QTableWidgetItem(str(write[0])))
                        main.girdiler.setItem(rowIndex, 1, QTableWidgetItem(str(write[1])))
                        main.girdiler.setItem(rowIndex, 2, QTableWidgetItem(str(write[2])))
                        main.girdiler.setItem(rowIndex, 3, QTableWidgetItem(str(write[3])))

                        rowIndex += 1

                    for widget in main.groupBox_3.findChildren(QLineEdit):
                        widget.clear()

                except Exception as ex:
                    print(ex)

            def add_new():

                try:

                    website_name = main.website_new.text().strip()
                    username = main.username_new.text().strip()
                    password = main.password_new.text().strip()
                    password_repeat = main.password_repeat_new.text().strip()

                    if len(website_name) == 0 or len(username) == 0 or len(password) == 0 or len(password_repeat) == 0:
                        raise SyntaxError(message_box("Info","Fill in all fields.",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png"))

                    self.cursor.execute("SELECT * FROM username_data")
                    users,user_control = self.cursor.fetchall(),False

                    for Id,user in users:
                        if user == username:
                            user_control = True
                            break

                    if user_control:
                        self.cursor.execute(f"INSERT INTO user_data (website_name,username_id,password) VALUES (%s,'{Id}',%s)",(website_name,password))
                        self.connect.commit()

                        message_box('Info','Registration successfully added.',QMessageBox.Icon.Information,'Resimler/info-button_beyaz.png')

                        for widget in main.groupBox.findChildren(QLineEdit):
                            widget.clear()
                    else:
                        self.cursor.execute("INSERT INTO username_data (username) VALUES (%s)",(username,))
                        self.connect.commit()

                        Id = self.cursor.lastrowid

                        self.cursor.execute(f"INSERT INTO user_data (website_name,username_id,password) VALUES (%s,'{Id}',%s)",(website_name,password))
                        self.connect.commit()

                        message_box('Info', 'Registration successfully added.', QMessageBox.Icon.Information,
                                     'Resimler/info-button_beyaz.png')

                        for widget in main.groupBox.findChildren(QLineEdit):
                            widget.clear()

                    all_show()
                except Exception as ex:
                    print(ex)

            def all_show():

                main.girdiler.clearContents() # Tabloları temizledim.

                time.sleep(0.2)

                self.cursor.execute("SELECT id,website_name,username_data.username,password FROM user_data inner join username_data ON user_data.username_id = username_data.username_id")
                infos,rowIndex = self.cursor.fetchall(),0 # Bilgilerimizi değişkene attık.

                main.girdiler.setRowCount(0)

                for write in infos:
                    rowCount = main.girdiler.rowCount()

                    main.girdiler.insertRow(rowCount)

                    main.girdiler.setItem(rowIndex,0,QTableWidgetItem(str(write[0])))
                    main.girdiler.setItem(rowIndex,1, QTableWidgetItem(str(write[1])))
                    main.girdiler.setItem(rowIndex, 2, QTableWidgetItem(str(write[2])))
                    main.girdiler.setItem(rowIndex,3,QTableWidgetItem(str(write[3])))

                    rowIndex += 1

            def user_settings():

                self.main_window.close()
                self.connect.close()

                self.login_connectDb_password()
                self.login_reset('main',username_K)

            def login_go():

                for widget in self.findChildren(QLineEdit):
                    widget.clear()

                main.database_control.setStyleSheet("""
                                                        border-radius: 25px;
                                                        background-color: red;
                                                        color: white;
                                                        width: 50px;
                                                        height: 50px; 
                                                    """)

                main.label_control.setText("Database Not Connected")

                self.main_window.close()

                self.connect.close()

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

                    main.database_control.setStyleSheet("""border-radius: 25px;
                                                           background-color: green;
                                                           color: white;
                                                           width: 50px;
                                                           height: 50px; """)

                    main.label_control.setText("Database Connected")

                    main.all_show.setEnabled(True)
                    main.save_new.setEnabled(True)
                    main.search.setEnabled(True)
                    main.save_change.setEnabled(True)
                    main.data_delete.setEnabled(True)

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
            main.save_new.clicked.connect(add_new)
            main.search.clicked.connect(username_search)
            main.save_change.clicked.connect(edit_information)
            main.data_delete.clicked.connect(delete_db)

            main.all_show.setEnabled(False)
            main.save_new.setEnabled(False)
            main.search.setEnabled(False)
            main.save_change.setEnabled(False)
            main.data_delete.setEnabled(False)

            connect_thread = Thread(target=connection)
            connect_thread.start()

            # Tablo Ayarları -- >
            main.girdiler.setColumnWidth(0,50)
            main.girdiler.setColumnWidth(1, 215)
            main.girdiler.setColumnWidth(2, 215)
            main.girdiler.setColumnWidth(3, 215)
            main.girdiler.setColumnWidth(4, 215)

            self.main_window.show()

    application = QApplication(sys.argv)
    window = Password_Manager()
    window.show()
    sys.exit(application.exec())

except Exception as ex:
    message_box("Info",f"Hata Mesajı : {ex}",QMessageBox.Icon.Warning,"Resimler/information-button_beyaz.png")