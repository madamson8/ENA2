import psycopg2
import sys
from passlib.hash import pbkdf2_sha256

password = "asdf"
pass_hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)


class ENA():
    available_commands = [
            'help',
            'login'
    ]

    def help():
        for i in available_commands:
            print(i)


    def deploy():
        print("Not ready yet.")


class password():
    def authenticate_user(password):
        print("hurray")
        return pbkdf2_sha256.verify(passsword, pass_hash)


def main():
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    print("Connecting to a database\n ->")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")
    pass_class = password()
    # test = input("pass:")
    # n_test = pass_class.authenticate_user(test)
    # print(n_test)

if __name__ == "__main__":
    main()





    # def login():
    #     if(pass == inputpassword):
    #         return True
    #     else:
    #         return False
