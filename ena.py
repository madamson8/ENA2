import psycopg2
import sys
from User import User

class ENA():
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
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
        self.ena_help()

if __name__ == "__main__":
    main()
    ena = ENA()
    ena.run()

class Load_Users():
    def load_users(self, ena, conn, cursor):
        conn = psycopg2.connect(ena.conn_string)
        cursor = conn.cursor()
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
        conn.close()
        return level

def main():
    ena = ENA()
    load_users = Load_Users()

    load_users.load_user(ena, conn, cursor)

main()
