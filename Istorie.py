from tkinter import *
import tkinter as tk
from PIL import ImageTk, ImageFilter
from PIL import Image, ImageOps
from cairosvg import svg2png
from io import BytesIO
import CheckScore


def frame(im, thickness=5):
    iw, ih = im.size
    ow, oh = iw+2*thickness, ih+2*thickness

    outer = f'<svg width="{ow}" height="{oh}" style="background-color:none"><rect rx="20" ry="20" width="{ow}" height="{oh}" fill="black"/></svg>'
    png   = svg2png(bytestring=outer)
    outer = Image.open(BytesIO(png))

    inner = f'<svg width="{ow}" height="{oh}"><rect x="{thickness}" y="{thickness}" rx="20" ry="20" width="{iw}" height="{ih}" fill="white"/></svg>'
    png   = svg2png(bytestring=inner)
    inner = Image.open(BytesIO(png)).convert('L')

    expanded = ImageOps.expand(im, border=thickness, fill=(0, 0, 0)).convert('RGB')

    outer.paste(expanded, None, inner)
    return outer


LARGE = ('Verdana', 10)
incr_all = 0
y = 0


class TkinterApp(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand= True)

        self.frames={}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive,
                  PageSix, PageSeven, PageEight, PageNine, PageTen):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.title('Istorie Quiz')
        self.image1 = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_istorie\\wallpaper_istorie2.jpg")
        self.image1 = self.image1.resize((1200, 700))

        incr_all = 0

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(0))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50,50))
        self.arrowRight_image = self.arrowRight_image.resize((50,50))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())

        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)

        self.canvas.create_text(70, 270, text='Spre deosebire de povestirea ficțională, specia de povestire numită '
                                             'istorie nu este construită prin intuiție intelectuală,\nci pornind de '
                                             'la surse: documente scrise, istorie orală, obiecte etc. Prin interpretarea'
                                             ' totalității acestor surse, istoria\nîși propune să reconstituie diversele'
                                             ' fațete ale trecutului. De-a lungul timpului, istoricii și-au schimbat '
                                             'foarte mult felul\nde a interpreta trecutul și perspectiva asupra faptelor'
                                             ' sau a evenimentelor trecute, și-au reevaluat sursele și maniera\n'
                                             '                                                           de a aborda '
                                             'respectivele surse.', anchor=NW, font=('Arial Unicode MS', 15), 
                                fill='black')

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
        controller.title('Istorie Quiz')
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))
        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie1.jpg")
        self.grasSat = self.grasSat.resize((500, 350))

        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                                                      self.arrowRight_image.convert('RGBA'))

        self.grasSat_brd = ImageOps.expand(self.grasSat, border=2, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (600, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='              In ce an a avut loc Batalia de la Hastings?',fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='1066', fill='white', anchor=NW, font=('Arial Unicode MS', 15))#rasp corect
        self.canvas.create_text(100, 420, text='1068', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100,470, text='1918', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 520, text='1963', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        x = IntVar()
        self.button1 = Button(self, text='A', fg='white',activeforeground='white', background='black',
                              activebackground = 'black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageTwo, PageOne), increment_all(PageOne, "D")])
        self.button4.pack()
        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.create_window(70, 535, window=self.button4)

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

#       controller.bind('<KeyRelease>', on_key_release)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))

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

        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie2.jpeg")
        self.grasSat = self.grasSat.resize((550, 350))
        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='Când a fost încoronarea reginei Elisabeta a II-a?', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='2 Iunie 1956', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='2 iunie 1961', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 470, text='2 iunie 1953', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button1, self.button3,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button1, self.button2,
                                                         controller, PageThree, PageTwo), increment_all(PageTwo, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.title('Fitness Quiz')
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))
        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie3.jpg")
        self.grasSat = self.grasSat.resize((500,350))

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

        self.grasSat_brd = ImageOps.expand(self.grasSat, border=2, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (600, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='              Ce razboi a aparut pe 1 septembrie 1939?', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Primul Razboi Mondial', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='Al Doilea Razboi Mondial', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(100,470, text='Razboiul din Vietnam', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 520, text='Razboiul Trandafirilor', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        x = IntVar()
        self.button1 = Button(self, text='A', fg='white',activeforeground='white', background='black',
                              activebackground = 'black', font=('Ink Fre', 17), width=3,
                              command=lambda:  [bg_button(self.button1, self.button2, self.button3, self.button4,
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
        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.create_window(70, 535, window=self.button4)

        self.canvas.grid_configure(sticky="nsew")
        self.canvas.pack()

        controller.minsize(self.gaussImage.width(), self.gaussImage.height())


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))

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

        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie4.jpg")
        self.grasSat = self.grasSat.resize((550, 350))
        # self.grasSat_brd_rd = frame(self.grasSat, 2)
        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='Care om de stiinta a descoperit gravitatia?', fill='white',  anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Galileo Galilei', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='Isaac Newton', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(100, 470, text='Thomas Edison', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageFive, PageFour), increment_all(PageFour, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageFive, PageFour), increment_all(PageFour, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button1, self.button2,
                                                         controller, PageFive, PageFour), increment_all(PageFour, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))

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

        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie5.jpg")
        self.grasSat = self.grasSat.resize((550, 350))

        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='Care a fost primul om ce a mers pe Luna?',fill='white',  anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Alan Bean', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='Pete Conrad', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 470, text='Neil Armstrong', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageSix, PageFive), increment_all(PageFive, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageSix, PageFive), increment_all(PageFive, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button1, self.button2,
                                                         controller, PageSix, PageFive), increment_all(PageFive, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))

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

        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie6.jpg")
        self.grasSat = self.grasSat.resize((550, 350))
        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='Ce au mestecat vechii egipteni pentru a vindeca un stomac "sarac"?',
                                fill='white',  anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Menta', fill='white', anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(100, 420, text='Frunze de varza', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 470, text='Porumb dulce', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button2,
                                                         controller, PageSeven, PageSix), increment_all(PageSix, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.img = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                              "quiz_istorie\\quiz_istorie6.jpg")
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
                                text='                                             Cine a creat prima forță de poliție '
                                     'din Marea Britanie?'
                                ,
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='Sir Edward Redmayne', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='Sir Robert Peel', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(780, 370, text='Sir Frank Columbo', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 420, text='Sir James Taggart', fill='white',
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
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.img = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                              "quiz_istorie\\quiz_istorie6.jpg")
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
                                text='                                          '
                                     'Cand a inceput si cand s-a incheiat Razboiul Rece?'
                                ,
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='1939-1945', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='1943-1973', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='1947-1991', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(780, 420, text='1952-1963', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button4,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button4,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button4,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button4, self.button1, self.button2, self.button3,
                                                         controller, PageNine, PageEight),
                                               increment_all(PageEight, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))

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

        self.grasSat = Image.open("C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
                                  "quiz_istorie\\quiz_istorie7.jpg")
        self.grasSat = self.grasSat.resize((550, 350))

        self.grasSat_brd = ImageOps.expand(self.grasSat, border=1, fill='black')
        self.gaussImage.paste(self.grasSat_brd, (550, 220))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100,170, text='In ce tara se afla monumentul preistoric Stonehenge?',fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 370, text='Anglia', fill='white', anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(100, 420, text='Rusia', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 470, text='China', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button1, self.button2, self.button3, self.button3,
                                                         controller, PageTen, PageNine), increment_all(PageNine, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button2, self.button1, self.button3, self.button3,
                                                         controller, PageTen, PageNine), increment_all(PageNine, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [bg_button(self.button3, self.button1, self.button2, self.button2,
                                                         controller, PageTen, PageNine), increment_all(PageNine, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\"
            "quiz_istorie\\wallpaper_istorie1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))

        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))
        self.controller = controller
        self.controller.protocol("WM_DELETE_WINDOW", lambda: [reset_answer_user(), self.controller.destroy()])
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(300, 200, text='Nelson Mandela a fost presedintele Africii (1994-1999)',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16, 'bold'))
        self.canvas.create_text(380, 370, text='Adevarat', fill='white', anchor=NW, font=('Arial Unicode MS', 15)) #rasp corect
        self.canvas.create_text(780, 370, text='Fals', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

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


def close_app(root):

    root.destroy()


def reset():
    global incr_all
    incr_all = 0
    return incr_all


answer_Istorie = {
    "PageOne": {
        "A": 1,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageTwo": {
        "A": 0,
        "B": 0,
        "C": 1
    },
    "PageThree": {
        "A": 0,
        "B": 1,
        "C": 0,
        "D": 0
    },
    "PageFour": {
        "A": 0,
        "B": 1,
        "C": 0
    },
    "PageFive": {
        "A": 0,
        "B": 0,
        "C": 1,
    },
    "PageSix": {
        "A": 1,
        "B": 0,
        "C": 0,
    },
    "PageSeven": {
        "A": 0,
        "B": 1,
        "C": 0,
        "D": 0
    },
    "PageEight": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0
    },
    "PageNine": {
        "A": 1,
        "B": 0,
        "C": 0
    },
    "PageTen": {
        "A": 1,
        "B": 0
    }
}

answer_user = {
    "PageOne": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
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
    },
    "PageSix": {
        "A": 0,
        "B": 0,
        "C": 0,
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
        "C": 0,
        "D": 0
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

checked = 0

numCountCheck = 0


def increment_all(cur_Page, index_answer):
    global answer_Istorie
    global answer_user
    global incr_all
    global checked
    indx = index_answer
    cur_Page = str(cur_Page.__name__)
    if cur_Page in answer_Istorie.keys():
        if index_answer in list(answer_Istorie[cur_Page].keys()):
            if answer_Istorie[cur_Page].get(indx) == 1:
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
        #   global numCountCheck
        checked = 0
        #   numCountCheck = 1
        print("Acesta este: " + str(list(answer_user.values())))
        return CheckScore.main(incr_all, app, answer_user, answer_Istorie)


def result():

    CheckScore.main(incr_all, app)

    print(list(answer_user.values()))


def reset_answer_user():
    global answer_user
    for x in list(answer_user.keys()):
        for y in list(answer_user[x].keys()):
            answer_user[x].update({y: 0})
    print(answer_user)
    return answer_user


def bg_button(button1, button2, button3, button4, root, num_page, cur_page):
    global count
    if count == 0:
        button1.config(background = 'green', activebackground='green')
        button2.config(background='black', activebackground='black')
        button3.config(background='black', activebackground='black')
        button4.config(background='black', activebackground='black')
        print(button1)
    root.show_frame(num_page)
    return button1


if __name__ == '__main__':
      main()
