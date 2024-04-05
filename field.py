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

