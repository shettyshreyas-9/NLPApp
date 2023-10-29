# library for guis
from tkinter import *
from mydb import DataBase
from tkinter import messagebox
import os
import json

from myapi import API

class NLPApp:
    def __init__(self):

        # create db object
        self.dbo = DataBase()

        # create api object
        self.apio = API()

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
        login_btn = Button(self.root,text='Login',width=15,height=2, command=self.perform_login)
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


    def perform_login(self):
        email= self.email_input.get()
        password= self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        # For Heading
        heading= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        # Button for Sentiment analysis
        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        # Button for Named Entity Recognition
        ner_btn = Button(self.root,text='Named Entity Recognition',width=30,height=4,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))

        # Button for Emotion Prediction
        emotion_btn = Button(self.root,text='Emotion Prediction',width=30,height=4,command=self.perform_registration)
        emotion_btn.pack(pady=(10,10))

        # Button for Logout
        logout_btn = Button(self.root,text='Logout',width=15,height=2,command=self.login_gui)
        logout_btn.pack(pady=(10,10))


    # sentiment GUI section
    def sentiment_gui(self):
        self.clear()

        # For Heading
        heading1= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana',24,'bold'))

        # For Heading
        heading2= Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading2.pack(pady=(20,20))
        heading2.configure(font=('verdana',15))

        # For entering text
        label1 = Label(self.root,text='Enter the text:')
        label1.pack(pady=(15,15))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=35)

        sentiment_pred_btn = Button(self.root,text='Analyze Sentiment',width=15,height=2, command=self.do_sentiment_analysis)
        sentiment_pred_btn.pack(pady=(10,10))

        # result
        self.sentiment_result = Label(self.root,text='',bg='#344952',fg='white')
        self.sentiment_result.pack(pady=(15,15))
        self.sentiment_result.configure(font=('verdana',15))

        goback_btn = Button(self.root,text='Go back',width=10,height=2,command=self.home_gui)
        goback_btn.pack(pady=(15,15))



    def ner_gui(self):
        self.clear()

        # For Heading
        heading1= Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana',24,'bold'))

        # For Heading
        heading2= Label(self.root,text='Named Entity Recognition',bg='#34495E',fg='white')
        heading2.pack(pady=(20,20))
        heading2.configure(font=('verdana',15))

        # For entering text
        label1 = Label(self.root,text='Enter the text:')
        label1.pack(pady=(15,15))

        self.ner_input = Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=35)

        ner_pred_btn = Button(self.root,text='Recognize Entity',width=15,height=2, command=self.do_ner)
        ner_pred_btn.pack(pady=(10,10))

        # result
        self.ner_result = Label(self.root,text='',bg='#344952',fg='white')
        self.ner_result.pack(pady=(15,15))
        self.ner_result.configure(font=('verdana',15))

        goback_btn = Button(self.root,text='Go back',width=10,height=2,command=self.home_gui)
        goback_btn.pack(pady=(15,15))



    def do_sentiment_analysis(self):
        text= self.sentiment_input.get()
        # print(text)
        result=self.apio.sentiment_analysis(text)
        print(result)

        txt=''
        for i in result['sentiment']:
            txt= txt + i+ '->' + str(result['sentiment'][i]) + '\n'
            # print(i,':',result['sentiment'][i])

        self.sentiment_result['text'] = txt



    def do_ner(self):
        text= self.ner_input.get()
        # print(text)
        result=self.apio.named_entity_recognition(text)
        print(result)

        txt=''
        for entity in result['entities']:
            txt= txt+ "name:"+ entity['name']+ '\n'
            txt= txt+ "category:"+ entity['category']+ '\n'
            txt= txt+ "confidence_score:"+ str(entity['confidence_score'])+ '\n'+'\n'

        print(txt)
        self.ner_result['text'] = txt



nlp= NLPApp()
