import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

root = ctk.CTk()
root.resizable(False, False)
root.geometry('900x600')
root.config(bg='#FAF0E6')

# ------------------------------------------------------------------------
# Conexão com banco de dados sqLITE3

conn = sqlite3.connect('./database/database.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users (
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   rg TEXT NOT NULL,
                   password TEXT NOT NULL )''')
# ------------------------------------------------------------------------














#FUNÇÃO LOGIN

def login_account():
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Sucesso', 'Login realizado com sucesso')
            else:
                messagebox.showerror('Erro', 'Senha inválida ;)')
        else:
            messagebox.showerror('Erro', 'Usuário inválido ;/')
    else: 
        messagebox.showerror('Erro', 'Preencha todos os campos')



def validar_formulario():
    username = username_cadastro.get()
    email = email_cadastro.get()
    rg = rg_cadastro.get()
    password = password_cadastro.get()
    
    
    if username != '' and email != '' and password != '' and rg != '':
        cursor.execute('SELECT  username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Usuário já existe.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute ('INSERT INTO users VALUES (?,?,?,?)', [username, email ,rg, hashed_password])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Conta criada com sucesso ;)')
    else:
        messagebox.showerror('Erro', 'Por favor, insira todos os dados.')
    
















# TELA DE CADASTRO DE USUARIO

def tela_cadastro():
    framelogin.destroy()
    framecadastro = ctk.CTkFrame(master=root, width=1000, height=1000)
    framecadastro.place(x=0, y=0)

    # IMAGEM DE FUNDO
    imagem_cadastro = PhotoImage(file='./img/fundo-cadastro.png')
    image_label = Label(framecadastro, image=imagem_cadastro)
    image_label.place(x=0, y=0)
    framecadastro.imagem_cadastro = imagem_cadastro
# ------------------------------------------------------------------------
    # FRAME DE CADASTRO PRINCIPAL
    framecadastro = ctk.CTkLabel(
        master=root, width=350, height=700, bg_color='#12abb3', text='')
    framecadastro.place(relx=0.637, rely=0.0)

    global username_cadastro
    global email_cadastro
    global rg_cadastro
    global password_cadastro
    
    # ------------------------------------------------------------------------
    
    username_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='Usuário',placeholder_text_color='#fff',text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    username_cadastro.place(x=60, y=60)
    username_cadastro.focus()
    
    # ------------------------------------------------------------------------
    
    email_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='Email',placeholder_text_color='#fff',text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    email_cadastro.place(x=60, y=100)
    
    # ------------------------------------------------------------------------
    
    rg_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='RG',placeholder_text_color='#fff',text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    rg_cadastro.place(x=60, y=140)
    
    # ------------------------------------------------------------------------
    
    
    password_cadastro = ctk.CTkEntry(framecadastro, show='*' ,placeholder_text='Senha',placeholder_text_color='#fff',text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    password_cadastro.place(x=60, y=180)
    
    
    # ------------------------------------------------------------------------
    #BOTÃO CADASTRAR-SE

    validar_cadastro = ctk.CTkButton(framecadastro,command=validar_formulario,text_color='#fff', text='CADASTRAR-SE', fg_color='#00965d', hover_color='#006e44', bg_color='#12abb3', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    validar_cadastro.place(x=90,y=230)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
    voltar_cadastro = ctk.CTkButton(framecadastro,text_color='#fff', text='ÁREA DE LOGIN', fg_color='#db152d', hover_color='#8f0b1b', bg_color='#12abb3', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    voltar_cadastro.place(x=10, y=500)
   
   
                  
    
    
    

# ------------------------------------------------------------------------
# FRAME DE LOGIN PRINCIPAL
framelogin = ctk.CTkFrame(master=root, width=700, height=400)
framelogin.place(relx=0.114, rely=0.17)


global username_entry
global password_entry
# ------------------------------------------------------------------------

# inputs área de login

username_entry = ctk.CTkEntry(
    master=root,placeholder_text='Digite seu usuário', border_color='white', width=300, height=50)
username_entry.place(relx=0.31, rely=0.39)
username_entry.focus()

password_entry = ctk.CTkEntry(
    master=root, show='*',placeholder_text='Digite sua senha', border_color='white', width=300, height=50)
password_entry.place(relx=0.31, rely=0.5)

signup_button = ctk.CTkButton(master=root,command=login_account ,text='CONECTAR', text_color='#fff',
                              width=130, cursor='hand2', fg_color='#808080', hover_color='#858a80')
signup_button.place(relx=0.39, rely=0.63)
# ------------------------------------------------------------------------
# botão para tela de cadastro
cadastro_button = ctk.CTkButton(framelogin, command=tela_cadastro, text_color='white', text='Realizar cadastro',
                                cursor='hand2', width=90, height=30, fg_color='#808080', hover_color='#858a80')
cadastro_button.place(x=586, y=370)

# ------------------------------------------------------------------------


root.mainloop()
