from dataclasses import dataclass
from enum import Enum
from collections import namedtuple
from random import seed, shuffle
from itertools import product
import random
import copy
from itertools import product
from tkinter import *
import ctypes
import random
import tkinter
import Sources as src

@dataclass
class Field:

    program : tkinter
    txt : str

    def __init__(self):
        #создали новый ткинтэр
        self.program = Tk()
        #заголовок, размер окна, шрифт
        self.program.title('Type Speed Test')
        self.program.geometry('700x700')
        self.program.option_add("*Label.Font", "consolas 30")
        self.program.option_add("*Button.Font", "consolas 30")
        self.txt = random.choice(src.Texts)
        
        self.current_pos = 0
        self.gray_text = Label(self.program, text=self.txt[0:self.current_pos], fg='grey')
        self.gray_text.place(relx=0.5, rely=0.5, anchor=E)

        self.black_text = Label(self.program, text=self.txt[self.current_pos:])
        self.black_text.place(relx=0.5, rely=0.5, anchor=W)
        
        self.current_letter = Label(self.program, text=self.txt[self.current_pos], fg='grey')
        self.current_letter.place(relx=0.5, rely=0.6, anchor=N)

        self.timer = Label(self.program, text=f'0 Seconds', fg='grey')
        self.timer.place(relx=0.5, rely=0.4, anchor=S)


        self.mutex = True
        self.program.bind('<Key>', self.keyPress)
        self.seconds = 0
