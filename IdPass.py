from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
from Choose import main
from PIL import Image, ImageTk
import tkinter
import mysql.connector

data_base = None
da = 0

mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", port="3306", database="utilizatori", auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("select * from tabel1")

users = mycursor.fetchall()

class IdPass:
        global data_base
        global mycursor

        data_base = {}
        for user in users:
           data_base[user[1]] = user[2]
        print(data_base)

def main():
    new = IdPass


def check_user(var_user):
    global da
    global data_base
    x = data_base.get("username")
    print(x)

    for u in data_base:
        print(u)
        if u == var_user:
            return u


def check_pass(var_pass):
    global da
    x = data_base.get("password")
    print(x)

    for p in data_base.values():
        if p == var_pass:
            return p


if __name__ == "__main__":
    check_user()
    check_pass()

