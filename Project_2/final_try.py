import tkinter as tk
import tkmacosx as tkm
import tkinter.font
import requests
import pickle
import win
import webbrowser
from importlib import reload
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from time import strftime
from datetime import date, timezone, timedelta
from datetime import datetime
from tkcalendar import Calendar
from currency_converter import CurrencyConverter


color = {"nero": "#252726", "orange": "#FF8700"}
btnState = False  # this is for navbar
expression = ""  # this is for calculator
money = ""  # this is for currency converter
unit_value = ()  # this is for unit converter
convert_value = ()  # this is for unit converter

'''
---Useful tkinter tutorial(Chinese)
https://www.cnblogs.com/aland-1415/p/6849193.html
---class tkinterApp is for changing pages.
https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
---using buttons in navbar to change pages, learned from Youtube.
---historical currency converter, here is the lib.
https://github.com/alexprengere/currencyconverter#readme
---real time currency converter, here is the web.
https://data-flair.training/blogs/currency-converter-python/
'''


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, CalculatorPage, UnitConverterPage, CurrencyConverterPage, ToDoList, PasswordManager,
                  GamesPage, HelpPage):
            frame = F(container, self)  # initializing frame
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "HOME"  # The title you want to show
        self.mode = "hour"  # this is for time
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        # Time ######################################
        self.frm_time = tk.Frame(master=self, relief=tk.SUNKEN, borderwidth=3, bg=color['nero'])
        self.lbl_date = tk.Label(master=self.frm_time, font=("arial", 30, "bold"),
                                 bg=color['nero'], fg="white", height=2)
        self.lbl_time = tk.Label(master=self.frm_time, font=("arial", 30, "bold"),
                                 bg=color['nero'], fg="white", height=2)
        self.lbl_cst = tk.Label(master=self.frm_time, font=("arial", 30, "bold"),
                                bg=color['nero'], fg="white", height=2)
        self.lbl_utc= tk.Label(master=self.frm_time, font=("arial", 30, "bold"),
                               bg=color['nero'], fg="white", height=2)
        self.frm_time.pack(side='top', fill="both", expand=1)
        self.lbl_date.pack(side='top', fill='x')
        self.lbl_time.pack(side='top', fill="x")
        self.lbl_cst.pack(side='top', fill='x')
        self.lbl_utc.pack(side='top', fill="x")
        self.showdate()
        self.showtime()
        self.showcst()
        self.showutc()
        self.cal = Calendar(self.frm_time, selectmode='day', bg='black',
                            font=('arial', 18, 'bold'))
        self.cal.pack(side='top', pady=20)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  , fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()],
                                 anchor='w', )
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w', )
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w', )
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w', )
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def showtime(self):
        string = strftime("%H:%M:%S %p %Z")
        self.lbl_time.config(text=string)
        self.lbl_time.after(1000, self.showtime)  # 1秒钟以后执行time函数

    def showdate(self):
        string = strftime("%Y-%m-%d")
        self.lbl_date.config(text=string)

    def showcst(self):
        utc = datetime.utcnow().replace(tzinfo=timezone.utc)
        cst = utc.astimezone(timezone(timedelta(hours=8)))
        cst = cst.strftime('%H:%M:%S %p ')
        cst += 'CST'
        self.lbl_cst.config(text=cst)
        self.lbl_cst.after(1000, self.showcst)

    def showutc(self):
        utc = datetime.utcnow()
        utc = utc.strftime('%H:%M:%S %p ')
        utc += 'UTC'
        self.lbl_utc.config(text=utc)
        self.lbl_utc.after(1000, self.showutc)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True


class CalculatorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "CALCULATOR"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        # Calculator ##########################################################
        self.frm_cal = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_cal.pack(side="top", fill="both", expand=1)
        self.controller.bind("<Key>", self.key_handler)
        self.frm_result = tk.Frame(self.frm_cal, relief=tk.SUNKEN, borderwidth=1, bg=color['nero'])
        self.frm_result.pack(side="top", fill="x", expand=0)
        self.label_result = tk.Label(self.frm_result, text="", height=2, font=("times", 30), bg='white')
        self.label_result.pack(fill='x')
        # buttons ################
        self.frm_buttons = tk.Frame(self.frm_cal, relief=tk.SUNKEN, borderwidth=1, bg=color['nero'])
        self.frm_buttons.pack(side="top", fill="both", expand=1)
        # line 1 #######
        self.button_pleft = tkm.Button(self.frm_buttons, text="(", command=lambda: self.add("("), cursor="star",
                                       width=84, bd=5, bg=color['nero'], fg="white", activebackground="DimGray",
                                       height=80, relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_pleft.grid(row=1, column=0, padx=3, pady=5)

        self.button_pright = tkm.Button(self.frm_buttons, text=")", command=lambda: self.add(")"), cursor="star",
                                        width=84, bd=5, bg=color['nero'], fg="white", activebackground="DimGray",
                                        height=80, relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_pright.grid(row=1, column=1, padx=3, pady=5)

        self.button_clear = tkm.Button(self.frm_buttons, text="C", command=lambda: self.clear(), cursor="star",
                                       width=84, bd=5, bg=color['nero'], fg="white", activebackground="DimGray",
                                       height=80, relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_clear.grid(row=1, column=2, padx=3, pady=5)

        self.button_back = tkm.Button(self.frm_buttons, text="←️", command=lambda: self.back(), cursor="star",
                                      width=84, bd=5, bg=color['nero'], fg="white", activebackground="DimGray",
                                      height=80, relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_back.grid(row=1, column=3, padx=3, pady=5)
        # line 2 #######
        self.button_7 = tkm.Button(self.frm_buttons, text="7", command=lambda: self.add("7"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_7.grid(row=2, column=0, padx=3)

        self.button_8 = tkm.Button(self.frm_buttons, text="8", command=lambda: self.add("8"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_8.grid(row=2, column=1, padx=3)

        self.button_9 = tkm.Button(self.frm_buttons, text="9", command=lambda: self.add("9"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_9.grid(row=2, column=2, padx=3)

        self.button_divide = tkm.Button(self.frm_buttons, text="÷", command=lambda: self.add("/"), cursor="star",
                                        width=84, font=('Arial Rounded MT', 40), height=80,
                                        bd=5, bg=color['orange'], fg="white", activebackground="SandyBrown",
                                        relief=tk.RIDGE, borderwidth=3)
        self.button_divide.grid(row=2, column=3, padx=3)
        # line 3 #######
        self.button_4 = tkm.Button(self.frm_buttons, text="4", command=lambda: self.add("4"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_4.grid(row=3, column=0, padx=4, pady=3)

        self.button_5 = tkm.Button(self.frm_buttons, text="5", command=lambda: self.add("5"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_5.grid(row=3, column=1, padx=3, pady=3)

        self.button_6 = tkm.Button(self.frm_buttons, text="6", command=lambda: self.add("6"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_6.grid(row=3, column=2, padx=3, pady=3)

        self.button_multiply = tkm.Button(self.frm_buttons, text="×", command=lambda: self.add("*"), cursor="star",
                                          width=84, bd=5, bg=color['orange'], fg="white", activebackground="SandyBrown",
                                          relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40), height=80)
        self.button_multiply.grid(row=3, column=3, padx=3, pady=3)
        # line 4 #######
        self.button_1 = tkm.Button(self.frm_buttons, text="1", command=lambda: self.add("1"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_1.grid(row=4, column=0, padx=3)

        self.button_2 = tkm.Button(self.frm_buttons, text="2", command=lambda: self.add("2"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_2.grid(row=4, column=1, padx=3)

        self.button_3 = tkm.Button(self.frm_buttons, text="3", command=lambda: self.add("3"), cursor="star", width=84,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_3.grid(row=4, column=2, padx=3)

        self.button_subtract = tkm.Button(self.frm_buttons, text="−", command=lambda: self.add("-"), cursor="star",
                                          width=84, bd=5, bg=color['orange'], fg="white", activebackground="SandyBrown",
                                          relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40), height=80)
        self.button_subtract.grid(row=4, column=3, padx=3)
        # line 5 #######
        self.button_0 = tkm.Button(self.frm_buttons, text="0", command=lambda: self.add("0"), cursor="star", width=180,
                                   bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                   relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_0.grid(row=5, column=0, columnspan=2, padx=3, pady=5)

        self.button_dot = tkm.Button(self.frm_buttons, text=".", command=lambda: self.add("."), cursor="star", width=84,
                                     bd=5, bg=color['nero'], fg="white", activebackground="DimGray", height=80,
                                     relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_dot.grid(row=5, column=2, padx=3)

        self.button_add = tkm.Button(self.frm_buttons, text="+", command=lambda: self.add("+"), cursor="star", width=84,
                                     bd=5, bg=color['orange'], fg="white", activebackground="SandyBrown", height=80,
                                     relief=tk.RIDGE, borderwidth=3, font=('Arial Rounded MT', 40))
        self.button_add.grid(row=5, column=3, padx=3)
        # line 6 #######
        self.button_equals = tkm.Button(self.frm_buttons, text="=", width=373, command=lambda: self.calculate(),
                                        cursor="star", bd=5, bg=color['orange'], fg='white', height=60,
                                        activebackground="SandyBrown", relief=tk.RIDGE, borderwidth=3,
                                        font=('Arial Rounded MT', 40))
        self.button_equals.grid(row=6, column=0, columnspan=4, padx=3)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  ,fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()], anchor='w',)
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w',)
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w',)
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w',)
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True

    def add(self, value):  # add the value into the expression
        global expression
        expression += value
        self.label_result.config(text=expression)

    def clear(self):  # clear the expression
        global expression
        expression = ""
        self.label_result.config(text=expression)

    def back(self):
        global expression
        expression = expression[0:len(expression) - 1]
        self.label_result.config(text=expression)

    def calculate(self):  # cal the answer
        global expression
        result = ""
        if expression != "":
            try:
                result = eval(expression)
            except:
                result = "error"
                expression = ""
        self.label_result.config(text=result)
        expression = str(result)

    def key_handler(self, event):
        global expression
        if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            self.add(event.keysym)
        elif event.keysym == "parenleft":
            self.add("(")
        elif event.keysym == "parenright":
            self.add(")")
        elif event.keysym == "plus":
            self.add("+")
        elif event.keysym == "minus":
            self.add("-")
        elif event.keysym == "asterisk":
            self.add("*")
        elif event.keysym == "slash":
            self.add("/")
        elif event.keysym in ("c", "C"):
            self.clear()
        elif event.keysym == "period":
            self.add(".")
        elif event.keysym in ("Return", "equal"):
            self.calculate()
        elif event.keysym == "BackSpace":
            expression = expression[0:len(expression) - 1]
            self.label_result.config(text=expression)


class UnitConverterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "Unit Converter"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        # Main frame #################################
        self.frm_uc = tk.Frame(self, relief=tk.SUNKEN, borderwidth=3, bg=color['nero'])
        self.frm_uc.pack(side="top", fill="both", expand=1)
        # row 0:
        self.lbl_choose_unit = tk.Label(self.frm_uc, text="Choose Unit", font=("arial", 20, "bold"),
                                        height=3, bg=color['nero'], fg="white")
        self.lbl_choose_unit.grid(row=0, column=0)
        self.cmb_choose_unit = ttk.Combobox(self.frm_uc, width=20, state='readonly',
                                            values=('Length', 'Weight', 'Area', 'Volume', 'Velocity', 'Time',
                                                    'Temperature', 'Circle', 'Digital'))
        self.cmb_choose_unit.grid(row=0, column=1)
        self.cmb_choose_unit.bind("<<ComboboxSelected>>", self.UnitSelected)
        # row 1:
        self.lbl_from_unit = tk.Label(self.frm_uc, text="Converted From", font=("arial", 20, "bold"),
                                      height=3, bg=color['nero'], fg="white")
        self.lbl_from_unit.grid(row=1, column=0, padx=10)
        self.cmb_choose_from = ttk.Combobox(self.frm_uc, width=20, state='readonly')
        self.cmb_choose_from.grid(row=1, column=1)
        # row 2:
        self.lbl_amount_unit = tk.Label(self.frm_uc, text="Value", font=("arial", 20, "bold"),
                                        height=3, bg=color['nero'], fg="white")
        self.lbl_amount_unit.grid(row=2, column=0)
        self.entry_amount_unit = tk.Entry(self.frm_uc, width=20, font=("arial", 15, "bold"))
        self.entry_amount_unit.grid(row=2, column=1)
        # row 3:
        self.lbl_to_unit = tk.Label(self.frm_uc, text="Convert To", font=("arial", 20, "bold"),
                                    height=3, bg=color['nero'], fg="white")
        self.lbl_to_unit.grid(row=3, column=0)
        self.cmb_choose_to = ttk.Combobox(self.frm_uc, width=20, state='readonly')
        self.cmb_choose_to.grid(row=3, column=1)
        # row 4:
        self.lbl_result = tk.Label(self.frm_uc, text='Result', font=("arial", 20, "bold"),
                                        height=3, bg=color['nero'], fg="white")
        self.lbl_result.grid(row=4, column=0)
        self.lbl_result_unit = tk.Label(self.frm_uc, text='...........', font=("arial", 20, "bold"),
                                        height=3, bg=color['nero'], fg="white")
        self.lbl_result_unit.grid(row=4, column=1)
        # row 5:
        self.btn_convert = tkm.Button(self.frm_uc, text="CONVERT", font=("arial", 15, "bold"), cursor='star',
                                      bg=color['nero'], fg='white', activebackground='DimGrey', bd=5,
                                      relief=tk.RIDGE, borderwidth=3, command=lambda: self.Convert())
        self.btn_convert.grid(row=5, column=0, columnspan=2, pady=20)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  , fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()],
                                 anchor='w', )
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w', )
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w', )
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w', )
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True

    def UnitSelected(self, event):
        self.cmb_choose_from.set("")
        self.cmb_choose_to.set("")
        global unit_value
        unit_value = ()
        global convert_value
        convert_value = ()
        unit = self.cmb_choose_unit.get()
        if unit == "Length":
            unit_value = ('millimeter(mm)', 'centimeter(cm)', 'meter(m)', 'Kilometer(km)', 'inch(in)', 'foot(ft)',
                          'yard(yd)', 'mile', 'light year')
            convert_value = (1000, 100, 1, 0.001, 39.380, 3.281, 1.094, 0.000621, 1.057e-16)
        elif unit == "Weight":
            unit_value = ('gram(g)', 'Kilogram(kg)', 'ounce', 'pound')
            convert_value = (1000, 1, 35.27, 2.205)
        elif unit == "Area":
            unit_value = ('square centimeter(cm^2)', 'square meter(m^2)', 'square kilometer(km^2)', 'square inch(in^2)',
                          'square foot(ft^2)', 'square yard(yd^2)', 'square mile', 'hectare(ha)', 'acre')
            convert_value = (10000, 1, 0.000001, 1550, 10.764, 1.196, 3.861e-7, 0.0001, 0.000247)
        elif unit == "Volume":
            unit_value = ('cubic centimeter(cm^3)', 'cubie meter(m^3)', 'cubic inch(in^3)', 'cubic foot(ft^3)',
                          'cubic yard(yd^3)')
            convert_value = (1000000, 1, 61023.744, 35.315, 1.308)
        elif unit == "Velocity":
            unit_value = ('kilometer per hour(km/h)', 'meter per second(m/s)', 'miles per hour(mph)', 'knot(kn)')
            convert_value = (3.6, 1, 2.237, 1.94)
        elif unit == "Time":
            unit_value = ('millisecond(ms)', 'second(s)', 'minute(min)', 'hour(hr)', 'day', 'week', 'month', 'year')
            convert_value = (31557600000, 31557600, 525960, 8766, 365.25, 52.179, 12, 1)
        elif unit == "Temperature":
            unit_value = ('Celsius(C)', 'Fahrenheit(F)', 'Kelvins(K)')
            convert_value = (1, 1.8+32, +273.15)
        elif unit == "Circle":
            unit_value = ('radians(rad)', 'degrees(deg)')
            convert_value = (1, 57.296)
        elif unit == "Digital":
            unit_value = ('bit(bit)', 'byte(byte)', 'kilobyte(kB)', 'megabyte(MB)', 'gigabyte(GB)', 'terabyte(TB)')
            convert_value = (8388608, 1048576, 1024, 1, 0.0009765625, 9.536743164e-7)
        self.cmb_choose_from['values'] = unit_value
        self.cmb_choose_to['values'] = unit_value

    def Convert(self):
        from_unit = self.cmb_choose_from.get()
        to_unit = self.cmb_choose_to.get()
        value = float(self.entry_amount_unit.get())
        if from_unit == "Celsius(C)" and to_unit == 'Fahrenheit(F)':
            result = value*1.8+32
        elif from_unit == "Celsius(C)" and to_unit == 'Kelvins(K)':
            result = value+273.15
        elif to_unit == "Celsius(C)" and from_unit == 'Fahrenheit(F)':
            result = (value-32)/1.8
        elif to_unit == "Celsius(C)" and from_unit == 'Kelvins(K)':
            result = value-273.15
        elif from_unit == "Fahrenheit(F)" and to_unit == 'Kelvins(K)':
            result = (value-32)/1.8+273.15
        elif to_unit == "Fahrenheit(F)" and from_unit == 'Kelvins(K)':
            result = (value-273.15)*1.8+32
        else:
            result = value*(convert_value[unit_value.index(to_unit)]/convert_value[unit_value.index(from_unit)])
        self.lbl_result_unit.config(text=result)


class CurrencyConverterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "Currency Converter"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        self.time_from = tk.StringVar()
        self.time_to = tk.StringVar()
        self.h_result = tk.StringVar()
        # Realtime data #####
        self.url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.data = requests.get(self.url).json()
        self.currencies = self.data['rates']
        self.date = self.data['date']
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        # Main frame #################################
        self.c = CurrencyConverter(fallback_on_missing_rate=True, fallback_on_wrong_date=True)
        self.frm_cc = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_cc.pack(side="top", fill="both", expand=1)
        # historical rates ######
        self.frm_choose = tk.Frame(self.frm_cc, relief=tk.SUNKEN, borderwidth=1, bg=color['nero'])
        self.frm_choose.pack(side="top", fill="both", expand=0)
        ###
        self.lbl_date = tk.Label(self.frm_choose, text="Historical Rates", font=("arial", 25, "bold"),
                                 bg=color['nero'], fg='white')
        self.lbl_date.grid(row=0, column=0, columnspan=2, padx=80, pady=5)
        ###
        self.lbl_choose = tk.Label(self.frm_choose, text="Choose to check:", font=("arial", 20, "bold"),
                                   height=1, bg=color['nero'], fg="white")
        self.lbl_choose.grid(row=1, column=0, padx=0, pady=4)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.c_value = ('KRW', 'LTL', 'PLN', 'HKD', 'ROL', 'EUR', 'USD', 'CNY', 'MXN', 'SGD', 'ILS', 'INR',
                        'CYP', 'HUF', 'ISK', 'PHP', 'IDR', 'AUD', 'NZD', 'MTL', 'THB', 'LVL', 'CAD', 'HRK',
                        'TRY', 'BGN', 'BRL', 'SKK', 'RON', 'GBP', 'RUB', 'TRL', 'MYR', 'EEK', 'CZK', 'ZAR',
                        'DKK', 'CHF', 'JPY', 'SEK', 'NOK', 'SIT')
        self.cmb_choose = ttk.Combobox(self.frm_choose, values=self.c_value, width=10, state='readonly')
        self.cmb_choose.grid(row=1, column=1, pady=4)
        self.cmb_choose.bind("<<ComboboxSelected>>", self.ValueSelect)
        self.cmb_choose.set("Currency")
        ###
        self.lbl_from = tk.Label(self.frm_choose, text="Available from:", font=("arial", 20, "bold"),
                                 height=1, bg=color['nero'], fg="white")
        self.lbl_from.grid(row=2, column=0, pady=4)
        self.lbl_to = tk.Label(self.frm_choose, text="Available to:", font=("arial", 20, "bold"),
                               height=1, bg=color['nero'], fg="white")
        self.lbl_to.grid(row=3, column=0, pady=4)
        self.lbl_from_time = tk.Label(self.frm_choose, textvariable=self.time_from, font=("times", 20, "bold"),
                                      height=1, bg=color['nero'], fg="white")
        self.lbl_from_time.grid(row=2, column=1, sticky="W", pady=4)
        self.lbl_to_time = tk.Label(self.frm_choose, textvariable=self.time_to, font=("times", 20, "bold"),
                                    height=1, bg=color['nero'], fg="white")
        self.lbl_to_time.grid(row=3, column=1, sticky="W", pady=4)
        # frm_2 #####
        self.frm_2 = tk.Frame(self.frm_choose, bg=color['nero'])
        self.frm_2.grid(row=4, column=0, columnspan=2)
        self.lbl_money_from = tk.Label(self.frm_2, text="  From", font=("arial", 20, "bold"),
                                       bg=color['nero'], fg='white')
        self.lbl_money_from.grid(row=0, column=0, pady=5)
        self.cmb_money_from = ttk.Combobox(self.frm_2, values=self.c_value, width=9, state='readonly')
        self.cmb_money_from.grid(row=0, column=1, pady=5)
        self.lbl_money_to = tk.Label(self.frm_2, text="  To  ", font=("arial", 20, "bold"),
                                     bg=color['nero'], fg='white')
        self.lbl_money_to.grid(row=0, column=2, pady=5)
        self.cmb_money_to = ttk.Combobox(self.frm_2, values=self.c_value, width=9, state='readonly')
        self.cmb_money_to.grid(row=0, column=3, pady=5)
        self.lbl_date = tk.Label(self.frm_2, text="  Date", font=("arial", 20, "bold"),
                                 bg=color['nero'], fg='white')
        self.lbl_date.grid(row=1, column=0, pady=5)
        self.entry_date = tk.Entry(self.frm_2, width=15, font=("arial", 15, "bold"))
        self.entry_date.grid(row=1, column=1, columnspan=3, pady=5)
        self.entry_date.insert(0, "yyyy-mm-dd")
        self.entry_date.bind("<FocusIn>", self.on_entry_click)
        self.entry_date.bind("<FocusOut>", self.on_focusout)
        self.lbl_amount = tk.Label(self.frm_2, text="Amount", font=("arial", 20, "bold"),
                                   bg=color['nero'], fg='white')
        self.lbl_amount.grid(row=2, column=0, pady=5)
        self.entry_amount = tk.Entry(self.frm_2, width=15, font=("arial", 15, "bold"))
        self.entry_amount.grid(row=2, column=1, columnspan=3, pady=5)
        self.lbl_result_t = tk.Label(self.frm_2, text='Result', font=("arial", 20, "bold"),
                                     bg=color['nero'], fg="white")
        self.lbl_result_t.grid(row=3, column=0, pady=5)
        self.lbl_result = tk.Label(self.frm_2, text='Waiting...', font=("arial", 20, "bold"),
                                   bg=color['nero'], fg="white")
        self.lbl_result.grid(row=3, column=1, columnspan=3, pady=5)
        self.btn_convert = tkm.Button(self.frm_2, text="CONVERT", font=("arial", 15, "bold"), cursor='star', bd=5,
                                      bg=color['nero'], fg='white', activebackground='DimGrey',
                                      relief=tk.RIDGE, borderwidth=3, command=lambda: self.convert_fn())
        self.btn_convert.grid(row=4, column=0, columnspan=4, pady=5)

        # real time rates ######
        self.frm_realtime = tk.Frame(self.frm_cc, relief=tk.SUNKEN, borderwidth=1, bg=color['nero'])
        self.frm_realtime.pack(side="top", fill="both", expand=1)
        self.lbl_real = tk.Label(self.frm_realtime, text="Real Time Rates", font=("arial", 25, "bold"),
                                 bg=color['nero'], fg='white')
        self.lbl_real.grid(row=0, column=0, columnspan=4, padx=80, pady=5)
        self.lbl_real_from = tk.Label(self.frm_realtime, text="  From", font=("arial", 20, "bold"),
                                      bg=color['nero'], fg='white')
        self.lbl_real_from.grid(row=1, column=0, pady=5)
        self.cmb_real_from = ttk.Combobox(self.frm_realtime,
                                          values=list(self.currencies.keys()), width=9, state='normal')
        self.cmb_real_from.grid(row=1, column=1, pady=5)
        self.lbl_real_to = tk.Label(self.frm_realtime, text="To", font=("arial", 20, "bold"),
                                    bg=color['nero'], fg='white')
        self.lbl_real_to.grid(row=1, column=2, pady=5)
        self.cmb_real_to = ttk.Combobox(self.frm_realtime,
                                        values=list(self.currencies.keys()), width=9, state='normal')
        self.cmb_real_to.grid(row=1, column=3, pady=5)
        self.lbl_real_date = tk.Label(self.frm_realtime, text="  Date", font=("arial", 20, "bold"),
                                      bg=color['nero'], fg='white')
        self.lbl_real_date.grid(row=2, column=0, pady=5)
        self.lbl_real_date_today = tk.Label(self.frm_realtime, text=self.date, font=("arial", 20, "bold"),
                                            bg=color['nero'], fg='white')
        self.lbl_real_date_today.grid(row=2, column=1, columnspan=3, pady=5)
        self.lbl_real_amount = tk.Label(self.frm_realtime, text="Amount", font=("arial", 20, "bold"),
                                        bg=color['nero'], fg='white')
        self.lbl_real_amount.grid(row=3, column=0, pady=5)
        self.entry_real_amount = tk.Entry(self.frm_realtime, width=15, font=("arial", 15, "bold"))
        self.entry_real_amount.grid(row=3, column=1, columnspan=3, pady=5)
        self.lbl_real_result_t = tk.Label(self.frm_realtime, text='Result', font=("arial", 20, "bold"),
                                          bg=color['nero'], fg="white")
        self.lbl_real_result_t.grid(row=4, column=0, pady=5)
        self.lbl_real_result = tk.Label(self.frm_realtime, text='Waiting...', font=("arial", 20, "bold"),
                                        bg=color['nero'], fg="white")
        self.lbl_real_result.grid(row=4, column=1, columnspan=3, pady=5)
        self.btn_real_convert = tkm.Button(self.frm_realtime, text="CONVERT", font=("arial", 15, "bold"), cursor='star',
                                           bg=color['nero'], fg='white', activebackground='DimGrey', bd=5,
                                           relief=tk.RIDGE, borderwidth=3, command=lambda: self.convert())
        self.btn_real_convert.grid(row=5, column=0, columnspan=4, pady=5)

        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  ,fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()], anchor='w',)
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w',)
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w',)
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w',)
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True

    def on_entry_click(self, event):
        if self.entry_date.get() == 'yyyy-mm-dd':
            self.entry_date.delete(0, "end")  # delete all the text in the entry
            self.entry_date.insert(0, '')  # Insert blank for user input

    def on_focusout(self, event):
        if self.entry_date.get() == '':
            self.entry_date.insert(0, 'yyyy-mm-dd')

    def ValueSelect(self, event):
        global money
        money = self.cmb_choose.get()
        f, t = self.c.bounds[money]
        self.time_from.set(f)
        self.time_to.set(t)

    def convert_fn(self):
        try:
            from_ = self.cmb_money_from.get()
            to_ = self.cmb_money_to.get()
            amount_ = self.entry_amount.get()
            date_ = self.entry_date.get()
            date_y = int(date_[0:4])
            date_m = int(date_[5:7])
            date_d = int(date_[8:10])
            result = round(self.c.convert(amount_, from_, to_, date=date(date_y, date_m, date_d)), 4)
            self.lbl_result.config(text=result)
        except:
            self.lbl_result.config(text="Wrong Date Format")

    def convert(self):  # Real time converter
        amount = float(self.entry_real_amount.get())
        from_currency = self.cmb_real_from.get()
        to_currency = self.cmb_real_to.get()
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        self.lbl_real_result.config(text=amount)


class ToDoList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "ToDoList"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        # ToDoList ##################################
        self.frm_tdl = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_tdl.pack(side="top", fill="both", expand=1)
        self.frm_top = tk.Frame(self.frm_tdl, relief=tk.SUNKEN, borderwidth=1, bg=color['nero'])
        self.frm_top.pack(side="top", fill="x", expand=0)
        self.listbox_tasks = tkinter.Listbox(self.frm_top, height=11, font=('arial', 20, 'bold'),
                                             bg=color['nero'], fg='white', selectbackground='DimGray')
        self.listbox_tasks.pack(side=tkinter.LEFT, fill='x', expand=1)
        self.scrollbar_tasks = tkinter.Scrollbar(self.frm_top)
        self.scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)
        self.entry_task = tkinter.Entry(self.frm_tdl, font=('arial', 15, 'bold'), bg=color['nero'], fg='white', bd=3,
                                        selectbackground='DimGray')
        self.entry_task.pack(fill=tk.X)
        self.entry_task.insert(0, "Enter your task here :)")
        self.entry_task.bind("<FocusIn>", self.on_entry_click)
        self.entry_task.bind("<FocusOut>", self.on_focusout)
        self.button_add_task = tkm.Button(self.frm_tdl, text="Add task", command=self.add_task,
                                          font=('arial', 15, 'bold'), relief=tk.RIDGE, borderwidth=3,
                                          bg=color['nero'], fg='white', activebackground='DimGray')
        self.button_add_task.pack(pady=15)
        self.button_delete_task = tkm.Button(self.frm_tdl, text="Delete task", command=self.delete_task,
                                             font=('arial', 15, 'bold'), relief=tk.RIDGE, borderwidth=3,
                                             bg=color['nero'], fg='white', activebackground='DimGray')
        self.button_delete_task.pack(pady=15)
        self.button_clear_tasks = tkm.Button(self.frm_tdl, text="Clear tasks", command=self.clear_tasks,
                                             font=('arial', 15, 'bold'), relief=tk.RIDGE, borderwidth=3,
                                             bg=color['nero'], fg='white', activebackground='DimGray')
        self.button_clear_tasks.pack(pady=15)
        self.button_load_tasks = tkm.Button(self.frm_tdl, text="Load tasks", command=self.load_tasks,
                                            font=('arial', 15, 'bold'), relief=tk.RIDGE, borderwidth=3,
                                            bg=color['nero'], fg='white', activebackground='DimGray')
        self.button_load_tasks.pack(pady=15)
        self.button_save_tasks = tkm.Button(self.frm_tdl, text="Save tasks", command=self.save_tasks,
                                            font=('arial', 15, 'bold'), relief=tk.RIDGE, borderwidth=3,
                                            bg=color['nero'], fg='white', activebackground='DimGray')
        self.button_save_tasks.pack(pady=15)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  , fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()],
                                 anchor='w', )
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                  fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w', )
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w', )
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w', )
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            self.listbox_tasks.insert(tkinter.END, task)
            self.entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

    def load_tasks(self):
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            self.listbox_tasks.delete(0, tk.END)
            for task in tasks:
                self.listbox_tasks.insert(tk.END, task)
        except:
            tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

    def save_tasks(self):
        tasks = self.listbox_tasks.get(0, self.listbox_tasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))

    def clear_tasks(self):
        self.listbox_tasks.delete(0, tk.END)

    def on_entry_click(self, event):
        if self.entry_task.get() == 'Enter your task here :)':
            self.entry_task.delete(0, "end")  # delete all the text in the entry
            self.entry_task.insert(0, '')  # Insert blank for user input

    def on_focusout(self, event):
        if self.entry_task.get() == '':
            self.entry_task.insert(0, 'Enter your task here :)')


class PasswordManager(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "Password Manager"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        #############################################
        self.frm_pwm = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_pwm.pack(side="top", fill="both", expand=1)
        self.lbl_1 = tk.Label(self.frm_pwm, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Welcome to Password Manager!', height=3)
        self.lbl_2 = tk.Label(self.frm_pwm, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Developed by WIN Sama.', height=3)
        self.lbl_3 = tk.Label(self.frm_pwm, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Link to Github:', height=3)
        self.lbl_1.pack(side='top')
        self.lbl_2.pack(side='top')
        self.lbl_3.pack(side='top')
        self.btn_gh = tkm.Button(self.frm_pwm, text='GITHUB', command=self.Web, bg=color['nero'], fg='white',
                                  font=('arial', 25, 'bold'), activebackground='DimGray')
        self.btn_gh.pack(pady=10)
        self.btn_win = tkm.Button(self.frm_pwm, text='START', command=self.Call, bg=color['nero'], fg='white',
                                  font=('arial', 25, 'bold'), activebackground='DimGray')
        self.btn_win.pack(pady=10)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  ,fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()], anchor='w',)
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w',)
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w',)
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w',)
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True

    def Call(self):
        reload(win)
        win.start()

    def Web(self):
        webbrowser.open(
            'https://github.com/winnimrawee/programming-practice-2021/tree/exercises/1TE19248G%20Coding%20Project')


class GamesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "GAMES"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        #############################################
        self.frm_game = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_game.pack(side="top", fill="both", expand=1)
        self.lbl_1 = tk.Label(self.frm_game, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Welcome to Math Fighter', height=3)
        self.lbl_2 = tk.Label(self.frm_game, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Developed by Champ Sama.', height=3)
        self.lbl_3 = tk.Label(self.frm_game, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                              text='Link to Github:', height=3)
        self.lbl_1.pack(side='top')
        self.lbl_2.pack(side='top')
        self.lbl_3.pack(side='top')
        self.btn_gh = tkm.Button(self.frm_game, text='GITHUB', bg=color['nero'], fg='white',
                                  font=('arial', 25, 'bold'), activebackground='DimGray')
        self.btn_gh.pack(pady=10)
        self.btn_cp = tkm.Button(self.frm_game, text='START', bg=color['nero'], fg='white',
                                 font=('arial', 25, 'bold'), activebackground='DimGray')
        self.btn_cp.pack(pady=10)
        self.lbl_cp = tk.Label(self.frm_game, font=('arial', 20, 'bold'), bg=color['nero'], fg='white',
                               text='Waiting for champ to finish :(', height=3)
        self.lbl_cp.pack(side='top')
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  ,fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()], anchor='w',)
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w',)
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w',)
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w',)
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_name = "HELP"
        self.icon_menu = PhotoImage(file="menu.png")
        self.icon_close = PhotoImage(file="close.png")
        # Title ####################################
        self.frm_top = tk.Frame(master=self, bg=color["orange"])  # orange
        self.frm_top.pack(side="top", fill=tk.X)
        self.lbl_title = tk.Label(master=self.frm_top, text=self.title_name, bg=color['orange'],
                                  font=("times", 30, "bold italic"), height=2)
        self.lbl_title.pack(side="top", fill=tk.X)
        self.btn_menu = tkm.Button(master=self.frm_top, image=self.icon_menu, bg=color["orange"], fg=color["orange"],
                                   bd=5, cursor="star", activebackground=color["orange"], padx=0, command=self.Switch)
        self.btn_menu.place(x=0, y=13)
        #############################################
        self.frm_help = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2, bg=color['nero'])
        self.frm_help.pack(side="top", fill="both", expand=1)
        self.lbl_1 = tk.Label(self.frm_help, text='Welcome to Desktop Assistant.', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.lbl_2 = tk.Label(self.frm_help, text='Developed by Yiluo.', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.lbl_3 = tk.Label(self.frm_help, text='This desktop app is for daily use.', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.lbl_4 = tk.Label(self.frm_help, text='Use Navbar to choose applications.', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.lbl_5 = tk.Label(self.frm_help, text='Version: 1.0.0', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.lbl_6 = tk.Label(self.frm_help, text='For more information:', font=('arial', 20, 'bold'),
                              bg=color['nero'], fg='white', height=2)
        self.btn_1 = tkm.Button(self.frm_help, text='GITHUB', bg=color['nero'], fg='white',
                                font=('arial', 25, 'bold'), activebackground='DimGray')
        self.lbl_1.pack(side='top', anchor='w')
        self.lbl_2.pack(side='top', anchor='w')
        self.lbl_3.pack(side='top', anchor='w')
        self.lbl_4.pack(side='top', anchor='w')
        self.lbl_5.pack(side='top', anchor='w')
        self.lbl_6.pack(side='top', anchor='w')
        self.btn_1.pack(side='top', pady=10)
        # Navbar ####################################
        self.frm_left = tk.Frame(master=self, bg='DimGray', height=1000, width=300)
        self.frm_left.place(x=-300, y=0)
        tk.Label(master=self.frm_left, text="Navbar", font=("times", 30, "bold italic"), bg="SandyBrown",
                 fg="black", height=2, width=25, padx=20).place(x=-110, y=0)
        self.btn_home = tkm.Button(self.frm_left, text="Home", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                   fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                   command=lambda: [controller.show_frame(HomePage), self.Switch()])
        self.btn_home.place(x=25, y=90)  # home button
        self.btn_cal = tkm.Button(self.frm_left, text="Calculator", font=('arial', 20, 'bold'), bg="DimGray", anchor='w'
                                  ,fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                  command=lambda: [controller.show_frame(CalculatorPage), self.Switch()])
        self.btn_cal.place(x=25, y=140)  # cal button
        self.btn_uc = tkm.Button(self.frm_left, text="Unit Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(UnitConverterPage), self.Switch()], anchor='w',)
        self.btn_uc.place(x=25, y=190)  # uc button
        self.btn_cc = tkm.Button(self.frm_left, text="Currency Converter", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(CurrencyConverterPage), self.Switch()],
                                 anchor='w')
        self.btn_cc.place(x=25, y=240)  # cc button
        self.btn_tdl = tkm.Button(self.frm_left, text="ToDoList", font=('arial', 20, 'bold'), bg="DimGray", anchor='w',
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(ToDoList), self.Switch()])
        self.btn_tdl.place(x=25, y=290)  # tdl button
        self.btn_pwm = tkm.Button(self.frm_left, text="Password Manager", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(PasswordManager), self.Switch()], anchor='w',)
        self.btn_pwm.place(x=25, y=340)  # pwm button
        self.btn_game = tkm.Button(self.frm_left, text="Games", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(GamesPage), self.Switch()], anchor='w',)
        self.btn_game.place(x=25, y=390)  # game button
        self.btn_help = tkm.Button(self.frm_left, text="Help", font=('arial', 20, 'bold'), bg="DimGray",
                                 fg=color["orange"], activebackground="DimGray", activeforeground="green", bd=3,
                                 command=lambda: [controller.show_frame(HelpPage), self.Switch()], anchor='w',)
        self.btn_help.place(x=25, y=440)  # help button
        self.btn_close = tkm.Button(self.frm_left, image=self.icon_close, bg="SandyBrown", cursor="star",
                                    activebackground="SandyBrown", bd=5, padx=0, command=self.Switch)
        self.btn_close.place(x=220, y=13)

    def Switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            x = 0
            while True:
                self.frm_left.place(x=-x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 320:
                    break
            btnState = False
        else:
            x = -300
            while True:
                self.frm_left.place(x=x, y=0)
                self.frm_left.update()
                self.frm_top.update()
                x += 20
                if x == 20:
                    break
            btnState = True


app = tkinterApp()
app.minsize(400, 700)
app.config(bg=color["nero"])
app.title("Desktop Assistant by Yiluo")
app.mainloop()