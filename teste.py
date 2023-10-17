#PROJETO DE ESTUDO PARA INTEGRAR BANCO DE DADOS SQLITE3 NO APP EXE

import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

#----------------------------------------------------------------------------------------------------------

app = ctk.CTk()

app.title('Tela de cadastro')

app.geometry('470x360')

app.config(bg='#001220')

font1 = ('Helvetica',25,'bold')
font2 = ('Arial', 17,'bold')
font3 = ('Arial', 13,'bold')
font4 = ('Arial', 13,'bold')

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
#---------------------------------------------------------------------------------------------------------    
#TELA DE LOGIN
def login():
    frame1.destroy()
    frame2 = ctk.CTkFrame(master=app, bg_color='#001220', fg_color='#001220',width=470,height=360)
    frame2.place(x=0,y=0)
    
    image1= PhotoImage(file='background.png')
    image1_label = Label(frame2, image=image1)
    image1_label.place(x=0,y=0)
    frame2.image1 = image1
    
    
    
    login_label2 = ctk.CTkLabel(frame2, font=font1, text= 'Área de login', text_color='#fff', bg_color='#001222')
    login_label2.place(relx=0.35,rely=0.12)
    
    
    global username_entry2
    global password_entry2
    
    
    username_entry2 = ctk.CTkEntry(master=frame2, font=font2, text_color='#fff', fg_color='#001a2e', placeholder_text='Digite seu usuário...', width=200)
    username_entry2.place(relx=0.3 , rely= 0.3)
    
    password_entry2 = ctk.CTkEntry(master=frame2, font=font2, text_color='#fff', fg_color='#001a2e', placeholder_text='Digite sua senha...', width=200)
    password_entry2.place(relx=0.3, rely= 0.5)
    
    login_button2= ctk.CTkButton(master=frame2,font=font2,text_color='#fff', text='Entrar', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=200)
    login_button2.place(relx=0.3,rely=0.8)
            
        
        
        
        
            
                    

#----------------------------------------------------------------------------------------------------------
#FRONT-END | TELA CADASTRO

frame1 = ctk.CTkFrame(master=app, bg_color='#001220', fg_color='#001220',width=470,height=360)
frame1.place(x=0,y=0)

image1= PhotoImage(file="background.png")
image1_label = Label(frame1, image=image1, bg='#001220')
image1_label.place(x=0,y=0)
#----------------------------------------------------------------------------------------------------------

signup_label = ctk.CTkLabel(frame1, font=font1, text='Cadastrar-se', text_color='#fff', bg_color='#001220')
signup_label.place(relx=0.35,rely=0.1)

#----------------------------------------------------------------------------------------------------------
#ENTRYS ----USERS AND PASSWORDS

username_entry =  ctk.CTkEntry(frame1, font=font2, text_color='#fff',fg_color='#001a2e' ,bg_color='#121111', border_color='#004780', border_width=3,placeholder_text='Digite seu username..', placeholder_text_color='#a3a3a3',corner_radius=5 ,width=200)
username_entry.place(relx=0.3,rely=0.2)

email_entry= ctk.CTkEntry(frame1,font=font2, text_color='#fff',fg_color='#001a2e' ,bg_color='#121111', border_color='#004780', border_width=3,placeholder_text='Digite seu email.', placeholder_text_color='#a3a3a3',corner_radius=5 ,width=200)
email_entry.place(relx=0.3,rely=0.4)


password_entry = ctk.CTkEntry(frame1, font=font2, show="*", text_color='#fff',fg_color='#001a2e', bg_color='#121111', border_color='#004780',border_width=3, placeholder_text='Digite sua senha..', placeholder_text_color='#a3a3a3', corner_radius=5 ,width=200)
password_entry.place(relx=0.3,rely=0.6)


signup_button= ctk.CTkButton(frame1, command=signup ,font=font2,text_color='#fff', text='Cadastrar-se', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
signup_button.place(relx=0.35,rely=0.8)



login_label = ctk.CTkLabel(frame1, font=font3, text='Já possui uma conta?', text_color='#fff', bg_color='#001220')
login_label.place(relx=0.00,rely=0.93 )

login_button = ctk.CTkButton(frame1,command=login ,font=font4, text_color='#00bf77', text='ENTRAR', fg_color='#001220', hover_color='#001220', cursor='hand2', corner_radius=5,width=40,height=1)
login_button.place(relx=0.88,rely=0.95)
















app.mainloop() 

 