import tkinter as tk
from tkinter import *
from PIL import ImageTk, ImageFilter
from PIL import Image, ImageOps
from cairosvg import svg2png
from io import BytesIO
import CheckScore


def frame(im, thickness=5):
    # Obtinem latimea si inaltimea imaginii de intrare si calculati latimea si inaltimea de iesire.
    iw, ih = im.size
    ow, oh = iw+2*thickness, ih+2*thickness

    # Marginile rotunjite din imagine vor fi desenate cu negru si vor fi salvate in memorie ca png.
    outer = f'<svg width="{ow}" height="{oh}" style="background-color:none"><rect rx="20" ry="20" width="{ow}" ' \
            f'height="{oh}" fill="black"/></svg>'
    png = svg2png(bytestring=outer)
    outer = Image.open(BytesIO(png))


    inner = f'<svg width="{ow}" height="{oh}"><rect x="{thickness}" y="{thickness}" rx="20" ry="20" width="{iw}" ' \
            f'height="{ih}" fill="white"/></svg>'
    png = svg2png(bytestring=inner)
    inner = Image.open(BytesIO(png)).convert('L')

    # Extindem canvas-ul original cu negru pentru a se potrivi cu dimensiunea din output (de iesire).
    expanded = ImageOps.expand(im, border=thickness, fill=(0, 0, 0)).convert('RGB')

    # Se lipeste imaginea extinsa pe marginea neagra exterioara folosind dreptunghiul interior alb ca masca.
    outer.paste(expanded, None, inner)
    return outer


LARGE = ('Verdana', 10)
incr_all = 0
y = 0

# Vom creea o clasa TkinterApp ce va mosteni tkinter (tk.TopLevel)
class TkinterApp(tk.Toplevel):

    # *args si **kwargs ne permite sa trecem un numar variabil de argumente in functie.
    # Argumentele *args nu au cuvinte cheie
    # Argumentele *args au asociate cuvinte cheie (se pot utiliza dictionare).
    # De obicei, cand lucram cu functii Python trebuie sa precizam direct argumentele pe care le va accepta functia.

    def __init__(self, *args, **kwargs):
        # In constructor initializam de asemenea si din tkinter widget-ul TopLevel (utilizat cand o aplicatie Python
        # vrea sa reprezinte informatii suplimentare sau grupuri de widget-uri in noua fereastra.
        tk.Toplevel.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand= True)

        # Am declarat o lista care-mi va memora mai multe frame-uri unde voi adauga pentru fiecare frame cate o
        # intrebare si variantele de raspuns.
        self.frames = {}

        # Urmatoarele linii de cod au fost initial introduse cu scopul de a ne putea redirectiona la fiecare pagina
        # pentru fiecare intrebare, apasand anumite taste (de exemplu: 1,2,3,4.. 10). Am dezactivat aceasta varianta
        # deoarece am realizat ca daca schimbam catre alte frame-uri si selectam repede alta varianta de raspuns se
        # poate ca trecerea de la o pagina la alta din lista de dictionare sa nu fie suficient de rapida, iar astfel,
        # noua varianta de raspuns poate fi modificata pentru pagina precedenta.
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive,
                  PageSix, PageSeven, PageEight, PageNine, PageTen):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Fereastra odata deschisa va afisa prima clasa "StartPage" ce mosteneste din tkinter widget-ul Frame.
        self.show_frame(StartPage)

    # Aceasta functie este utilizata pentru a schimba frame-urile intre ele (intrebarile din fereastra curenta), cu
    # scopul de a oferi oportunitatea utilizatorului sa se intoarca la o anumita intrebare.
    # Pentru parametru "cont" se memoreaza frame-ul (intrebarea) la care dorim sa ajungem, din lista de frames se
    # memoreaza frame-ul respectiv in variabila "frame", iar in cele din urma utilizam functia "tkraise()" pentru
    # a pune frame-ul "in top", adica se va afisa peste toate celelalte frame-uri.
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Pentru clasa respectiva mostenim toate atributele din tkinter (tk) din widget-ul Frame. clasa va fi acum recunoscuta
# ca fiind de tip Frame.
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.image1 = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_univers\\wallpaper_univers.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(0))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50,50))
        self.arrowRight_image = self.arrowRight_image.resize((50,50))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())

        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)

        self.canvas.create_text(70, 270,
                                text='Universul este deseori definit ca "totalitatea existenței", sau tot ceea ce '
                                     'există, tot ce a existat și tot ceea ce va exista.\n'
                                     'Este totalitatea spațiului și timpului, a '
                                     'tuturor formelor de materie și energie.'
                                     ' În timp ce dimensiunea întregului Univers\n'
                                     'nu este cunoscută, universul observabil poate fi măsurat.'
                                     'Acum ca am facut o scurta introducere, ne vom dezvolta cul-\n'
                                     '                                                         '
                                     '  tura generala pe acest subiect',
                                anchor=NW, font=('Arial Unicode MS', 15), fill='white')

        self.button = Button(self.canvas, text='Continua')
        self.button.config(font=('Ink Fre', 12), bg='#dadbdf', activebackground='#dadbdf',
                           command=lambda: [controller.show_frame(PageOne), reset()])
        self.button.pack()

        self.button1 = Button(self.canvas, text='Intoarce-te')
        self.button1.config(font=('Ink Fre', 12), bg='#dadbdf', activebackground='#dadbdf',
                            command=lambda: [close_app(controller), reset()])
        self.button1.pack()

        self.canvas.create_window(520, 450, window=self.button)
        self.canvas.create_window(660, 450, window=self.button1)

        self.canvas.pack()

        controller.resizable(False, False)
        controller.minsize(self.gaussImage.width(), self.gaussImage.height())


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.title('Univers Quiz')
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(0))
        self.gaussImage = self.gaussImage.resize((1200, 700))
        self.grasSat = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\"
                                  "Python_images\\Choose\\quiz_univers\\wallpaper_univers.jpg")
        self.grasSat = self.grasSat.resize((500,350))

        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        ##################
        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                                                      self.arrowRight_image.convert('RGBA'))

        self.grasSat_brd = ImageOps.expand(self.grasSat, border=2, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (600, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='                        Ce se afla in imaginea de mai jos?',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='O stea', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='Ochiul Stelei Spatiale', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(100, 470, text='Galaxie', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        x = IntVar()
        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button2,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "C")])
        self.button3.pack()
        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)

        self.canvas.grid_configure(sticky="nsew")
        self.canvas.pack()
        controller.minsize(self.gaussImage.width(), self.gaussImage.height())

        def str_to_class(str):
            return getattr(sys.modules[__name__], str)

        def on_key_release(event):
            key_mapping = {'1': "PageOne", '2': "PageTwo", '3': "PageThree", '4': "PageFour",
                           '5': "PageFive", '6': "PageSix", '7': "PageSeven", '8': "PageEight", '9': "PageNine",
                           '0': "PageTen"}
            key_released = event.keysym
            if key_released in key_mapping:
                controller.show_frame(str_to_class(key_mapping[key_released]))

#           controller.bind('<KeyRelease>', on_key_release)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))

        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                                                     self.arrowLeft_image.convert('RGBA'))

        self.grasSat = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_univers\\quiz_univers2.jpg")
        self.grasSat = self.grasSat.resize((550, 350))
        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='Protubenantele solare se produc in:', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Fotosfera', fill='white',
                                anchor=NW, font=('Arial Unicode MS',15))#rasp corect
        self.canvas.create_text(100, 420, text='Coroana Solar', fill='white',
                                anchor=NW, font=('Arial Unicode MS',15))
        self.canvas.create_text(100, 470, text='Cromosfera', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button2,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))

        self.img = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                              "quiz_univers\\quiz_univers3.jpg")
        self.img = self.img.resize((500,300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='             Planetele de tip terestru se caracterizeaza prin:',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Densitate mica', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 420, text='Numar mare de sateliti', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 470, text='Densitate mare', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))#rasp corect
        self.canvas.create_text(180, 520, text='Viteza mare de rotatie', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageFour, PageThree),
                                               increment_all(PageThree, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageFour, PageThree),
                                               increment_all(PageThree, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageFour, PageThree),
                                               increment_all(PageThree, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageFour, PageThree),
                                               increment_all(PageThree, "D")])
        self.button4.pack()

        self.canvas.create_window(150, 385, window=self.button1)
        self.canvas.create_window(150, 435, window=self.button2)
        self.canvas.create_window(150, 485, window=self.button3)
        self.canvas.create_window(150, 535, window=self.button4)

        self.canvas.pack()


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))
        self.img = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                              'quiz_univers\\wallpaper_univers2.jpg')
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='        Universul este format din:', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Materie organizata', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 420, text='Materie organizata si neorganizata', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(180, 470, text='Materie neorganizata', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageFive, PageFour),
                                               increment_all(PageFour, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageFive, PageFour),
                                               increment_all(PageFour, "B")])
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button2, self.button1, self.button1,
                                                         controller, PageFive, PageFour),
                                               increment_all(PageFour, "C")])
        self.button3.pack()

        self.canvas.create_window(150, 385, window=self.button1)
        self.canvas.create_window(150, 435, window=self.button2)
        self.canvas.create_window(150, 485, window=self.button3)

        self.canvas.pack()


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))
        self.img = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                              'quiz_univers\\quiz_univers4.jpg')
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='                                                      '
                                              'Cate galaxii exista in Univers?',fill='white',  anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='150 miliarde de galaxii', fill='white', anchor=NW,
                                font=('Arial Unicode MS',15)) #rasp corect
        self.canvas.create_text(180, 420, text='50 galaxii', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 470, text='140 mii de galaxii', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 520, text='1 miliard de galaxii', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageSix, PageFive),
                                               increment_all(PageFive, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageSix, PageFive),
                                               increment_all(PageFive, "B")])
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageSix, PageFive),
                                               increment_all(PageFive, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageSix, PageFive),
                                               increment_all(PageFive, "D")])
        self.button4.pack()
        self.canvas.create_window(150, 385, window=self.button1)
        self.canvas.create_window(150, 435, window=self.button2)
        self.canvas.create_window(150, 485, window=self.button3)
        self.canvas.create_window(150, 535, window=self.button4)
        self.canvas.pack()


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.img = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                              'quiz\\quiz_fitness7.jpg')
        self.img = self.img.resize((500, 300))
        self.img_brd = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))

        # self.gaussImage.paste(self.img_brd, (630, 160))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(120, 170,
                                text='                                                       '
                                     'Cum se numeste galaxia noastra?'
                                ,
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='Big-Bang', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='Terra', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='Universul', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 420, text='Calea Lactee', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))# rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.img = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                              'quiz\\quiz_fitness7.jpg')
        self.img = self.img.resize((500, 300))
        self.img_brd = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(120, 170,
                                text='                                              '
                                     'Care este cea mai apropiata stea de Terra?'
                                ,
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='Pluto', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='Marte', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='Soarele', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))#rasp corect
        self.canvas.create_text(780, 420, text='Luna', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageEight, PageSeven),
                                               increment_all(PageSeven, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageEight, PageSeven),
                                               increment_all(PageSeven, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageEight, PageSeven),
                                               increment_all(PageSeven, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageEight, PageSeven),
                                               increment_all(PageSeven, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))

        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                                                     self.arrowLeft_image.convert('RGBA'))

        self.grasSat = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_univers\\quiz_univers5.jpg")
        self.grasSat = self.grasSat.resize((550, 350))
        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='Cat timp dureaza ca razele soarelui sa ajunga pe pamant?', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='8 minute', fill='white', anchor=NW, font=('Arial Unicode MS', 15))#rasp corect
        self.canvas.create_text(100, 420, text='10 minute', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 470, text='12 minute', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button2,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))
        self.img = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                              "quiz_univers\\quiz_univers6.jpg")
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='Când apare o eclipsă de Lună?', fill='white',  anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Cand Pamantul este intre Soare si Luna', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(180, 420, text='Cand Luna este intre Pamant si Soare', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 470, text='Cand Pamantul acopera Luna', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageTen, PageNine),
                                               increment_all(PageNine, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageTen, PageNine),
                                               increment_all(PageNine, "B")])
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageTen, PageNine),
                                               increment_all(PageNine, "C")])
        self.button3.pack()

        self.canvas.create_window(150, 385, window=self.button1)
        self.canvas.create_window(150, 435, window=self.button2)
        self.canvas.create_window(150, 485, window=self.button3)

        self.canvas.pack()


class PageTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_univers\\wallpaper_univers7.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.controller = controller
        self.controller.protocol("WM_DELETE_WINDOW", lambda: [reset_answer_user(), self.controller.destroy()])
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))

        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(300, 200, text='In Fotosfera se inregistreaza cele mai mari temperaturi',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16, 'bold'))
        self.canvas.create_text(380, 370, text='Adevarat', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='Fals', fill='white', anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button2, self.button2,
                                                         controller, PageTen, PageTen), increment_all(PageTen, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button1, self.button1,
                                                         controller, PageTen, PageTen), increment_all(PageTen, "B")])
        self.button2.pack()
        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(750, 385, window=self.button2)
        self.canvas.pack()


app = None


def main():
    global app
    app = TkinterApp()
    app.mainloop()


def exit_app():
    global app
    app.destroy()
    app.quit()


def try_again():
    global app
    exit_app()
    main()


def close_app(root):

    root.destroy()


def reset():
    global incr_all
    incr_all = 0
    return incr_all


count = 0
numCount = 0

# Raspunsurile corecte memorate in mai multe liste.
answer_Univers = {
    "PageOne": {
        "A": 0,
        "B": 1,
        "C": 0
    },
    "PageTwo": {
        "A": 1,
        "B": 0,
        "C": 0
    },
    "PageThree": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0
    },
    "PageFour": {
        "A": 0,
        "B": 1,
        "C": 0
    },
    "PageFive": {
        "A": 1,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageSix": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 1
    },
    "PageSeven": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0
    },
    "PageEight": {
        "A": 1,
        "B": 0,
        "C": 0
    },
    "PageNine": {
        "A": 1,
        "B": 0,
        "C": 0
    },
    "PageTen": {
        "A": 0,
        "B": 1
    }
}

answer_user = {
    "PageOne": {
        "A": 0,
        "B": 0,
        "C": 0
    },
    "PageTwo": {
        "A": 0,
        "B": 0,
        "C": 0
    },
    "PageThree": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageFour": {
        "A": 0,
        "B": 0,
        "C": 0
    },
    "PageFive": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageSix": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageSeven": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageEight": {
        "A": 0,
        "B": 0,
        "C": 0
    },
    "PageNine": {
        "A": 0,
        "B": 0,
        "C": 0
    },
    "PageTen": {
        "A": 0,
        "B": 0
    }
}
button1_num = 1
dd = ""
da = str(PageTen.__name__)
print(str(PageTen.__name__))
print(type(da))

checked = 0


def increment_all(cur_Page, index_answer):
    global answer_Univers
    global answer_user
    global incr_all
    global checked
    indx = index_answer
    cur_Page = str(cur_Page.__name__)
    if cur_Page in answer_Univers.keys():
        if index_answer in list(answer_Univers[cur_Page].keys()):
            if answer_Univers[cur_Page].get(indx) == 1:
                for x in answer_user[cur_Page]:
                    answer_user[cur_Page][x] = 0
                print(index_answer + ": Good Answer")
                answer_user[cur_Page].update({index_answer: 1})
                print(list(answer_user[cur_Page].keys()))
                print(list(answer_user[cur_Page].values()))
                incr_all += 1
            else:
                for x in answer_user[cur_Page]:
                    answer_user[cur_Page][x] = 0
                answer_user[cur_Page].update({index_answer: 1})
                print(index_answer + ": Bad Answer")
                print(list(answer_user[cur_Page].keys()))
                print(list(answer_user[cur_Page].values()))
    print(list(answer_user.values()))

    for x in list(answer_user.keys()):
        for y in list(answer_user[x].values()):
            if y == 1:
                checked += 1
    if checked != 10:
        checked = 0
    else:
        checked = 0
        print("Acesta este: " + str(list(answer_user.values())))
        return CheckScore.main(incr_all, app, answer_user, answer_Univers)

# Functie utilizata pentru a afisa scorul obtinut.
def result():
    CheckScore.main(incr_all, app)
    print(list(answer_user.values()))

# Functie utilizata pentru a reseta toate raspunsurile utilizatorului.
def reset_answer_user():
    global answer_user
    for x in list(answer_user.keys()):
        for y in list(answer_user[x].keys()):
            answer_user[x].update({y: 0})
    print(answer_user)
    return answer_user

# Pentru varianta de raspuns selectata, se va modifica culoarea butonului cu verde.
def bg_button(button_A, buttonB, buttonC, buttonD, root, num_page, cur_page):
    global count
    global Univers
    global button1_num

    if count == 0:
        button_A.config(background = 'green', activebackground='green')
        buttonB.config(background='black', activebackground='black')
        buttonC.config(background='black', activebackground='black')
        buttonD.config(background='black', activebackground='black')
        print(button_A)
        if button1_num == list(answer_Univers["PageOne"].keys())[list(answer_Univers["PageOne"].values()).index(1)]:
            print("Aceasta este buna")
        else:
            button1_num = 0

    root.show_frame(num_page)
    return button_A


if __name__ == '__main__':
    main()
