import customtkinter as ctk
import sqlite3
from tkinter import *

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
                   password TEXT NOT NULL )''')
# ------------------------------------------------------------------------

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

    username_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='Usuário',placeholder_text_color='#fff',text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3')
    username_cadastro.place(x=60, y=60)
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# FRAME DE LOGIN PRINCIPAL
framelogin = ctk.CTkFrame(master=root, width=700, height=400)
framelogin.place(relx=0.114, rely=0.17)


# ------------------------------------------------------------------------

# inputs área de login

username_entry = ctk.CTkEntry(
    master=root, placeholder_text='Digite seu usuário', border_color='white', width=300, height=50)
username_entry.place(relx=0.31, rely=0.39)

password_entry = ctk.CTkEntry(
    master=root, placeholder_text='Digite sua senha', border_color='white', width=300, height=50)
password_entry.place(relx=0.31, rely=0.5)

signup_button = ctk.CTkButton(master=root, text='CONECTAR', text_color='#fff',
                              width=130, cursor='hand2', fg_color='#808080', hover_color='#858a80')
signup_button.place(relx=0.39, rely=0.63)
# ------------------------------------------------------------------------
# botão para tela de cadastro
cadastro_button = ctk.CTkButton(framelogin, command=tela_cadastro, text_color='white', text='Realizar cadastro',
                                cursor='hand2', width=90, height=30, fg_color='#808080', hover_color='#858a80')
cadastro_button.place(x=586, y=370)

# ------------------------------------------------------------------------


root.mainloop()
