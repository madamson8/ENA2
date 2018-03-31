import os
import shutil
from src.User import User, Edit_Users
from src.deploy import Deploy
from src.Scheduler import Scheduler
from settings import create_tables
from Commands import Commands
import getpass
from os.path import expanduser


class ENA():
    HOME = expanduser("~")

    # Creating Objects
    edit_users = Edit_Users()
    commands = Commands()
    deploy = Deploy()
    # Booleans
    running = False
    # Objects
    main_user = None
    ena = None
    id = None
    # Strings
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    # Array for users
    users = []

    #constructor
    def ena(self, ena):
        self.running = True
        self.ena = ena
        #Creates the commands
        self.commands.commands(ena, self.main_user, self.deploy)
        self.commands = self.commands
        try:
            #Checks if there is a table, if so, it loads the users
            self.id = self.edit_users.load_users(ena)
        except:
            #Creates tables then loads empty users and sets the user id to 0
            Create_Tables = create_tables()
            Create_Tables.create_tables(ena)
            self.id = self.edit_users.load_users(ena)
        self.ena.run()

    #this command is used in Commands.py
    def ena_help(self, help_commands):
        print("=======================================")
        for i in help_commands:
            print(i)
        print("=======================================")


    #Admin function
    def show_users(self):
        for user in self.users:
            print("=======================================")
            user.show_info()
            print("=======================================")

    def login(self):
        testing_username = input("username: ")
        for user in self.users:
            #check for the username in the database
            if(user.username == testing_username):
                #checks password based of the id, the id is minus one because the array starts at zero and the id starts at one
                temp_id = user.id
                testing_password = getpass.getpass("Password: ")
                test = self.users[temp_id-1].user_login(testing_password, user.password)
                #logs in user
                if(test):
                    user.logged_in = True
                    self.main_user = user
        #this checks if the user is logged in, checks if they are admin, then lets them know they are logged in
        if(not self.main_user == None):
            self.clear()
            if(self.main_user.level == 0):
                print("----ADMIN----")
            print(self.main_user.username + ", You are now logged in")
        #this lets the user know that their password or username is incorrect
        else:
            print("username or password is incorrect")

    def logout(self):
        #this logs them out, as the functions name implies
        for user in self.users:
            user.logged_in = False
        self.main_user = None
        print("You are now logged out")

    def clear(self):
        #check if the user is using windows
        if os.name == 'nt':
            os.system('cls')
        #else it uses linux termianls 'clear'
        else:
            os.system('clear')

    def run(self):
        self.clear()
        #gets commands
        command = input("Hello, my name is Ena, how may I assist you today: ")
        #main running loop
        while(self.running):
            self.commands.test_commands(command, self.main_user)
            command = input("How may I assist you today: ")

if __name__ == "__main__":
    ena = ENA()
    ena.ena(ena)
