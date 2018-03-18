import psycopg2
import sys
from User import User

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
        create_user()
        self.ena_help()

class create_user():
    def create_user():
        username = input("please enter username:")
        password = input("please enter password:")
        user = User(username, password, 0)

        cursor.execute("CREATE TABLE User (reading String not null)")
        query = "INSERT INTO username values (?);"
        cursor.execute(query, [username])
        # save changes to file for next exercise
        connection.commit()
        connection.close()



def main():
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    print("Connecting to a database\n ->")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")


    username = input("please enter username:")
    password = input("please enter password:")
    user = User()
    user.user(username, password, 0,)

    cursor.execute("CREATE TABLE User (reading String not null)")
    query = "INSERT INTO username values (?);"
    cursor.execute(query, [username])
    # save changes to file for next exercise
    connection.commit()
    connection.close()


ena = ENA()
# ena.run()
main()





    # def login():
    #     if(pass == inputpassword):
    #         return True
    #     else:
    #         return False
