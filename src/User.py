from passlib.hash import pbkdf2_sha256
import psycopg2
import getpass
import easygui

class User:
    id = None
    username = None
    password = None
    level = None
    logged_in = False
    abs_path = ""

    def user(self, id, username, password, level, abs_path):
        self.id = id
        self.username = username
        self.password = password
        self.level = level
        self.abs_path = abs_path


    def change_level(self, level_key, level_num):
        if(pbkdf2_sha256.encrypt(level_key, rounds=200000, salt_size=16)):
            self.level = level_num
            print("level changed")
        else:
            print("key incorrect")

    def change_username(self, new_username):
        self.username = new_username
        print("username changed")

    def create_password(self, password):
        return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)

    def change_password(self, new_password):
        if(pbkdf2_sha256.encrypt(new_password, rounds=200000, salt_size=16)):
            self.password = new_password
            print("Password changed")
        else:
            print("Password incorrect")

    def user_login(self, password, test_password):
        test = pbkdf2_sha256.verify(password, self.password)
        return test

class Edit_Users():
    def load_users(self, ena):
        conn = psycopg2.connect(ena.conn_string)
        cursor = conn.cursor()
        id = 0
        level = 0
        cursor.execute("SELECT * FROM Users;")
        # Remember to add fields added to the user constructor here.
        # To add the fields to the column add them in settings.py
        for user_info in cursor:
            user = User()
            user.user(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4])
            ena.users.append(user)
            id = user_info[0]
        conn.commit()
        conn.close()

        return id

    def create_user(self, ena, id):
        user = User()
        conn = psycopg2.connect(ena.conn_string)
        cursor = conn.cursor()
        username = input("username: ")
        password = user.create_password(getpass.getpass("Password: "))
        level = 0
        id += 1
        abs_path = easygui.fileopenbox()
        cursor.execute("INSERT INTO Users VALUES(%s,%s,%s,%s,%s)", (id, username, password, level, abs_path))
        conn.commit()
        conn.close()
        user.user(id, username, password, level, abs_path)
        ena.users.append(user)
