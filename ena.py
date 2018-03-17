import psycopg2
import sys
from subprocess import call
from pathlib import Path


class ENA(object):
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


def main():
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    print("Connecting to a database\n ->")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")
    conn.close()

if __name__ == "__main__":
    main()
    ena = ENA()
    ena.run()


ena = ENA()
ena.run()


