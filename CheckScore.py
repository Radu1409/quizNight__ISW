from tkinter import *
import tkinter
from PIL import ImageTk, Image
import Istorie
import Univers
import Geografie
import It
import Fitness
from Choose import *


import CheckInfo

argument = 0
numCountCheck = 0


def close_both(root1):

    root1.destroy()


def main(var, new, dict, old_dict):
    global numCountCheck
    print(argument)
    root = Toplevel()
    new.destroy()
    d = CheckScore(root, var, new, dict, old_dict)

    root.mainloop()
    return root, dict


def funct():
    argum = argument
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
    def __init__(self, master, var, new, dict, old_dict):
        frame = Frame(master)
        self.master = master
        self.master.title('Score')
        self.master.geometry('400x200')
        if 'normal' == self.master.state():
            self.master.focus_set()
        if hasattr(Istorie, 'self.master'):
            self.master.lift()
        page = None

        self.canvas = Canvas(master, width=400, height=200)

        self.button_check = Button(self.master, text='Check info', font=('Ink Fre', 12),
                                   command=lambda: [close_both(self.master), CheckInfo.main(dict, old_dict, var, new)])
        self.button_try = Button(self.master, text="Try again", font=('Ink Fre', 12),
                                 command=lambda: [close_both(self.master), new.destroy(), funct()])
        self.button_close = Button(self.master, text='Close', font=('Ink Fre', 12),
                                   command=lambda: [close_both(self.master), new.destroy(), functs()])

        self.button_check.pack()
        self.button_try.pack()
        self.button_close.pack()
        self.image = Image.open("C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Choose\\"
                                "wall_background_mauve.jpg")

        self.master.protocol("WM_DELETE_WINDOW", lambda: [close_wind_reset_score(self.master, dict), new.destroy()])

        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
        self.canvas.create_text(65, 50, text="Your score is " + str(var) + "/" + "10", fill='white', anchor=NW,
                                font=('Ink Free', 25, 'bold'))
        self.canvas.create_window(75, 150, window=self.button_check)
        self.canvas.create_window(200,150, window=self.button_try)
        self.canvas.create_window(315, 150, window=self.button_close)
        self.canvas.pack()

        self.master.focus_set()
        self.master.wm_attributes("-topmost", 1)
        self.master.resizable(False, False)

        self.master.mainloop()


if __name__ == '__main__':
    pass
