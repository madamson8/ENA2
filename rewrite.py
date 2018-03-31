import os
import getpass
import psycopg2
import sys
import traceback
import hashlib


class ENA(object):

    available_commands = {
        'help',
        'login',
        'create user',
        'exit'
    }

    def clear(self):
        os.system('cls')

    def ena(self):
        for i in range(30):
            print()
        print("Hello, my name is ENA.")
        print("I was created by Heber Brau and Matthew Adamson to assist in everyday tasks.")
        print("Connecting...")
        conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            print("Connected!")
            print()
            print("Please login to continue.")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            hashlib.sha256(password).hexdigest()
        except:
            traceback.format_exc()

    def database(self):
        pass


ena = ENA()
ena.ena()
