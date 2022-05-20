from tkinter import *
import tkinter
from PIL import ImageTk, Image
import Istorie
import Univers
import Geografie
import It
import Fitness
from Choose import *


#importam modulul CheckInfo
import CheckInfo

# Initializam urmatoarele variabile cu 0.
argument = 0
numCountCheck = 0


def close_both(root1):
    # Functia "destroy()" permite inchiderea ferestrei cu referinta la obiect.
    root1.destroy()

# Declaram o functie cu 4 parametrii pentru a initializa listele cand selectam variantele de raspuns ce le consideram
# a fi corecte.
def main(var, new, dict, old_dict):

    # Declaram variabila urmatoare de tip global pentru a identifica script-ul ca facem referire la o variabila globala
    # deja declarata.
    global numCountCheck
    print(argument)

    # Functia "TopLevel()" este utilizata cu scopul de a aduce in evidenta prima fereastra fata de celelalte ferestre
    # deschise.
    root = Toplevel()

    # Functia "destroy()" este utilizata in scopul de a inchide fereastrea cu referinta la obiect.
    new.destroy()

    # Variabila d reprezinta referinta la obiect in momentul apelarii "CheckScore".
    d = CheckScore(root, var, new, dict, old_dict)

    # "mainloop()" este folosit cu scopul de a rula bucla de evenimente Tkinter.
    root.mainloop()

    # Se returneaza "root" si "dict"
    return root, dict


def funct():
    # Initializam "argum" cu valoarea din variabila "argument"
    argum = argument

    # In functie de valoarea "argum" (selectia tipului de intrebari), atunci se reseteaza cuvintele cheie (A, B, C, D)
    # din fiecare pagina, prin a face un update reinitializand toate valorile cuvintelor cheie cu 0. Functia "funct()"
    #  este utilizata pentru cazul in care utilizatorul doreste sa bifeze optiunea "Incearca din nou" din CheckScore.
    if argum == 1:
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
    if argum == 2:
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

    if argum == 3:
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
    if argum == 4:
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
    if argum == 5:
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


def close_wind_reset_score(root, dict):
    root.destroy()
    root.quit()
    for x in list(dict.keys()):
        # print()
        for y in list(dict[x].keys()):
            dict[x].update({y: 0})
            # print(list(Univers[x].values()))
    print(dict)


def functs():
    argum = argument

    # In functie de valoarea "argum" (selectia tipului de intrebari), atunci se reseteaza cuvintele cheie (A, B, C, D)
    # din fiecare pagina, prin a face un update reinitializand toate valorile cuvintelor cheie cu 0.
    if argum == 1:
        def reset_answer_user():
            for x in list(Istorie.answer_user.keys()):
                print()
                for y in list(Istorie.answer_user[x].keys()):
                    Istorie.answer_user[x].update({y: 0})
                print(Istorie.answer_user[x].values())

        reset_answer_user()
        Istorie.incr_all = 0
        Istorie.checked = 0
    if argum == 2:
        def reset_answer_user():
            for x in list(Univers.answer_user.keys()):
                print()
                for y in list(Univers.answer_user[x].keys()):
                    Univers.answer_user[x].update({y: 0})
                print(Univers.answer_user[x].values())
        reset_answer_user()
        Univers.incr_all = 0
        Univers.checked = 0

    if argum == 3:
        def reset_answer_user():
            for x in list(Geografie.answer_user.keys()):
                print()
                for y in list(Geografie.answer_user[x].keys()):
                    Geografie.answer_user[x].update({y: 0})
                print(Geografie.answer_user[x].values())

        reset_answer_user()
        Geografie.incr_all = 0
        Geografie.checked = 0
    if argum == 4:
        def reset_answer_user():
            for x in list(It.answer_user.keys()):
                print()
                for y in list(It.answer_user[x].keys()):
                    It.answer_user[x].update({y: 0})
                print(It.answer_user[x].values())

        reset_answer_user()
        It.incr_all = 0
        It.checked = 0
    if argum == 5:
        def reset_answer_user():
            for x in list(Fitness.answer_user.keys()):
                print()
                for y in list(Fitness.answer_user[x].keys()):
                    Fitness.answer_user[x].update({y: 0})
                print(Fitness.answer_user[x].values())

        reset_answer_user()
        Fitness.incr_all = 0
        Fitness.checked = 0


class CheckScore:

    # Functia "__init__" reprezinta constructorul clasei. Aceasta este apelata in momentul in care se creeaza un obiect
    # al clasei.
    # Self reprezintă instanta clasei. Cu "self" putem accesa atributele si metodele clasei.
    # Parametrul master este widget-ul parinte si este un parametru opțional care este trimis noii instante a
    # clasei cand este initializata.
    def __init__(self, master, var, new, dict, old_dict):

        # Widget-ul Frame este utilizat in scopul de a organiza un grup de widget-uri.
        frame = Frame(master)

        # Configuram parametrul "master"
        self.master = master
        self.master.title('Scor')
        self.master.geometry('400x200')
        if 'normal' == self.master.state():
            self.master.focus_set()
        if hasattr(Istorie, 'self.master'):
            self.master.lift()
        page = None

        # Am creat un obiect cu widget ul Canvas unde i-am setat latimea si lungimea.
        self.canvas = Canvas(master, width=400, height=200)

        # Am creat cate un obiect cu widget-ul Button, iar pentru parametrul "command" am utilizat lambda pentru a
        # apela mai multe instante si functii.
        self.button_check = Button(self.master, text='Raspunsuri', font=('Ink Fre', 12),
                                   command=lambda: [close_both(self.master), CheckInfo.main(dict, old_dict, var, new)])
        self.button_try = Button(self.master, text="Incearca din nou", font=('Ink Fre', 12),
                                 command=lambda: [close_both(self.master), new.destroy(), funct()])
        self.button_close = Button(self.master, text='Inchide', font=('Ink Fre', 12),
                                   command=lambda: [close_both(self.master), new.destroy(), functs()])

        self.button_check.pack()
        self.button_try.pack()
        self.button_close.pack()
        self.image = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python"
                                "\\Python_images\\Choose\\"
                                "wall_background_mauve.jpg")

        # Aceasta linie de cod este folosita cu scopul de a inchide atat fereastra pentru verificarea raspunsurilor,
        # cat si cea care ne afiseaza scorul obtinut, odata ce apasam pe butonul "X" din fereastra cu afisarea
        # raspunsurilor corecte.
        self.master.protocol("WM_DELETE_WINDOW", lambda: [close_wind_reset_score(self.master, dict), new.destroy()])

        # Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
        # BitmapImage si PhotoImage din imaginile din modulul PIL.
        self.image = ImageTk.PhotoImage(self.image)

        # Se adauga imaginea de background, text-ul cu privire la scorul obtinut si butoanele ce ne vor directiona
        # la afisarea raspunsurilor corecte, la obtiunea de reincercare a testului si inchiderea ferestrei.
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
        self.canvas.create_text(65, 50, text="Your score is " + str(var) + "/" + "10", fill='white', anchor=NW,
                                font=('Ink Free', 25, 'bold'))
        self.canvas.create_window(75, 150, window=self.button_check)
        self.canvas.create_window(200,150, window=self.button_try)
        self.canvas.create_window(315, 150, window=self.button_close)

        # Metoda pack() este utilizata pentru a declara pozitia widget-urilor unul in raport cu celalalt, in loc
        # sa fie declarata locatia exacta.
        self.canvas.pack()

        self.master.focus_set()

        # Am folosit urmatoarea functie pentru a permite ferestrei curente sa se afiseze intotdeauna deasupra tuturor
        # ferestrelor deschise, iar unu este considerat "True"
        self.master.wm_attributes("-topmost", 1)

        # Configurarea ferestrei window cu scopul de a nu se putea modifica dimensiunea acesteia.
        self.master.resizable(False, False)

        # "mainloop()" este folosit cu scopul de a rula bucla de evenimente Tkinter.
        self.master.mainloop()

# "if __name__ == '__main__'" codul va fi executat numai daca fisierul a fost rulat direct si nu a fost importat.
if __name__ == '__main__':
    pass
