from tkinter import *
import tkinter
from PIL import ImageTk, Image
import Univers
import Istorie
import Geografie
import It
import Fitness
import CheckScore
import inspect
import Choose
from Choose import *
from tkinter import ttk

argument2 = 0

# Functia "main()" preia cu ajutorul parametriilor valorile vechi si curente din lista de raspunsuri.
# Fereastra cu verificare scor va fi afisata deasupra tuturor ferestrelor.
# Se returneaza fereastra si lista de raspunsuri.
def main(dictt, old_dictt, var, neww):
    root = Toplevel()
    i = CheckInfo(root, dictt, old_dictt, var, neww)
    root.mainloop()
    return root, dictt

# Functie utilizata pentru a reseta toate valorile din dictionar cu valoarea 0, pentru a sterge raspunsurile memorate.
# In cazul in care apasam pe butonul "Incearca din nou".
def funct2():
    argum2 = argument2
    if argum2 == 1:
        def reset_answer_user():
            for x in list(Istorie.answer_user.keys()):
                print()
                for y in list(Istorie.answer_user[x].keys()):
                    Istorie.answer_user[x].update({y: 0})
                print(Istorie.answer_user[x].values())
        reset_answer_user()
        Istorie.try_again()
        Istorie.incr_all = 0
        Istorie.checked = 0
    if argum2 == 2:
        def reset_answer_user():
            for x in list(Univers.answer_user.keys()):
                print()
                for y in list(Univers.answer_user[x].keys()):
                    Univers.answer_user[x].update({y: 0})
                print(Univers.answer_user[x].values())

        reset_answer_user()
        Univers.try_again()
        Univers.incr_all = 0
        Univers.checked = 0

    if argum2 == 3:
        def reset_answer_user():
            for x in list(Geografie.answer_user.keys()):
                print()
                for y in list(Geografie.answer_user[x].keys()):
                    Geografie.answer_user[x].update({y: 0})
                print(Geografie.answer_user[x].values())

        reset_answer_user()
        Geografie.try_again()
        Geografie.incr_all = 0
        Geografie.checked = 0
    if argum2 == 4:
        def reset_answer_user():
            for x in list(It.answer_user.keys()):
                print()
                for y in list(It.answer_user[x].keys()):
                    It.answer_user[x].update({y: 0})
                print(It.answer_user[x].values())

        reset_answer_user()
        It.try_again()
        It.incr_all = 0
        It.checked = 0
    if argum2 == 5:
        def reset_answer_user():
            for x in list(Fitness.answer_user.keys()):
                print()
                for y in list(Fitness.answer_user[x].keys()):
                    Fitness.answer_user[x].update({y: 0})
                print(Fitness.answer_user[x].values())

        reset_answer_user()
        Fitness.try_again()
        Fitness.incr_all = 0
        Fitness.checked = 0

# Functie utilizata pentru a reseta scorul in cazul in care se apasa iconita "X" din fereastra curenta.
def close_wind_reset_score(root, dictt):
    root.destroy()
    root.quit()
    for x in list(dictt.keys()):
        for y in list(dictt[x].keys()):
            dictt[x].update({y: 0})
    print(dictt)

# Functie utilizata pentru inchiderea ferestrei adaugate ca si parametru.
def close_app(root):
    root.destroy()


class CheckInfo():

    # Functia "__init__" reprezinta constructorul clasei. Aceasta este apelata in momentul in care se creeaza un obiect
    # al clasei.
    # Self reprezintă instanta clasei. Cu "self" putem accesa atributele si metodele clasei.
    # Parametrul master este widget-ul parinte si este un parametru opțional care este trimis noii instante a
    # clasei cand este initializata.
    def __init__(self, master, dictt, old_dictt, var, neww):

        # Widget-ul Frame este utilizat in scopul de a organiza un grup de widget-uri.
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=1)
        print("aicii" + str(list(dictt.values())))
        print("aicii" + str(list(old_dictt.values())))

        # Configuram parametrul "master"
        self.master = master
        self.master.title('Raspunsuri')

        # Am creat un obiect cu widget ul Canvas unde i-am setat latimea si lungimea.
        self.canvas = Canvas(frame, width=626, height=626)

        # Am adaugat cate o imagine pentu fiecare tip de intrebare din lista si am redimensionat imaginile.
        # Am folosit si Image.ANTIALIAS pentru a blura marginile pixelilor din imagine.
        # Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
        # BitmapImage si PhotoImage din imaginile din modulul PIL.
        self.image = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                "wall_background_mauve12.jpg")
        self.image = ImageTk.PhotoImage(self.image)

        # Se adauga imaginea de background, text-ul cu privire la scorul obtinut si butoanele ce ne vor directiona
        # la afisarea raspunsurilor corecte, la obtiunea de reincercare a testului si inchiderea ferestrei.
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
        self.canvas.create_text(250, 25, text="Raspunsuri", fill="white", anchor=NW,
                                font=('Arial Unicode MS', 20))
        self.canvas.create_text(290, 60, text="(" + str(var) + "/10)", fill="white", anchor=NW,
                                font=('Arial Unicode MS', 16))

        # x, y sunt folosite pentru pozitionarea textului pentru fiecare varianta de raspuns in frame.
        # si se numeroteaza intrebarile ( 1), 2) ..., 3) )
        x, y = 5, 100
        for numb in range(1, 11):
            self.canvas.create_text(x, y, text=f"{numb})", fill="white", anchor=NW,
                                    font=('Arial Unicode MS', 20))
            y += 100

        num = 0
        num2 = 0
        s = 100

        # Variabila utilizata pentru a intrerupe unele instructiuni din bucla "while"
        breaker_for = False

        # bucla "while" va rula atata timp pana cand toate intrebarile vor avea un raspuns ales de user.
        while num < 10:
            quiz_page = list(old_dictt.keys()).pop(num)

            for y in list(old_dictt[quiz_page].values()):
                if y == 1:
                    print(list(old_dictt[quiz_page].keys())[list(old_dictt[quiz_page].values()).index(1)])
                    user_correct = list(old_dictt[quiz_page].keys())[list(old_dictt[quiz_page].values()).index(1)]

                    quiz_user = list(dictt.keys()).pop(num2)

                    for p in list(dictt[quiz_user].values()):
                        if p == 1:
                            user_wrong = list(dictt[quiz_user].keys())[list(dictt[quiz_user].values()).index(1)]
                            print("Raspunsul user-ului: " + user_wrong)

                            # Se afiseaza raspunsul user-ului ca fiind corect in cazul in care corespunde cu
                            # variantele corecte memorate in lista originala.
                            if list(dictt[quiz_user].keys())[list(dictt[quiz_user].values()).index(1)] == \
                                    list(old_dictt[quiz_page].keys())[list(old_dictt[quiz_page].values()).index(1)]:
                                print("Raspuns corect: " + user_correct + ")")
                                self.canvas.create_text(45, s, text=f'Raspuns corect: {user_correct})', fill="green",
                                                        anchor=NW, font=('Arial Unicode MS', 20, 'bold'))
                                s += 100
                                print()
                                if num != 9 or num2 != 9:
                                    num += 1
                                    num2 += 1
                                else:
                                    breaker_for = True
                                    break
                            else:
                                # Afisarea raspunsului gresit si raspunsului ce era de fapt corect.
                                print("Raspuns gresit: " + user_wrong + ")")
                                print("Raspuns corect: " + user_correct + ")")
                                self.canvas.create_text(45, s, text=f'Raspuns gresit: {user_wrong})', fill="red",
                                                        anchor=NW, font=('Arial Unicode MS', 20, 'bold'))
                                self.canvas.create_text(45, s+50, text=f'Raspunsul corect era: {user_correct})',
                                                        fill="Grey",
                                                        anchor=NW, font=('Arial Unicode MS', 20, 'bold'))
                                s += 100
                                print()
                                if num != 9 or num2 != 9:
                                    num += 1
                                    num2 += 1
                                else:
                                    breaker_for = True
                                    break
            if breaker_for:
                break

        for x in list(dictt.keys()):
            for y in list(dictt[x].keys()):
                dictt[x].update({y: 0})

        print(dictt)

        # Functie utilizata pentru a reseta scorul in cazul in care se apasa iconita "X" din fereastra curenta.
        self.master.protocol("WM_DELETE_WINDOW", lambda: [close_wind_reset_score(self.master, dictt), neww.destroy()])

        # Am creat cate un obiect cu widget-ul Button, iar pentru parametrul "command" am utilizat lambda pentru a
        # apela mai multe instante si functii.
        self.button1 = Button(self.master, text="Incearca din nou", font=('Ink Fre', 12),
                              command=lambda: [neww.destroy(), close_app(self.master), funct2()])
        self.button2 = Button(self.master, text="Inchide", font=('Ink Fre', 12),
                              command=lambda: [neww.destroy(), close_app(self.master)])

        # Functiile "pack()" se apeleaza mereu pentru widget-uri pentru organizarea acestora
        # inaintea de a fi adaugate in widget-ul parinte.
        self.button1.pack()
        self.button2.pack()

        self.canvas.create_window(250, 1200, window=self.button1)
        self.canvas.create_window(400, 1200, window=self.button2)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Setam in ce parte a ferestrei ni se va afisa bara de derulare (scrollbar).
        self.my_scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # Aceste linii de cod le-am utilizat pentru a-mi permite sa scrolez in fereastra cu verificarea raspunsurilor.
        self.canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Imi afiseaza fereastra deasupra tuturor ferestrelor.
        self.master.wm_attributes("-topmost", 1)

        # Configurarea ferestrei window cu scopul de a nu se putea modifica dimensiunea acesteia.
        self.master.resizable(False, False)

        # "mainloop()" este folosit cu scopul de a rula bucla de evenimente Tkinter.
        self.master.mainloop()

# "if __name__ == '__main__'" codul va fi executat numai daca fisierul a fost rulat direct si nu a fost importat.
if __name__ == "__main__":
    main()
