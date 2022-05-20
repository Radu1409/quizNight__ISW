from tkinter import *
import tkinter as tk
from PIL import ImageTk, ImageFilter
from PIL import Image, ImageOps
from cairosvg import svg2png
from io import BytesIO
import CheckScore


def frame(im, thickness=5):

    iw, ih = im.size
    ow, oh = iw + 2 * thickness, ih + 2 * thickness

    outer = f'<svg width="{ow}" height="{oh}" style="background-color:none"><rect rx="20" ry="20" width="{ow}" height="{oh}" fill="black"/></svg>'
    png = svg2png(bytestring=outer)
    outer = Image.open(BytesIO(png))

    inner = f'<svg width="{ow}" height="{oh}"><rect x="{thickness}" y="{thickness}" rx="20" ry="20" width="{iw}" height="{ih}" fill="white"/></svg>'
    png = svg2png(bytestring=inner)
    inner = Image.open(BytesIO(png)).convert('L')

    expanded = ImageOps.expand(im, border=thickness, fill=(0, 0, 0)).convert('RGB')

    outer.paste(expanded, None, inner)
    return outer


LARGE = ('Verdana', 10)


class TkinterApp(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour,
                  PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen):
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

        self.image1 = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_it\\wallpaper_it3.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(2))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        # controller.geometry("1200x700")

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())

        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)

        self.canvas.create_text(70, 270,
                                text='Cu toții știm că în IT oportunitățile de creștere sunt nelimitate, iar odată cu'
                                     ' acesteași alegerea traseului de învățare\npoate fi ușor complicat, mai ales dacă'
                                     ' te afli la prima interacțiune cu lumea tehnică. Răspunsul la întrebarea “De\n'
                                     'unde să încep?” este cu atât mai încâlcit când te gândești la schimbarea carierei'
                                     ' și a domeniului de activitate. Dar,\nîn cele din urmă, asta face parte din '
                                     'farmecul domeniului.Pentru a intelege mai usor si a evolua in domeniul IT, ai\n'
                                     '       nevoie sa asimilezi cunostintele de baza, iar pentru acest lucru, am '
                                     'pregatit un quiz special pentru tine.',
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

        controller.resizable(False, False)
        controller.minsize(self.gaussImage.width(), self.gaussImage.height())


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.title('It Quiz')
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))
        self.grasSat = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\"
                                  "Choose\\quiz_it\\quiz_it1.jpg")
        self.grasSat = self.grasSat.resize((550, 350))

        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        ##################
        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))

        self.grasSat_brd_rd = frame(self.grasSat, 2)
        self.gaussImage.paste(self.grasSat_brd_rd, (600, 200), self.grasSat_brd_rd.convert('RGBA'))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='Care sunt cele mai folosite limbaje de programare?', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 355, text='Python, Ruby, C++, Switft', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 410, text='Python, Java, JavaScript, C++', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(100, 460, text='Objective C, C++, Java, Kotlin', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        x = IntVar()
        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button3, controller, PageTwo,
                                            PageOne), increment_all(PageOne, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button3, controller, PageTwo,
                                            PageOne), increment_all(PageOne, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button2, controller, PageTwo,
                                            PageOne), increment_all(PageOne, "C")])
        self.button3.pack()
        self.canvas.create_window(70, 370, window=self.button1)
        self.canvas.create_window(70, 420, window=self.button2)
        self.canvas.create_window(70, 470, window=self.button3)

        self.canvas.grid_configure(sticky="nsew")
        self.canvas.pack()
        controller.minsize(self.gaussImage.width(), self.gaussImage.height())


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
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
                                  "quiz_it\\quiz_it2.jpg")
        self.grasSat = self.grasSat.resize((550, 350))
        self.grasSat_brd_rd = frame(self.grasSat, 2)
        self.gaussImage.paste(self.grasSat_brd_rd, (600, 180), self.grasSat_brd_rd.convert('RGBA'))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170, text='Cine a fondat compania Apple?', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 365, text='Ronald Wayne', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 420, text='Steve Jobs', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(100, 475, text='Steve Wozniak', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button3, controller,
                                            PageThree, PageTwo), increment_all(PageTwo, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button1, self.button3, controller,
                                            PageThree, PageTwo), increment_all(PageTwo, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button1, self.button2, controller,
                                            PageThree, PageTwo), increment_all(PageTwo, "C")])
        self.button3.pack()

        self.canvas.create_window(70, 385, window=self.button1)
        self.canvas.create_window(70, 435, window=self.button2)
        self.canvas.create_window(70, 485, window=self.button3)
        self.canvas.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
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
                              'quiz_it\\quiz_it3.jpg')
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170,
                                text='         O rețea concepută pentru a permite comunicarea în cadrul unei '
                                     'organizații se numește:',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Browser', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 420, text='Internet', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 470, text='Intranet', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(180, 520, text='World Wide Web', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller,
                                            PageFour, PageThree), increment_all(PageThree, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller,
                                            PageFour, PageThree), increment_all(PageThree, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller,
                                            PageFour, PageThree), increment_all(PageThree, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller,
                                            PageFour, PageThree), increment_all(PageThree, "D")])
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
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
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
                              'quiz_it\\quiz_it4.jpg')
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170,
                                text='             Care este numele unui dispozitiv de indicare a computerului?',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Monitor', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 420, text='Mouse', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(180, 470, text='Moden', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 520, text='Placa de sunet', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller,
                                            PageFive, PageFour), increment_all(PageFour, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller,
                                            PageFive, PageFour), increment_all(PageFour, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller,
                                            PageFive, PageFour), increment_all(PageFour, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller,
                                            PageFive, PageFour), increment_all(PageFour, "D")])
        self.button4.pack()

        self.canvas.create_window(150, 385, window=self.button1)
        self.canvas.create_window(150, 435, window=self.button2)
        self.canvas.create_window(150, 485, window=self.button3)
        self.canvas.create_window(150, 535, window=self.button4)
        self.canvas.pack()


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
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
                              'quiz_it\\quiz_it5.jpg')
        self.img = self.img.resize((500, 300))
        self.img_border = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.img_border, (660, 260))
        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(100, 170,
                                text='                                                '
                                     'Ce sistem de operare a dezvoltat Google?',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(180, 370, text='Android', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(180, 420, text='iOS', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 470, text='Windows', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(180, 520, text='BlackBerry OS', fill='white', anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller, PageSix,
                                            PageFive), increment_all(PageFive, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller, PageSix,
                                            PageFive), increment_all(PageFive, "B")])
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller, PageSix,
                                            PageFive), increment_all(PageFive, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller, PageSix,
                                            PageFive), increment_all(PageFive, "D")])
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
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
        self.image1 = self.image1.resize((1200, 700))
        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowRight_image = Image.open("Python_images/arrows/arrow_right.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))
        self.arrowRight_image = self.arrowRight_image.resize((50, 50))

        self.img = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\'
                              'quiz_it\\quiz_it6.jpg')
        self.img = self.img.resize((500, 400))
        self.img_brd = ImageOps.expand(self.img, border=2, fill='black')

        self.gaussImage.paste(self.arrowRight_image, (self.gaussImage.size[0] - self.arrowRight_image.size[0] - 20,
                                                      self.gaussImage.size[1] - self.arrowRight_image.size[1] - 20),
                              self.arrowRight_image.convert('RGBA'))
        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))
        self.gaussImage.paste(self.img_brd, (660, 125))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)
        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(120, 170, text='Ce înseamnă acronimul FTP?', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 16))
        self.canvas.create_text(100, 360, text='File transfer protocol', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(100, 410, text='Fast total processing', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(100, 460, text='Free transistor protocol', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button3, controller,
                                            PageSeven, PageSix), increment_all(PageSix, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button3, controller,
                                            PageSeven, PageSix), increment_all(PageSix, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button2, controller,
                                            PageSeven, PageSix), increment_all(PageSix, "C")])
        self.button3.pack()
        self.canvas.create_window(70, 375, window=self.button1)
        self.canvas.create_window(70, 425, window=self.button2)
        self.canvas.create_window(70, 475, window=self.button3)
        self.canvas.pack()


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_it\\wallpaper_it1.jpg")
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
                                text='           Care dintre acestea nu este unul dintre primele „protocoale” sau '
                                     'modalități de utilizare\n'
                                     '                                                               a internetului?',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='FTP', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='Telnet', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='blogging', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(780, 420, text='Gopher', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller,
                                            PageEight, PageSeven), increment_all(PageSeven, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller,
                                            PageEight, PageSeven), increment_all(PageSeven, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller,
                                            PageEight, PageSeven), increment_all(PageSeven, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller,
                                            PageEight, PageSeven), increment_all(PageSeven, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_it\\wallpaper_it1.jpg")
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
                                text='                                                          Colectia de 1024 Biti:',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='1MB', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='1KB', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(780, 370, text='1TB', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 420, text='1GB', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller,
                                            PageNine, PageEight), increment_all(PageEight, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller,
                                            PageNine, PageEight), increment_all(PageEight, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller,
                                            PageNine, PageEight), increment_all(PageEight, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller,
                                            PageNine, PageEight), increment_all(PageEight, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                 "quiz_it\\wallpaper_it1.jpg")
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
                                text='           Identificați dispozitivul prin care datele și instrucțiunile sunt '
                                     'introduse într-un computer',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16))
        self.canvas.create_text(380, 370, text='Software', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))
        self.canvas.create_text(380, 420, text='Output device', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(780, 370, text='Input device', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))  # rasp corect
        self.canvas.create_text(780, 420, text='Memory', fill='white',
                                anchor=NW, font=('Arial Unicode MS', 15))

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button3, self.button4, controller, PageTen,
                                            PageNine), increment_all(PageNine, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button3, self.button4, controller, PageTen,
                                            PageNine), increment_all(PageNine, "B")])
        self.button2.pack()
        self.button3 = Button(self, text='C', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button3, self.button1, self.button2, self.button4, controller, PageTen,
                                            PageNine), increment_all(PageNine, "C")])
        self.button3.pack()
        self.button4 = Button(self, text='D', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button4, self.button1, self.button2, self.button3, controller, PageTen,
                                            PageNine), increment_all(PageNine, "D")])
        self.button4.pack()

        self.canvas.create_window(350, 385, window=self.button1)
        self.canvas.create_window(350, 435, window=self.button2)
        self.canvas.create_window(750, 385, window=self.button3)
        self.canvas.create_window(750, 435, window=self.button4)
        self.canvas.pack()


class PageTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image1 = Image.open(
            "C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\quiz_it\\wallpaper_it1.jpg")
        self.image1 = self.image1.resize((1200, 700))

        self.gaussImage = self.image1.filter(ImageFilter.GaussianBlur(5))
        self.gaussImage = self.gaussImage.resize((1200, 700))

        self.arrowLeft_image = Image.open("Python_images/arrows/arrow_left.png")
        self.arrowLeft_image = self.arrowLeft_image.resize((50, 50))

        self.gaussImage.paste(self.arrowLeft_image, (20,
                                                     self.gaussImage.size[1] - self.arrowLeft_image.size[1] - 20),
                              self.arrowLeft_image.convert('RGBA'))

        self.gaussImage = ImageTk.PhotoImage(self.gaussImage)

        self.controller = controller
        self.controller.protocol("WM_DELETE_WINDOW", lambda: [reset_answer_user(), self.controller.destroy()])

        self.canvas = Canvas(self, width=self.gaussImage.width(), height=self.gaussImage.height())
        self.canvas.create_image(0, 0, image=self.gaussImage, anchor=NW)
        self.canvas.create_text(400, 200, text='"Nu oricine poate ajunge programator"',
                                fill='white', anchor=NW, font=('Arial Unicode MS', 16, 'bold'))
        self.canvas.create_text(380, 370, text='Adevarat', fill='white', anchor=NW, font=('Arial Unicode MS', 15))
        self.canvas.create_text(780, 370, text='Fals', fill='white', anchor=NW,
                                font=('Arial Unicode MS', 15))  # rasp corect

        self.button1 = Button(self, text='A', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button1, self.button2, self.button2, self.button2, controller, PageTen,
                                            PageTen), increment_all(PageTen, "A")])
        self.button1.pack()
        self.button2 = Button(self, text='B', fg='white', activeforeground='white', background='black',
                              activebackground='black', font=('Ink Fre', 17), width=3,
                              command=lambda: [
                                  bg_button(self.button2, self.button1, self.button1, self.button1, controller, PageTen,
                                            PageTen), increment_all(PageTen, "B")])
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


answer_It = {
    "PageOne": {
        "A": 0,
        "B": 1,
        "C": 0,
    },
    "PageTwo": {
        "A": 0,
        "B": 1,
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
        "C": 0,
        "D": 0
    },
    "PageFive": {
        "A": 1,
        "B": 0,
        "C": 0,
        "D": 0
    },
    "PageSix": {
        "A": 1,
        "B": 0,
        "C": 0
    },
    "PageSeven": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0
    },
    "PageEight": {
        "A": 0,
        "B": 1,
        "C": 0,
        "D": 0
    },
    "PageNine": {
        "A": 0,
        "B": 0,
        "C": 1,
        "D": 0
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
        "C": 0,
        "D": 0
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
        "C": 0,
        "D": 0
    },
    "PageTen": {
        "A": 0,
        "B": 0
    }
}

checked = 0


def increment_all(cur_Page, index_answer):
    global answer_It
    global answer_user
    global incr_all
    global checked
    indx = index_answer
    cur_Page = str(cur_Page.__name__)
    if cur_Page in answer_It.keys():
        if index_answer in list(answer_It[cur_Page].keys()):
            if answer_It[cur_Page].get(indx) == 1:
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
        return CheckScore.main(incr_all, app, answer_user, answer_It)


def result():
    CheckScore.main(incr_all, app)
    print(list(answer_user.values()))


def reset_answer_user():
    global answer_user
    for x in list(answer_user.keys()):
        # print()
        for y in list(answer_user[x].keys()):
            answer_user[x].update({y: 0})
            # print(list(Univers[x].values()))
    print(answer_user)
    return answer_user


def bg_button(button1, button2, button3, button4, root, num_page, cur_page):
    global count
    if count == 0:
        button1.config(background='green', activebackground='green')
        button2.config(background='black', activebackground='black')
        button3.config(background='black', activebackground='black')
        button4.config(background='black', activebackground='black')
        print(button1)
    root.show_frame(num_page)
    return button1


if __name__ == '__main__':
    main()
