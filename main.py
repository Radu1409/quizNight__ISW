from tkinter import *
from tkinter import messagebox
from Choose import main
from PIL import Image, ImageTk
import tkinter
import IdPass



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
    window.destroy()


def exitWin():
    window.destroy()


def switch():
    if button1["state"] == NORMAL:
        button1["state"] = DISABLED
    else:
        button1["state"] = NORMAL


def toLogin():
    global countLogin
    global user
    global passw
    global button1
    global numLoginCount

    countLogin += 1

    screen1 = Toplevel(window)
    screen1.title("Autentificare")
    image1 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\Login\\Login1.jpg')
    image1 = image1.rotate(180)
    image1 = ImageTk.PhotoImage(image1)

    canvas = Canvas(screen1, width=image1.width(), height=image1.height())
    canvas.create_image(0, 0, image=image1, anchor=NW)
    canvas.create_text(180, 200, text='Sign In', anchor=NW, font=('Arial Unicode MS', 22))
    canvas.create_text(80, 260, text='Username', anchor=NW, font=('PMingLiU-ExtB', 12, 'bold'))
    canvas.create_text(80, 340, text='Password', anchor=NW, font=('PMingLiU-ExtB', 12, 'bold'))

    if countLogin == 1:
        entrySet_user = StringVar()
        entrySet_pass = StringVar()
    else:
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
        global entry_user
        global entry_pass
        global countLogin

        if x.get() == 1:
            entry_user = user
            entry_pass = passw
            print('Bifat')

        else:
            entry_user = ''
            entry_pass = ''
            print('Nebifat')
            countLogin = 0

    def close_window():
        global user
        global passw

        checkboxActiveDeactive()

        try:
            user = entryUser.get()
            passw = entryPass.get()
        except:
            pass

        screen1.destroy()
        button1.config(state="normal")
        print("Window closed")

#   screen1.protocol("WM_DELETE_WINDOW", close_window)

    entryUser = Entry(screen1, width=25, textvariable=entrySet_user)
    entryPass = Entry(screen1, show='*', width=25, textvariable=entrySet_pass)
    entryUser.pack()
    entryPass.pack()

    entryUser.config(font=('Calibri', 13, 'italic'))
    entryPass.config(font=('Calibri', 13, 'italic'))

    canvas.create_window(194, 383, window=entryPass)
    canvas.create_window(194, 303, window=entryUser)

    entryUser.focus()

    image2 = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\submit_ButtonNew.png')
    image2 = image2.resize((300, 220), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    x = IntVar()

#   if cv2.getWindowProperty('Autentificare', 1) == -1
    checkbox = Checkbutton(screen1, text='Remember me', variable=x, onvalue=1, offvalue=0,
                           command=checkboxActiveDeactive)
    checkbox.pack()
    checkbox.config(font=('Ink Fre', 10), bg='#dadbdf', activebackground='#dadbdf')
    canvas.create_window(136, 430, window=checkbox)

    submit = Button(screen1, image=image2, width=206, height=45, borderwidth=0, bg='#dadbdf',
                    activebackground='#dadbdf', command=lambda: submitFun())
    submit.pack()

    def submitFun():

      while True:
        username = entryUser.get()
        password = entryPass.get()

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

        count += 1
        counts += 1

        if username == IdPass.check_user(username) and count == 0 and password == IdPass.check_pass(password) and counts == 0:
            print('FELICITARI, TE AI LOGAT DIN PRIMA! #1')
            tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')

            if x.get() == 1:
                user = entryUser.get()
                passw = entryPass.get()

            screen1.destroy()

            window.destroy()
            count = -1
            counts = -1
            main()
            break
        elif username == IdPass.check_user(username) and password == IdPass.check_pass(password):
            user_change = canvas.itemconfig(user_change, text='', fill='red', anchor=NW,
                                            font=('Arial Unicode MS', 8))
            pass_change = canvas.itemconfig(pass_change, text='', fill='red', anchor=NW,
                                            font=('Arial Unicode MS', 8))
            print('FELICITARI, TE AI LOGAT DIN PRIMA! #1')
            tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')

            if x.get() == 1:
                user = entryUser.get()
                passw = entryPass.get()

            screen1.destroy()
            window.destroy()
            count = -1
            counts = -1
            main()
            break

        elif username == IdPass.check_user(username) and count == 0 and password != IdPass.check_pass(password) and counts == 0:
            pass_change = canvas.create_text(90, 395, text='Parola gresita!', fill='red', anchor=NW,
                                             font=('Arial Unicode MS', 8))

            break

        elif username != IdPass.check_user(username) and count == 0 and password == IdPass.check_pass(password) and counts == 0:
            user_change = canvas.create_text(90, 316, text='Username gresit!', fill='red', anchor=NW,
                                             font=('Arial Unicode MS', 8))

            break
        else:
            if username != IdPass.check_user(username) and count == 0:
                user_change = canvas.create_text(90, 316, text='Username gresit!', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))
            if username != IdPass.check_user(username):
                num1 = 0

            if password != IdPass.check_pass(password) and counts == 0:
                pass_change = canvas.create_text(90, 395, text='Parola gresita!', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))
            if password != IdPass.check_pass(password):
                num2 = 0

            try:
                if username == IdPass.check_user(username):
                        user_change = canvas.itemconfig(user_change, text='', fill='red', anchor=NW,
                                                        font=('Arial Unicode MS', 8))
                        num1 = 1
                        count = -1

            except:
                num1 = 0
                user_change = canvas.create_text(90, 316, text='', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))
            try:
                if password == IdPass.check_pass(password):
                        pass_change = canvas.itemconfig(pass_change, text='', fill='red', anchor=NW,
                                                        font=('Arial Unicode MS', 8))
                        num2 = 1
                        counts = -1

            except:
                num2 = 0
                pass_change = canvas.create_text(90, 395, text='', fill='red', anchor=NW,
                                                 font=('Arial Unicode MS', 8))

            if num1 == 1 and num2 == 1:
                print(print('FELICITARI, TE AI LOGAT DIN PRIMA! #2'))
                tkinter.messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')
                if x.get() == 1:
                    user = entryUser.get()
                    passw = entryPass.get()
                    user_check = user
                    pass_check = passw

                screen1.destroy()
                num1 = 0
                num2 = 0
                main()
            break

    canvas.create_window(220, 480, window=submit)
    canvas.pack()
    label.pack()

    button1.config(state="disabled")
    screen1.protocol("WM_DELETE_WINDOW", close_window)

    screen1.resizable(False, False)
    screen1.mainloop()


window = Tk()

image = PhotoImage(file='New folder/QuizGamePython.png')
window.iconphoto(True, image)
window.title('Quiz Game')

image = Image.open('New folder/quizNight.jpeg')
image = image.resize((600, 550))
image = ImageTk.PhotoImage(image)

label = Label(window, image=image)
label.pack()

button1 = Button(window, text='Play')
button1.config(width=13)
button1.config(font=("Helvetica", 10, 'bold'), command=toLogin)
button1.place(x=245, y=450)

button = Button(window, text='Exit')
button.config(width = 13)
button.config(font=("Helvetica", 10, 'bold'), command=exitWin)
button.place(x=245, y=485)

openImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\open.png')
openImage = openImage.resize((20, 20))
openImage = ImageTk.PhotoImage(openImage)

saveImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\savee.png')
saveImage = saveImage.resize((20, 20))
saveImage = ImageTk.PhotoImage(saveImage)

exitImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\exiit.png')
exitImage = exitImage.resize((20, 20))
exitImage = ImageTk.PhotoImage(exitImage)

cutImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\cutt.png')
cutImage = cutImage.resize((20, 20))
cutImage = ImageTk.PhotoImage(cutImage)

copyImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\copy.png')
copyImage = copyImage.resize((20, 20))
copyImage = ImageTk.PhotoImage(copyImage)

pasteImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\pastee.png')
pasteImage = pasteImage.resize((20, 20))
pasteImage = ImageTk.PhotoImage(pasteImage)

scoreImage = Image.open('C:\\Users\\Lenovo\\Documents\\Proiecte_CV\\Proiect_CV_cu_MySQL\\Proiect_Python\\Python_images\\icon_FileMenu\\score.png')
scoreImage = scoreImage.resize((20, 20))
scoreImage = ImageTk.PhotoImage(scoreImage)

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))

menubar.add_cascade(label="File", menu = fileMenu)
fileMenu.add_command(label=' Open', image=openImage, compound='left')
fileMenu.add_command(label=" Save", image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label=' Exit', image=exitImage, compound='left', command=exitMenuBar)

editMenu = Menu(menubar, tearoff=False, font=('MV Boli', 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label=' Cut', image=cutImage, compound='left')
editMenu.add_command(label=' Copy', image=copyImage, compound='left')
editMenu.add_command(label=' Paste', image=pasteImage, compound='left')

readMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label='Read', menu=readMenu)

readMenu.add_command(label=" Score", image=scoreImage, compound='left')

window.resizable(False, False)
window.mainloop()








