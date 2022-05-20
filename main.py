from tkinter import *
from tkinter import messagebox
from Choose import main
from PIL import Image, ImageTk
import tkinter
import IdPass

# Am initializat variabile pentru a putea face verificari pentru cazul in care doresc sa verific numarul de inregistrari
# , sa verific situatii precum un caz in care username-ul este introdus gresit si parola este corecta, sa-mi afiseze
# sub label mesajul de eroare (Username gresit) sau in cazul in care parola este introdusa gresit si username-ul este
# coresc, sa-mi afiseze sub label doar mesajul de eroare (Parola gresita!), sau ambele mesaje de eroare in cazul in care
# si username-ul si parola sunt introduse gresit!

count = -1
counts = -1
num1 = 0
num2 = 0
num_1 = 0
num_2 = 0
countLogin = 0
user = ''
passw = ''
user_check = ''
pass_check = ''
user_change = None
pass_change = None

numLoginCount = 0


def exitMenuBar():
    window.destroy() # Functie utilizata in scopul de a elimina fereastra.


def exitWin():
    window.destroy() # Functie utilizata in scopul de a elimina fereastra.


def switch():
    if button1["state"] == NORMAL:
        button1["state"] = DISABLED
    else:
        button1["state"] = NORMAL


def toLogin():

    # odata ce functia "toLogin()" va fi apelata, va creea aceste variabile ca fiind globale (vor putea fi accesate
    # si de alte functii)
    global countLogin
    global user
    global passw
    global button1
    global numLoginCount

    # de fiecare data cand va fi apelata aceasta functie, variabila va fi incrementata cu 1, pentru a
    # identifica numarul de incercari pentru care s-a incercat conectarea. De asemenea, va fi utilizata
    # pentru a seta valoarea la 0 in cazul in care casuta "Tine-ma minte"  a fost debifata.
    countLogin += 1

    # Functia TopLever() permite aducerea ferestrei deasupra tuturor ferestrelor.
    screen1 = Toplevel(window)

    # Setarea titlului ferestrei pentru fereastra
    screen1.title("Autentificare")

    # Functia "open()" din libraria "Image" are ca scop identificarea fisierului.
    # Continutul este stocat in variabila "image1"
    image1 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\'
                        'Python_images\\Login\\Login1.jpg')

    # Functia "rotate()" este utilizata pentru a intoarce imaginea cu 180 de grade.
    image1 = image1.rotate(180)

    # modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
    # BitmapImage si PhotoImage din imaginile din modulul PIL.
    image1 = ImageTk.PhotoImage(image1)

    # Widget ul Canvas este folosit pentru a
    # adauga grafica structurata la aplicatie.
    canvas = Canvas(screen1, width=image1.width(), height=image1.height())

    # anchor este utilizat in a pozitiona imaginea astfel incat
    # pozitia precizata sa coincida cu NW.
    canvas.create_image(0, 0, image=image1, anchor=NW)

    # cu ajutorul functiei "create_text()", dupa cum se pot vedea parametrii utilizati, am setat pozitia (primii 2
    #  parametrii) pentru care vreau sa se afiseze valoarea din parametrul "text", urmat de parametru "anchor" ce este
    # folosit pentru a defini unde sa fie pozitionat textul in raport cu punctul de referinta ales (din primii 2
    # parametrii) ("NW" reprezinta "North West"), dupa care pentru parametrul "font" setez stilul de font pentru textul
    # ales si dimensiunea acestuia.
    canvas.create_text(180, 200, text='Logare', anchor=NW, font=('Arial Unicode MS', 22))
    canvas.create_text(80, 260, text='Nume de utilizator', anchor=NW, font=('PMingLiU-ExtB', 12, 'bold'))
    canvas.create_text(80, 340, text='Parola', anchor=NW, font=('PMingLiU-ExtB', 12, 'bold'))

    if countLogin == 1:

        # declararea variabilelor de tip String pentru a evita Warning-urile. De asemenea, reinitializarea variabilelor
        # in cazul in care se incearca pentru a doua oara conectarea.
        entrySet_user = StringVar()
        entrySet_pass = StringVar()
    else:
        # declararea variabilelor globale si variabilelor
        global entryUser
        global entryPass
        global user
        global passw

        entrySet_user = StringVar()
        entrySet_pass = StringVar()

        entry_user = StringVar()
        entry_pass = StringVar()

        entrySet_user.set(user)
        entrySet_pass.set(passw)

    def checkboxActiveDeactive():

        # Am declarat variabilele globale pentru a face referire la alte variabile deja declarate in liniile de cod.
        global entry_user
        global entry_pass
        global countLogin

        # Am folosit functia "get()" pentru a returna valoarea variabilei "x" (pe care am declarat-o in liniile de
        # cod de mai jos pentru cazul in care casuta este bifata sau nu. Cand este bifata, se initializeaza valoarea
        # cu 1, iar in cazul in care este debifata, se returneazza valoarea 0.
        if x.get() == 1:
            entry_user = user
            entry_pass = passw
            print('Bifat')

        else:
            entry_user = ''
            entry_pass = ''
            print('Nebifat')
            countLogin = 0

    # Functie utilizata pentru a manipula conditiile in care se va inchide fereastra curenta.
    def close_window():

        # Am declarat variabilele globale pentru a face referire la alte variabile deja declarate in liniile de cod.
        global user
        global passw

        # Se va identifica daca casuta este bifata sau debifata.
        checkboxActiveDeactive()

        # Se returneaza valoarea variabilelor entryUser si entryPass si se memoreaza in variabilele user si passw.
        try:
            user = entryUser.get()
            passw = entryPass.get()
        except:
            pass

        # Functia .destroy()" este folosita pentru a inchide fereastra curenta.
        screen1.destroy()

        # Se reconfigureaza statusul butonului "Play" la "normal" pentru a putea
        # fi din nou utilizat.
        button1.config(state="normal")
        print("Window closed")


    # Functia "Entry()" este utilizata pentru a manipula continutul din casetele de text. Am setat parametrul "width"
    # pentru latimea continutului si pentru variabila "entryPass" am setat parametrul "show" pentru a specifica cum
    # doresc sa se afiseze continutul din caseta de text respectiva.
    entryUser = Entry(screen1, width=25, textvariable=entrySet_user)
    entryPass = Entry(screen1, show='*', width=25, textvariable=entrySet_pass)

    # Functiile "pack()" se apeleaza mereu pentru widget-urile (spre exemplu: "Entry") pentru organizarea acestora
    # inaintea de a fi adaugate in widget-ul parinte.
    entryUser.pack()
    entryPass.pack()

    # Se reconfigureaza variabilele "entryUser" si "entryPass" cu functia "config()", modificandu-se fonturile.
    entryUser.config(font=('Calibri', 13, 'italic'))
    entryPass.config(font=('Calibri', 13, 'italic'))

    # Se creeaza o subfereastra pentru fereastra curenta.
    canvas.create_window(194, 383, window=entryPass)
    canvas.create_window(194, 303, window=entryUser)

    # Aceasta functie este utilizata in scopul de a focaliza un anume widget doar in cazul in care fereastra principala
    # este focalizata.
    entryUser.focus()

    # Setarea imaginii de background pentru fereastra curenta.
    # Setarea dimensiuniilor pentru imaginea de background.
    # modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
    # BitmapImage si PhotoImage din imaginile din modulul PIL.
    image2 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                        '\\Python_images\\submit_ButtonNew.png')
    image2 = image2.resize((300, 220), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    # Declararea variabilei "x" de tip IntVar().
    x = IntVar()

    # Crearea casutei de text. Am folosit variabila "ckeckbox" ca si referinta la obiect pentru widget-ul
    # Checkbutton in scopul de a aduce configurarii ale obiectului.
    checkbox = Checkbutton(screen1, text='Tine-ma minte', variable=x, onvalue=1, offvalue=0,
                           command=checkboxActiveDeactive)

    # Aceasta functie este utilizata in scopul de a focaliza un anume widget doar in cazul in care fereastra principala
    # este focalizata.
    checkbox.pack()

    # Configurarea variabilei ce este folosita ca si referinta la obiect pentru widget-ul Checkbutton.
    checkbox.config(font=('Ink Fre', 10), bg='#dadbdf', activebackground='#dadbdf')

    # Pozitionarea variabilei "checkbox" in fereaastra.
    canvas.create_window(136, 430, window=checkbox)

    # Crearea casutei de text. Am folosit variabila "submit" ca si referinta la obiect pentru widget-ul
    # Button in scopul de a aduce configurarii ale obiectului.
    submit = Button(screen1, image=image2, width=206, height=45, borderwidth=0, bg='#dadbdf',
                    activebackground='#dadbdf', command=lambda: submitFun())

    # Aceasta functie este utilizata in scopul de a focaliza un anume widget doar in cazul in care fereastra principala
    # este focalizata.
    submit.pack()

    def submitFun():

      while True:
        # Se returneaza valorile in alte variabile.
        username = entryUser.get()
        password = entryPass.get()

        # declararea variabilelor globale si variabilelor.
        global count
        global counts
        global user_change
        global pass_change
        global num1
        global num2
        global user
        global passw
        global user_check
        global pass_check

        # Variabile utilizate in scopul de a afisa/scoate mesajul de eroare din fereastra de logare.
        count += 1
        counts += 1

        # In cazul in care incercam logarea pentru prima oara cu variabilele "count" si "counts" setate la 0, atunci
        # se va executa direct urmatoarele secvente de cod din instructiunea "if"
        if username == IdPass.check_user(username) and count == 0 and password == IdPass.check_pass(password) and counts == 0:
            print('FELICITARI, TE AI LOGAT DIN PRIMA! #1')

            # Se va afisa intr-o minifereastra mesajul cu privire la faptul ca logarea a fost realizata cu succes.
            tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')

            # Daca checkbox a fost setat, continuturile din casutele de text vor fi stocate in variabilele "user"
            # si passw.
            if x.get() == 1:
                user = entryUser.get()
                passw = entryPass.get()

            # Dupa inchiderea miniferestrei cu mesajul respectiv, se va inchide si fereastra de logare.
            screen1.destroy()
            window.destroy()

            # Avand in vedere ca logarea s-a realizat cu succes, se vor decrementa cele doua variabile.
            count = -1
            counts = -1

            # Se va deschide o noua fereastra unde ne vom putea selecta tipul de intrebari (Istorie, Geografie, Fitness,
            # It, Univers)
            main()

            # Se va intrerupe bucla "while True"
            break

        # Daca incercarea de logare nu s-a realizat cu succes din prima.
        elif username == IdPass.check_user(username) and password == IdPass.check_pass(password):

            # Se reinitializeaza mesajul de eroare cu String-ul '' pentru a nu mai fi afisat.
            user_change = canvas.itemconfig(user_change, text='', fill='red', anchor=NW,
                                            font=('Arial Unicode MS', 8))
            pass_change = canvas.itemconfig(pass_change, text='', fill='red', anchor=NW,
                                            font=('Arial Unicode MS', 8))
            print('FELICITARI, TE AI LOGAT DIN PRIMA! #1')
            tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')

            # Daca checkbox a fost setat, continuturile din casutele de text vor fi stocate in variabilele "user"
            # si passw.
            if x.get() == 1:
                user = entryUser.get()
                passw = entryPass.get()

            # Dupa inchiderea miniferestrei cu mesajul respectiv, se va inchide si fereastra de logare.
            screen1.destroy()
            window.destroy()

            # Avand in vedere ca logarea s-a realizat cu succes, se vor decrementa cele doua variabile.
            count = -1
            counts = -1

            # Se va deschide o noua fereastra unde ne vom putea selecta tipul de intrebari (Istorie, Geografie, Fitness,
            # It, Univers)
            main()

            # Se va intrerupe bucla "while True"
            break

        # Conditie pentru cazul in care parola introduse este gresita.
        elif username == IdPass.check_user(username) and count == 0 and password != IdPass.check_pass(password) and counts == 0:

            # Se reinitializeaza mesajul de eroare.
            pass_change = canvas.create_text(90, 395, text='Parola gresita!', fill='red', anchor=NW,
                                             font=('Arial Unicode MS', 8))

            # Se va intrerupe bucla "while True"
            break
        # Conditie pentru cazul in care parola introduse este gresita.
        elif username != IdPass.check_user(username) and count == 0 and password == IdPass.check_pass(password) and counts == 0:

            # Se reinitializeaza mesajul de eroare.
            user_change = canvas.create_text(90, 316, text='Username gresit!', fill='red', anchor=NW,
                                             font=('Arial Unicode MS', 8))

            # Se va intrerupe bucla "while True"
            break
        else:

            # Conditie pentru cazul in care numele de utilizator introdus este gresit si se incearca logarea pentru
            # prima oara.
            if username != IdPass.check_user(username) and count == 0:

                # Se reinitializeaza mesajul de eroare.
                user_change = canvas.create_text(90, 316, text='Username gresit!', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))

            # Se intializeaza variabila "num1" cu valoarea 0.
            if username != IdPass.check_user(username):
                num1 = 0

            # Conditie pentru cazul in care parola introdusa este gresita si se incearca logarea pentru
            # prima oara.
            if password != IdPass.check_pass(password) and counts == 0:

                # Se reinitializeaza mesajul de eroare.
                pass_change = canvas.create_text(90, 395, text='Parola gresita!', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))

            # Se intializeaza variabila "num1" cu valoarea 0.
            if password != IdPass.check_pass(password):
                num2 = 0

            # Am folosit blocurile "try" si "except" pentru a gestiona erorile ce pot aparea.
            try:
                # Verificare conditie daca numele de utilizator corespunde cu numele de utilizator din lista.
                if username == IdPass.check_user(username):

                        # Se reinitializeaza mesajul de eroare cu String-ul '' pentru a nu mai afisa mesajul
                        # de eroare.
                        user_change = canvas.itemconfig(user_change, text='', fill='red', anchor=NW,
                                                        font=('Arial Unicode MS', 8))

                        # Se seteaza valorile "num1" si "count".
                        num1 = 1
                        count = -1

            # Daca avem o eroare, se vor executa urmatoarele linii de cod din "except"
            except:

                # Se reinitializeaza variabila "num1" si mesajul de eroare cu String-ul '' pentru a nu mai afisa
                # mesajul de eroare.
                num1 = 0
                user_change = canvas.create_text(90, 316, text='', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))

            # Am folosit blocurile "try" si "except" pentru a gestiona erorile ce pot aparea.
            try:

                # Verificare conditie daca parola corespunde cu parola din lista.
                if password == IdPass.check_pass(password):

                        # Se reinitializeaza mesajul de eroare cu String-ul '' pentru a nu mai afisa mesajul
                        # de eroare.
                        pass_change = canvas.itemconfig(pass_change, text='', fill='red', anchor=NW,
                                                        font=('Arial Unicode MS', 8))

                        # Se seteaza valorile "num2" si "count".
                        num2 = 1
                        counts = -1

            # Daca avem o eroare, se vor executa urmatoarele linii de cod din "except"
            except:

                # Se reinitializeaza variabila "num2" si mesajul de eroare cu String-ul '' pentru a nu mai afisa
                # mesajul de eroare.
                num2 = 0
                pass_change = canvas.create_text(90, 395, text='', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))

            # Daca num1 si num2 au valorile 1, se vor executa codurile din bucla "if".
            if num1 == 1 and num2 == 1:
                print(print('FELICITARI, TE AI LOGAT DIN PRIMA! #2'))

                # Se va deschide o minifereastra cu mesajul de informare "Te-ai logat cu succes!".
                tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')

                # Daca "checkbox" va fi bifat, atunci se vor memora continuturile din casutele de intrare.
                if x.get() == 1:
                    user = entryUser.get()
                    passw = entryPass.get()
                    user_check = user
                    pass_check = passw

                # Se va inchide fereastra ce are variabila "screen1" ca si referinta la obiect. Se reinitializeaza
                # variabilele "num1" si "num2" si se apeleaza functia "main()" ce ne va deschide o fereastra cu
                # tipurile de intrebari.
                screen1.destroy()
                num1 = 0
                num2 = 0
                main()

            # Se va intrerupe bucla "while True" daca utilizam break.
            break

    # Adaugam variabila "submit" si o pozitionam in widget-ul canvas din fereastra.
    canvas.create_window(220, 480, window=submit)

    # Aceasta functie este utilizata in scopul de a focaliza un anume widget doar in cazul in care fereastra principala
    # este focalizata.
    canvas.pack()

    # Aceasta functie este utilizata in scopul de a focaliza un anume widget doar in cazul in care fereastra principala
    # este focalizata.
    label.pack()

    # Se reconfigureaza statusul butonului "Play" ca fiind "disabled/dezactivat"
    # pentru a nu mai putea fi apasat butonul "Play".
    button1.config(state="disabled")

    # Se inchide fereastra "screen1".
    screen1.protocol("WM_DELETE_WINDOW", close_window)

    # Functia "resizable()" are parametrii setati "False, False" pentru a nu putea
    # fi modificata inaltimea si latimea ferestrei.
    screen1.resizable(False, False)

    # Functia mainloop() pentru a afisa fereastra. Aceasta va permite sa ruleze in
    # continuu (pana la oprirea programului) si asteapta evenimentele de la
    # utilizator.
    screen1.mainloop()

# Functie ce are scopul de a afisa fereastra principala si de a manipula toate componentele aplicatiei
# tkinter.
window = Tk()

# Widget ul PhotoImage are rolul de a afisa o imagine pentru
# un buton sau eticheta.
image = PhotoImage(file='New folder/QuizGamePython.png')

# Functie pentru aplicatia tkinter pentru a adauga o imagine pentru iconita.
window.iconphoto(True, image)

# Definirea unui nume al aplicatiei.
window.title('Quiz Game')

# Setarea imaginii de background pentru fereastra curenta.
image = Image.open('New folder/quizNight.jpeg')

# Setarea dimensiuniilor pentru imaginea de background.
image = image.resize((600, 550))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
image = ImageTk.PhotoImage(image)

# Inserarea imaginii in fereastra aplicatiei in widget-ul "Label"
label = Label(window, image=image)

# Metoda pack() este utilizata pentru a declara pozitia widget-urilor unul in raport cu celalalt, in loc
# sa fie declarata locatia exacta.
label.pack()

# Widget ul "Button" este utilizat in scopul de a adauga mai multe butoane intr-o
# fereastra. Scopul acestuia este de a deschide o noua fereastra pentru logare.
button1 = Button(window, text='Joaca')

# Configurarea obiectului "button1" pentru definirea latimii.
button1.config(width=13)

# Configurarea obiectului "button1" pentru
# setarea fontului, dimensiunii si comanda ce urmeaza
# a fi executata in momentul apasarii acestuia.
button1.config(font=("Helvetica", 10, 'bold'), command=toLogin)

# Specificarea pozitiei butonului in fereastra aplicatiei.
button1.place(x=245, y=450)

# Widget ul Button este utilizat in scopul de a adauga mai multe butoane intr-o
# fereastra. Scopul acestuia este de a inchide fereastra si oprirea aplicatie.
button = Button(window, text='Iesire')

# Configurarea obiectului "button1" pentru definirea latimii.
button.config(width = 13)

# Configurarea obiectului "button1" pentru
# setarea fontului, dimensiunii si comanda ce urmeaza
# a fi executata in momentul apasarii acestuia.
button.config(font=("Helvetica", 10, 'bold'), command=exitWin)

# Specificarea pozitiei butonului in fereastra aplicatiei.
button.place(x=245, y=485)

# Adaugarea imagini in variabila "openImage" cu ajutorul modulului "Image".
openImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                       '\\Python_images\\icon_FileMenu\\open.png')

# Definirea dimensiunii imaginii.
openImage = openImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
openImage = ImageTk.PhotoImage(openImage)

# Adaugarea imagini in variabila "saveImage" cu ajutorul modulului "Image".
saveImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                       '\\Python_images\\icon_FileMenu\\savee.png')

# Definirea dimensiunii imagini
saveImage = saveImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
saveImage = ImageTk.PhotoImage(saveImage)

# Adaugarea imagini in variabila "exitImage" cu ajutorul modulului "Image".
exitImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                       '\\Python_images\\icon_FileMenu\\exiit.png')

# Definirea dimensiunii imagini
exitImage = exitImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
exitImage = ImageTk.PhotoImage(exitImage)

# Adaugarea imagini in variabila "cutImage" cu ajutorul modulului "Image".
cutImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                      '\\Python_images\\icon_FileMenu\\cutt.png')

# Definirea dimensiunii imagini.
cutImage = cutImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
cutImage = ImageTk.PhotoImage(cutImage)

# Adaugarea imagini in variabila "copyImage" cu ajutorul modulului "Image".
copyImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                       '\\Python_images\\icon_FileMenu\\copy.png')

# Definirea dimensiunii imagini
copyImage = copyImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
copyImage = ImageTk.PhotoImage(copyImage)

# Adaugarea imagini in variabila "pasteImage" cu ajutorul modulului "Image".
pasteImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                        '\\Python_images\\icon_FileMenu\\pastee.png')

# Definirea dimensiunii imagini
pasteImage = pasteImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
pasteImage = ImageTk.PhotoImage(pasteImage)

# Adaugarea imagini in variabila "scoreImage" cu ajutorul modulului "Image".
scoreImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                        '\\Python_images\\icon_FileMenu\\score.png')

# Definirea dimensiunii imagini
scoreImage = scoreImage.resize((20, 20))

# Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
# BitmapImage si PhotoImage din imaginile din modulul PIL.
scoreImage = ImageTk.PhotoImage(scoreImage)

# Widget ul "Meniu" este folosit in a tipuri de meniuri diferite
menubar = Menu(window)

# Utilizarea functiei "config()" pentru a seta meniul ales
window.config(menu=menubar)

# Setarea font-ului.
fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))

# Functia "add_cascade()" este folosita cu scopul de a permite
# Inserarea mai multor submeniuri.
menubar.add_cascade(label="Fisier", menu = fileMenu)

# Functia "add_command()" este folosita cu
# cu scopul de a adauga mai multe.
fileMenu.add_command(label=' Deschide', image=openImage, compound='left')
fileMenu.add_command(label=" Salveaza", image=saveImage, compound='left')

# Functie pentru aducerea unui separator intre submeniuri.
fileMenu.add_separator()

# Functia "add_command()" este folosita cu
# cu scopul de a adauga mai multe.
fileMenu.add_command(label=' Iesire', image=exitImage, compound='left', command=exitMenuBar)

# Widget ul "Meniu" este folosit in a tipuri de meniuri diferite
editMenu = Menu(menubar, tearoff=False, font=('MV Boli', 15))

# Functia "add_cascade()" este folosita cu scopul de a permite
# Inserarea mai multor submeniuri.
menubar.add_cascade(label='Editeaza', menu=editMenu)

# Functia "add_command()" este folosita cu
# cu scopul de a adauga mai multe.
editMenu.add_command(label=' Taie', image=cutImage, compound='left')
editMenu.add_command(label=' Copiaza', image=copyImage, compound='left')
editMenu.add_command(label=' Insereaza', image=pasteImage, compound='left')

# Widget ul "Meniu" este folosit in a tipuri de meniuri diferite
readMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))

# Functia "add_cascade()" este folosita cu scopul de a permite
# Inserarea mai multor submeniuri.
menubar.add_cascade(label='Citeste', menu=readMenu)

# Functia "add_command()" este folosita cu
# cu scopul de a adauga mai multe.
readMenu.add_command(label=" Scor", image=scoreImage, compound='left')

# Configurarea ferestrei window cu scopul de a nu se putea modifica dimensiunea acesteia.
window.resizable(False, False)

# "mainloop()" este folosit cu scopul de a rula bucla de evenimente Tkinter.
window.mainloop()








