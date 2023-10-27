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
        # For Heading
        heading= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        # For Email

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,10),ipady=4)

        # For password

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=40,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        # Button for login
        login_btn = Button(self.root,text='Login',width=15,height=2)
        login_btn.pack(pady=(10,10))

        # For Registering

        # label3 = Label(self.root,text='Not a member?')
        # label3.pack(pady=(20,10))
        redirect_btn = Button(self.root,text='Register')
        redirect_btn.pack(pady=(20,10))



nlp= NLPApp()
