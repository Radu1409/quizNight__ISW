from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
from Choose import main
from PIL import Image, ImageTk
import tkinter

data_base = None
da = 0


class IdPass:
        global data_base
        data_base = {
            "username": ['user', 'Mihai'],
            "password": ['parola', 'alta_parola']
        }


def main():
    new = IdPass


def check_user(var_user):
    global da
    global data_base
    x = data_base.get("username")
    print(x)

    for u in data_base.get("username"):
        print(u)
        if u == var_user:
            da = list(data_base["username"]).index(var_user)
            return u


def check_pass(var_pass):
    global da
    x = data_base.get("password")
    print(x)

    for p in data_base.get("password"):
        if p == var_pass:
            print("da si aici!")
            if da == list(data_base["password"]).index(var_pass):
                return p


if __name__ == "__main__":
    check_user()
    check_pass()

