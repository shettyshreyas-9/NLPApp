# library for guis
from tkinter import *


class NLPApp:
    def __init__(self):
        # load gui of login
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/luffy_fev.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        heading= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))


nlp= NLPApp()
