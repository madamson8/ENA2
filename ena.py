import psycopg2
import sys

class ENA():
    available_commands = [
            'help',
            'login'
    ]

    def help():
        for i in available_commands:
            print(i)

    
    def deploy():
        print("Not ready yet.")


def main():
    conn_string = "host='localhost' dbname='enabrain' user='postgres' password='BrightBridge1'"
    print("Connecting to a database\n ->")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")

if __name__ == "__main__":
    main()

