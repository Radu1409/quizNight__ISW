from tkinter import *
from tkinter import messagebox, colorchooser, filedialog
from Choose import main
from PIL import Image, ImageTk
import tkinter
import mysql.connector

data_base = None
da = 0

# Dupa ce am importat baza de date din mySQL, am conectat proiectul cu mySQL, unde i-am permis accesul introducand
# numele utilizatorului, parola de acces si numarul portului pe care v-a rula. De asemenea, am adaugat si numele
# bazei de date de unde va lua informatiile tuturor persoanelor inregistrate.
mydb = mysql.connector.connect(host="localhost", user="root", passwd="123456", port="3306", database="acces_users",
                               auth_plugin = 'mysql_native_password') #database="utilizatori"

# Aceasta metoda "cursor()" este utilizata pentru a putea executa instructiuni si pentru a comunica cu baza de date
# aleasa din mySQL.
mycursor = mydb.cursor()

# Aceasta functie are rolul de a executa o instructiune din mySQL.
# "select * from users_table" preia toate datele din tabelul "users_table"
mycursor.execute("select * from users_table") #mycursor.execute("select * from table1")

# Functia "fetchall()" returneaza intregul rezultat al unei inregistrari. Returneaza o lista de tupluri ce contin
# toate randurile. Daca nu exista nici o inregistrare de preluat, se returneaza o lista goala.
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

# Se verifica daca numele de utilizator introdus corespunde cu numele de utilizator din baza de date.
def check_user(var_user):
    global da
    global data_base
    x = data_base.get("user") #    x = data_base.get("username")
    print(x)

    for u in data_base:
        print(u)
        if u == var_user:
            return u

# Se verifica daca parola introdusa corespunde cu parola din baza de date.
def check_pass(var_pass):
    global da
    x = data_base.get("password") #    x = data_base.get("password")
    print(x)

    for p in data_base.values():
        if p == var_pass:
            return p

# "if __name__ == '__main__'" codul va fi executat numai daca fisierul a fost rulat direct si nu a fost importat.
if __name__ == "__main__":
    check_user()
    check_pass()

