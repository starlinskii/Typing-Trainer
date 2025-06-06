from field import Field
from tkinter import Label, E, W, N, S, Button, CENTER, TclError
import random
import Sources as src

class Interface:

    fld : Field

    def __init__(self):
        self.fld = Field()
    
    def Renew(self):
        self.fld.txt = random.choice(src.Texts)
        
        self.fld.current_pos = 0
        self.fld.gray_text = Label(self.fld.program, text=self.fld.txt[0:self.fld.current_pos], fg='grey')
        self.fld.gray_text.place(relx=0.5, rely=0.5, anchor=E)

        self.fld.black_text = Label(self.fld.program, text=self.fld.txt[self.fld.current_pos:])
        self.fld.black_text.place(relx=0.5, rely=0.5, anchor=W)
        
        self.fld.current_letter = Label(self.fld.program, text=self.fld.txt[self.fld.current_pos], fg='grey')
        self.fld.current_letter.place(relx=0.5, rely=0.6, anchor=N)

        self.fld.timer = Label(self.fld.program, text=f'0 Seconds', fg='grey')
        self.fld.timer.place(relx=0.5, rely=0.4, anchor=S)

        self.fld.mutex = True
        self.fld.program.bind('<Key>', self.keyPress)
        self.fld.seconds = 0
        self.fld.program.after(60000, self.Stop)
        self.fld.program.after(1000, self.Tick)

    def Stop(self):
        self.fld.mutex = False
        cnt_of_words = len(self.fld.gray_text.cget('text').split(' '))

        self.fld.timer.destroy()
        self.fld.current_letter.destroy()
        self.fld.black_text.destroy()
        self.fld.gray_text.destroy()

        self.fld.speed = Label(self.fld.program, text=f'Words per Minute: {cnt_of_words / self.fld.seconds * 60}', fg='black')
        self.fld.speed.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.fld.restarter = Button(self.fld.program, text=f'Retry', command=self.Restart)
        self.fld.restarter.place(relx=0.5, rely=0.6, anchor=CENTER)
        
    def Tick(self):
        if not self.fld.mutex:
            return
        self.fld.seconds += 1
        self.fld.timer.configure(text=f'{self.fld.seconds} Seconds')
        self.fld.program.after(1000, self.Tick)
    
    def Restart(self):
        self.fld.speed.destroy()
        self.fld.restarter.destroy()
        self.Reset()

    def Reset(self):
        self.Renew()
    
    def keyPress(self, event=None):
        try:
            if event.char == self.fld.black_text.cget('text')[0]:
                if len(self.fld.black_text.cget('text')) == 1:
                    txt=''
                    self.fld.gray_text.configure(text=self.fld.gray_text.cget('text') + event.char)
                    self.Stop()
                else:
                    self.fld.black_text.configure(text=self.fld.black_text.cget('text')[1:])
                    self.fld.gray_text.configure(text=self.fld.gray_text.cget('text') + event.char)
                    self.fld.current_letter.configure(text=self.fld.black_text.cget('text')[0])
        except TclError:
            pass
