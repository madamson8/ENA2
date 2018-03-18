import psycopg2
import sys
from User import User

class ENA():
    available_commands = [
            'help',
            'login'
    ]

    users = []

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
        create_user()
        self.ena_help()

class load_users():
    def create_user(self, ena, conn, cursor):
        user = User()
        level = 0
        cursor.execute("SELECT * FROM Users;")
        for user_info in cursor:
            user.user(user_info[0], user_info[1], user_info[2], user_info[3])
            print(user_info)
            ena.users.append(user)
            level = user_info[0]
        #cursor.execute("INSERT INTO Users VALUES(2,%s,%s,%s)", (username, password, level))
        conn.commit()
        return level

def main():
    ena = ENA()
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    print("Connecting to a database\n ->")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")

    create_user_test = load_users()
    create_user_test.create_user(ena, conn, cursor)

main()
