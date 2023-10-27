# library for guis
from tkinter import *
from mydb import DataBase
from tkinter import messagebox

class NLPApp:
    def __init__(self):

        # create db object
        self.dbo = DataBase()

        # load gui of login
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/luffy_fev.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):

        self.clear()

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
        redirect_now_btn = Button(self.root,text='Register Now', command= self.register_gui)
        redirect_now_btn.pack(pady=(20,10))

    # command used to redirect
    def register_gui(self):
        self.clear()

        # For Heading
        heading= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        # For Name

        label0 = Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=40)
        self.name_input.pack(pady=(5,10),ipady=4)

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

        # Button for Register
        register_btn = Button(self.root,text='Register',width=15,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        # For Registering

        # label3 = Label(self.root,text='Not a member?')
        # label3.pack(pady=(20,10))
        login_redirect_btn = Button(self.root, text='Login Here',command=self.login_gui)
        login_redirect_btn.pack(pady=(20,10))


    # clearing screen function
    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from gui
        name= self.name_input.get()
        email= self.email_input.get()
        password= self.password_input.get()
        print(name)

        response = self.dbo.add_data(name,email,password)

        if response:
            # print('Registration successful')
            messagebox.showinfo('Success','Registration success. You can login now')
        else:
            # print('email exists')
            messagebox.showinfo('Error','Email already exists')

nlp= NLPApp()
