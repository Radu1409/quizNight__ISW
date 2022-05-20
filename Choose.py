from tkinter import *
from PIL import ImageTk, Image
import Istorie
import Univers
import Geografie
import It
import Fitness
import CheckScore
import CheckInfo

args = 0


class Choose:

    # Functia "__init__" reprezinta constructorul clasei. Aceasta este apelata in momentul in care se creeaza un obiect
    # al clasei.
    # Self reprezintă instanta clasei. Cu "self" putem accesa atributele si metodele clasei.
    # Parametrul master este widget-ul parinte si este un parametru opțional care este trimis noii instante a
    # clasei cand este initializata.
    def __init__(self, master):

        # Widget-ul Frame este utilizat in scopul de a organiza un grup de widget-uri.
        frame = Frame(master)

        # Configuram parametrul "master"
        self.master = master
        self.master.title('Alegere')

        # Aceste linii de cod sunt utilizate cu scopul de a seta iconita imagine pentru fereastra respectiva.
        self.image = PhotoImage(file='New folder/QuizGamePython.png')
        self.master.iconphoto(True, self.image)

        # Am adaugat cate o imagine pentu fiecare tip de intrebare din lista si am redimensionat imaginile.
        # Am folosit si Image.ANTIALIAS pentru a blura marginile pixelilor din imagine.
        # Modulul ImageTk se utilizeaza pentru crearea si modificarea unor obiecte
        # BitmapImage si PhotoImage din imaginile din modulul PIL.
        self.image1 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'wall_background_mauve_light.jpg')
        self.image1 = self.image1.resize((900, 570))

        self.image2 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'simpson_choose.png')
        self.image2 = self.image2.resize((150, 150))

        self.image3 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'Choose_istorie\\wallpaper_istorie3.jpg')
        self.image3 = self.image3.resize((180, 140), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.image3)

        self.image4 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'Choose_Univers\\wallpaper_Univers3.jpg')
        self.image4 = self.image4.resize((180, 140), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(self.image4)

        self.image5 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'Choose_Geografie\\wallpaper_Geografie.jpg')
        self.image5 = self.image5.resize((180, 140), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(self.image5)

        self.image6 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python'
                                 '\\Python_images\\Choose\\'
                                 'Choose_IT\\wallpaper_IT3.jpg')
        self.image6 = self.image6.resize((180, 140), Image.ANTIALIAS)

        self.image6 = ImageTk.PhotoImage(self.image6)

        self.image7 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_Fitness\\wallpaper_fitness2.jpg')
        self.image7 = self.image7.resize((180, 140), Image.ANTIALIAS)
        self.image7 = ImageTk.PhotoImage(self.image7)


        # Am adaugat o imagine PNG si a fost necesara utilizarea functiei "convert('RGBA')
        self.image1.paste(self.image2, (self.image1.size[0] - self.image2.size[0],
                                        self.image1.size[1] - self.image2.size[1]), self.image2.convert('RGBA'))

        self.image1 = ImageTk.PhotoImage(self.image1)

        # Widget ul Canvas este folosit pentru a
        # adauga grafica structurata la aplicatie.
        self.canvas = Canvas(master, width=self.image1.width(), height=self.image1.height())

        # anchor este utilizat in a pozitiona imaginea astfel incat
        # pozitia precizata sa coincida cu NW.
        self.canvas.create_image(0, 0, image=self.image1, anchor=NW)

        # Am adaugat cate un text pentru fiecare imagine pentru a specifica din ce categorie face parte fiecare
        # lista de intrebari.
        self.canvas.create_text(165, 255, text='Istorie', fill='white',anchor=NW, font=('Arial Unicode MS', 16,
                                                                                        'italic bold'))

        self.canvas.create_text(400, 255, text='Univers', fill='white', anchor=NW, font=('Arial Unicode MS', 16,
                                                                                         'italic bold'))

        self.canvas.create_text(630, 255, text='Geografie', fill='white', anchor=NW, font=('Arial Unicode MS', 16,
                                                                                           'italic bold'))
        self.canvas.create_text(300, 475, text='IT', fill='white', anchor=NW, font=('Arial Unicode MS', 16,
                                                                                    'italic bold'))
        self.canvas.create_text(515, 475, text='Fitness', fill='white', anchor=NW, font=('Arial Unicode MS', 16,
                                                                                         'italic bold'))
        self.canvas.create_text(20, 50, text='Alegeti tipul de intrebari:', fill='white', anchor=NW,
                                font=('Ink Free', 25, ' bold'))

        # Metoda pack() este utilizata pentru a declara pozitia widget-urilor unul in raport cu celalalt, in loc
        # sa fie declarata locatia exacta.
        self.canvas.pack()

        # Am creat cate un widget Button unde am inserat imaginile stocate in liniile de cod precedente, pentru care
        # le-am specificat si pozitia acestora in frame. Odata la apasarea butonului, ne va directiona la categoria
        # de intrebari respectiva.
        self.button = Button(self.canvas, image=self.image3, fg='white', borderwidth=0, background='black',
                             activebackground='black',
                             command=lambda: func(1)).place(x=110, y=115)
        self.button = Button(self.canvas, image=self.image4, fg='white', borderwidth=0, background='black',
                             activebackground='black',
                             command=lambda: func(2)).place(x=350, y=115)
        self.button = Button(self.canvas, image=self.image5, fg='white', borderwidth=0, background='black',
                             activebackground='black',
                             command=lambda: func(3)).place(x=590, y=115)
        self.button = Button(self.canvas, image=self.image6, fg='white', borderwidth=0, background='black',
                             activebackground='black',
                             command=lambda: func(4)).place(x=230, y=335)
        self.button = Button(self.canvas, image=self.image7, fg='white', borderwidth=0, background='black',
                             activebackground='black',
                             command=lambda: func(5)).place(x=460, y=335)

        # Metoda pack() este utilizata pentru a declara pozitia widget-urilor unul in raport cu celalalt, in loc
        # sa fie declarata locatia exacta.
        frame.pack()


# Functia de mai jos imi va creea fereastra cu atributele specificate in clasa "Choose" si nu va permite redimensionarea
# ferestrei.
def main():
    root = Tk()
    b = Choose(root)
    root.resizable(False, False)
    root.mainloop()


# Aceasta functie este utilizata pentru a specifica un argument pentru fereastra pe care dorim sa o inchidem.
def exitChoose(root):
    root.destroy()


# Aceasta functie este utilizata pentru a minimiza fereastra Choose.
def minimizeChoose():
    global root
    root.update()
    root.deiconify()


# Se verifica ce categorie de intrebari s-a ales prin valoarea variabilei "args".
# Se initializeaza din modulul "CheckScore" variabila "argument" cu valoarea din variabila "args"
# Se initializeaza din modulul "CheckInfo" variabila "argument2" cu valoarea din variabila "args"
# In functie de valoarea variabilei "args" se va deschide o fereastra cu lista de intrebari din categoria respectiva.
def func(args):
    if args == 1:
        print(args)
        CheckScore.argument = args
        CheckInfo.argument2 = args
        Istorie.main()

    if args == 2:
        print(args)
        CheckScore.argument = args
        CheckInfo.argument2 = args
        Univers.main()

    if args == 3:
        print(args)
        CheckScore.argument = args
        CheckInfo.argument2 = args
        Geografie.main()

    if args == 4:
        print(args)
        CheckScore.argument = args
        CheckInfo.argument2 = args
        It.main()

    if args == 5:
        print(args)
        CheckScore.argument = args
        CheckInfo.argument2 = args
        Fitness.main()

    print(args)

    # Se returneaza valoarea variabilei "args"
    return args

# "if __name__ == '__main__'" codul va fi executat numai daca fisierul a fost rulat direct si nu a fost importat.
if __name__ == '__main__':
    main()
