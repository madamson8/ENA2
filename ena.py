import psycopg2
import sys
from passlib.hash import pbkdf2_sha256
[]

password = "asdf"
pass_hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)



class ENA():
    available_commands = [
            'help',
            'login'
    ]

    def ena_help(self):
        for i in self.available_commands:
            print(i)

    def exit(self):
        print("Exiting")

    def deploy(self):
        yn = input("Do you have heroku installed? Y/n ")
        if yn.lower() == "y":
            print("Beginning Deployment.")
            print("Creating siteinfo.html")
            yn = input("I have detected your home as: " + str(Path.home()) + ".  Is this correct? Y/n ")
            if yn.lower() == "y":
                filepath = input("Please enter the path to the root of your project: ")
                try:
                    new_filepath = "" + filepath
                    file = open(new_filepath, 'r')
                except:
                    pass
                call("heroku login")
        else:
            print("Please install the Heroku CLI to contine.")
            exit()

    def run(self):
        self.ena_help()


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


ena = ENA()
ena.run()





    # def login():
    #     if(pass == inputpassword):
    #         return True
    #     else:
    #         return False
