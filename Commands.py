import sys
import os
from User import User, Edit_Users

class Commands():
    user = None
    ena = None

    #command arrays
    no_user_commands_array = [
        'help',
        'login',
        'create user',
        'exit'
    ]

    admin_commands_array = [
        'help',
        'create run file',
        'deploy',
        'show user information',
        'show users information',
        'logout',
        'exit'
    ]

    level_1_commands_array = [
        'help',
        'deploy',
        'show user information',
        'logout',
        'exit'
    ]

    lowest_level_commands_array = [
        'help',
        'show user information',
        'logout',
        'exit'
    ]

    #constructor
    def commands(self, ena, user):
        #created to make it possible to call user or ena without making a new instance
        self.ena = ena
        self.user = user

    def test_commands(self, command, user):
        self.user = user
        #Logged in
        if(not self.user == None):
            #Admin
            if(self.user.level == 0):
                self.admin_commands(command)
            #Level 1
            elif(self.user.level == 1):
                self.level_1_commands(command)
            #Lowest level
            else:
                self.lowest_level_commands(command)
        #Not logged in
        else:
            self.no_user_commands(command)

    def admin_commands(self, command):
        #clears the screen, lables what is happening, then runs an admin function
        self.ena.clear()
        print("----ADMIN----")
        self.label(command)
        #checks command, then runs functions
        if(command.lower() == "create run file"):
            self.user.create_run_file()
        elif(command.lower() == "help"):
            self.ena.ena_help(self.admin_commands_array)
        elif(command.lower() == "deploy"):
            self.ena.deploy()
        elif(command.lower() == "show user information"):
            self.user.show_info()
        elif(command.lower() == "show users information"):
            self.ena.show_users()
        elif(command.lower() == "logout"):
            self.ena.logout()
        elif(command.lower() == "exit"):
            self.exit()
        else:
            print("Im sorry, I did not get that")

    def level_1_commands(self, command):
        #clears the screen, lables what is happening
        self.ena.clear()
        self.label(command)
        #checks command, then runs functions
        if(command.lower() == "help"):
            self.ena.ena_help(self.level_1_commands_array)
        elif(command.lower() == "deploy"):
            self.ena.deploy()
        elif(command.lower() == "show user information"):
            self.user.show_info()
        elif(command.lower() == "logout"):
            self.ena.logout()
        elif(command.lower() == "exit"):
            self.exit()
        else:
            print("Im sorry, I did not get that")

    def lowest_level_commands(self, command):
        #clears the screen, lables what is happening
        self.ena.clear()
        self.label(command)
        #checks command, then runs functions
        if(command.lower() == "help"):
            self.ena.ena_help(self.lowest_level_commands_array)
        elif(command.lower() == "show user information"):
            self.user.show_info()
        elif(command.lower() == "logout"):
            self.ena.logout()
        elif(command.lower() == "exit"):
            self.exit()
        else:
            print("Im sorry, I did not get that")

    def no_user_commands(self, command):
        #clears the screen, lables what is happening
        self.ena.clear()
        self.label(command)
        #checks command, then runs functions
        if(command.lower() == "help"):
            self.ena.ena_help(self.no_user_commands_array)
        elif(command.lower() == "login"):
            self.ena.login()
        elif(command.lower() == "create user"):
            self.ena.edit_users.create_user(self.ena, self.id)
        elif(command.lower() == "exit"):
            self.exit()
        else:
            print("Im sorry, I did not get that")

    def label(self, label):
        #labels look like ----LABEL----
        print("----" + label.upper() + "----")

    def exit(self):
        #clears screen then exits program
        self.ena.clear()
        exit()
