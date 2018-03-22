import os
from src.User import Edit_Users
import src.Deploy
from settings import create_tables
import getpass
from os.path import expanduser


class ENA():
    HOME = expanduser("~")

    running = False

    main_user = None
    ena = None
    id = None
    edit_users = Edit_Users()

    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"

    no_user_commands = [
        'help',
        'login',
        'create user',
        'exit'
    ]

    available_commands = [
            'help',
            'deploy',
            'logout',
            'exit'
    ]

    users = []
    def ena(self, ena):
        self.running = True
        self.ena = ena
        try:
            self.id = self.edit_users.load_users(ena)
        except:
            Create_Tables = create_tables()
            Create_Tables.create_tables(ena)
            self.id = self.edit_users.load_users(ena)
        self.ena.run()

    def ena_help(self):
        if(not self.main_user == None):
            print("=======================================")
            for i in self.available_commands:
                print(i)
            print("=======================================")
        else:
            print("=======================================")
            for i in self.no_user_commands:
                print(i)
            print("=======================================")

    def exit(self):
        print("Exiting")


    def run(self):
        self.clear()
        command = input("Hello, my name is Ena, how may I assist you today: ")
        while(self.running):
            if(not self.main_user == None):
                if(command.lower() == "help"):
                    self.clear()
                    print("----HELP----")
                    self.ena_help()
                elif(command.lower() == "deploy"):
                    self.clear()
                    # deploy.deploy()
                    print("----DEPLOY----")

                elif(command.lower() == "logout"):
                    self.clear()
                    print("----LOGOUT----")
                    self.logout()
                elif(command.lower() == "exit"):
                    self.clear()
                    exit()
                else:
                    self.clear()
                    print("Im sorry, I did not get that")
            else:
                if(command.lower() == "help"):
                    self.clear()
                    print("----HELP----")
                    self.ena_help()
                elif(command.lower() == "login"):
                    self.clear()
                    print("----LOGIN----")
                    self.login()
                elif(command.lower() == "create user"):
                    self.clear()
                    print("----CREATE USER----")
                    self.edit_users.create_user(self.ena, self.id)
                elif(command.lower() == "exit"):
                    self.clear()
                    exit()
                else:
                    print("Im sorry, I did not get that")
            command = input("How may I assist you today: ")

    def login(self):
        testing_username = input("username: ")
        for user in self.users:
            if(user.username == testing_username):
                temp_id = user.id
                testing_password = getpass.getpass("Password: ")
                test = self.users[temp_id-1].user_login(testing_password, user.password)
                if(test):
                    user.logged_in = True
                    self.main_user = user
        if(not self.main_user == None):
            print("noice, " + self.main_user.username + ", Your logged in")
        else:
            print("username or password is incorrect")

    def logout(self):
        for user in self.users:
            user.logged_in = False
        self.main_user == None
        print("You are now logged out")

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


def main():
    #emptyrn
    print("running")


if __name__ == "__main__":
    ena = ENA()
    main()
    ena.ena(ena)
