# library for guis
from tkinter import *


class NLPApp:
    def __init__(self):
        # load gui of login
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/luffy_fev.ico')
        self.root.mainloop()


nlp= NLPApp()
