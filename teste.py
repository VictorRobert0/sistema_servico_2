#PROJETO DE ESTUDO PARA INTEGRAR BANCO DE DADOS SQLITE3 NO APP EXE

import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

#----------------------------------------------------------------------------------------------------------

app = ctk.CTk()

app.title('Tela de login')

app.geometry('470x360')

app.config(bg='#001220')

font1 = ('Helvetica', 25,'bold')
font2 = ('Arial', 17,'bold')
font3 = ('Arial', 13,'bold')
font4 = ('Arial', 13,'bold', 'underline')

#----------------------------------------------------------------------------------------------------------
#Conexão com banco de dados sqLITE3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users (
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL )''')


#---------------------------------------------------
#FUNÇÃO DE CADASTRO

def signup():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    if username != '' and email != '' and password != '':
        cursor.execute('SELECT  username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Usuário já existe.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute ('INSERT INTO users VALUES (?,?,?)', [username,email ,hashed_password])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Conta criada com sucesso ;)')
    else:
        messagebox.showerror('Erro', 'Por favor, insira todos os dados.')
                    

#----------------------------------------------------------------------------------------------------------
#FRONT-END

frame1 = ctk.CTkFrame(master=app, bg_color='#001220', fg_color='#001220',width=470,height=360)
frame1.place(x=0,y=0)

image1= PhotoImage(file="background.png")
image1_label = Label(frame1, image=image1, bg='#001220')
image1_label.place(x=0,y=0)
#----------------------------------------------------------------------------------------------------------

signup_label = ctk.CTkLabel(frame1, font=font1, text='Cadastrar-se', text_color='#fff', bg_color='#001220')
signup_label.place(x=280,y=20)

#----------------------------------------------------------------------------------------------------------
#ENTRYS ----USERS AND PASSWORDS

username_entry =  ctk.CTkEntry(frame1, font=font2, text_color='#fff',fg_color='#001a2e' ,bg_color='#121111', border_color='#004780', border_width=3,placeholder_text='Digite seu username..', placeholder_text_color='#a3a3a3',corner_radius=5 ,width=200,height=50)
username_entry.place(x=230,y=80)

email_entry= ctk.CTkEntry(frame1,font=font2, text_color='#fff',fg_color='#001a2e' ,bg_color='#121111', border_color='#004780', border_width=3,placeholder_text='Digite seu email.', placeholder_text_color='#a3a3a3',corner_radius=5 ,width=200,height=50)
email_entry.place(x=230,y=150)


password_entry = ctk.CTkEntry(frame1, font=font2, show="*", text_color='#fff',fg_color='#001a2e', bg_color='#121111', border_color='#004780',border_width=3, placeholder_text='Digite sua senha..', placeholder_text_color='#a3a3a3', corner_radius=5 ,width=200, height=50)
password_entry.place(x=230,y=230)


signup_button= ctk.CTkButton(frame1, command=signup ,font=font2,text_color='#fff', text='Cadastrar-se', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
signup_button.place(x=230,y=320)



login_label = ctk.CTkLabel(frame1, font=font3, text='Já possui uma conta?', text_color='#fff', bg_color='#001220')
login_label.place(x=230,y=250 )

login_button = ctk.CTkButton(frame1, font=font4, text_color='#00bf77', text='ENTRAR', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
login_button.place(x=395,y=250)
















app.mainloop() 

 