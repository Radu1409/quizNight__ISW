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

    def __init__(self, master):

        frame = Frame(master)

        self.master = master
        self.master.title('Choose')
        self.image = PhotoImage(file='New folder/QuizGamePython.png')
        self.master.iconphoto(True, self.image)

        self.image1 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'wall_background_mauve_light.jpg')
        self.image1 = self.image1.resize((900, 570))

        self.image2 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'simpson_choose.png')
        self.image2 = self.image2.resize((150, 150))

        self.image3 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_istorie\\wallpaper_istorie3.jpg')
        self.image3 = self.image3.resize((180, 140), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.image3)

        self.image4 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_Univers\\wallpaper_Univers3.jpg')
        self.image4 = self.image4.resize((180, 140), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(self.image4)

        self.image5 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_Geografie\\wallpaper_Geografie.jpg')
        self.image5 = self.image5.resize((180, 140), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(self.image5)

        self.image6 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_IT\\wallpaper_IT3.jpg')
        self.image6 = self.image6.resize((180, 140), Image.ANTIALIAS)
        self.image6 = ImageTk.PhotoImage(self.image6)

        self.image7 = Image.open('C:\\Users\\Lenovo\\PycharmProjects\\Proiect_Python\\Python_images\\Choose\\'
                                 'Choose_Fitness\\wallpaper_fitness2.jpg')
        self.image7 = self.image7.resize((180, 140), Image.ANTIALIAS)
        self.image7 = ImageTk.PhotoImage(self.image7)

        self.image1.paste(self.image2, (self.image1.size[0] - self.image2.size[0],
                                        self.image1.size[1] - self.image2.size[1]), self.image2.convert('RGBA'))

        self.image1 = ImageTk.PhotoImage(self.image1)

        self.canvas = Canvas(master, width=self.image1.width(), height=self.image1.height())
        self.canvas.create_image(0, 0, image=self.image1, anchor=NW)

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
        self.canvas.create_text(20, 50, text='Please choose the type of question:', fill='white', anchor=NW,
                                font=('Ink Free', 25, ' bold'))

        self.canvas.pack()

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

        frame.pack()


def main():
    root = Tk()
    b = Choose(root)
    root.resizable(False, False)
    root.mainloop()


def exitChoose(root):
    root.destroy()


def minimizeChoose():
    global root
    root.update()
    root.deiconify()


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
    return args


if __name__ == '__main__':
    main()
