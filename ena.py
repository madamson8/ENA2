import psycopg2
import sys
from User import User, Edit_Users

class ENA():
    ena = None
    id = None
    edit_users = Edit_Users()

    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"



    available_commands = [
            'help',
            'login'
    ]

    users = []
    def ena(self, ena):
        self.ena = ena
        self.id = self.edit_users.load_users(ena)
        self.ena.run()

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
        self.edit_users.create_user(self.ena, self.id)

def main():
    #emptyrn
    print("running")

if __name__ == "__main__":
    ena = ENA()
    main()
    ena.ena(ena)
