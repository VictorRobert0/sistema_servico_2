import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

root = ctk.CTk()
root.title('SISTEMA LOGISTICA - LOGIN')
root.resizable(False, False)
root.geometry('900x400')
root.config(bg='#FAF0E6')
root._set_appearance_mode("Dark")

# ------------------------------------------------------------------------


# ------------------------------------------------------------------------

# Conexão com banco de dados sqLITE3


# Tabela de servicos

conn = sqlite3.connect('./database/database.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS servicos (
                   servico TEXT NOT NULL
                   )''')


# -------------------------------------------------------------------------

# Tabela de Users

conn = sqlite3.connect('./database/database.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users (
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   rg TEXT NOT NULL,
                   password TEXT NOT NULL )''')
# ------------------------------------------------------------------------


# lista = cursor.execute('SELECT * FROM servicos ')
# print(cursor.fetchone())


# --------------------------------------------------------------------------

# VALIDANDO O INPUT DO SERVIÇO

def validar_servico():
    service = services_input.get()

    if service != '':
        cursor.execute(
            'SELECT  servico FROM servicos WHERE servico=?', [service])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Serviço já existe.')
        else:

            cursor.execute('INSERT INTO servicos VALUES (?)', [service])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Serviço criado com sucesso ;)')

    else:
        messagebox.showerror('Erro', 'Por favor, preencha os dados.')


# ------------------------------------------------------------------------

# INTERFACE DO SISTEMA
def sistema_on():

    sistema = ctk.CTkToplevel()
    sistema.geometry('900x900')
    sistema.title('SISTEMA DE LOGISTICA')

    sistema.resizable(False, False)
    
    frame_sistema = ctk.CTkFrame(master=sistema, width=900, height=900)
    # IMAGEM DE FUNDO
    imagem_sistema = PhotoImage(file='./img/Underconstruction-bro.png')
    image_label = Label(sistema, image=imagem_sistema, width=900, height=900)
    image_label.place(x=0, y=0)
    frame_sistema.imagem_sistema = imagem_sistema
    frame_sistema.place(x=0, y=0)

        
    
    
    
    
        
        
    sistema.mainloop()



# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# VALIDAÇÃO LOGIN E ACESSO A SISTEMA

def login_account():
    global username
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute(
            'SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Sucesso', 'Login realizado com sucesso')
                return sistema_on()

            else:
                messagebox.showerror('Erro', 'Senha inválida ;)')
        else:
            messagebox.showerror('Erro', 'Usuário inválido ;/')
    else:
        messagebox.showerror('Erro', 'Preencha todos os campos')
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# FUNÇÃO CADASTRO
def validar_formulario():
    username = username_cadastro.get()
    email = email_cadastro.get()
    rg = rg_cadastro.get()
    password = password_cadastro.get()

    if username != '' and email != '' and password != '' and rg != '':
        cursor.execute(
            'SELECT  username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Usuário já existe.')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?,?,?,?)', [
                           username, email, rg, hashed_password])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Conta criada com sucesso ;)')

    else:
        messagebox.showerror('Erro', 'Por favor, insira todos os dados.')
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


def voltar_page():
    framecadastro1.destroy()
    framecadastro.destroy()


# TELA DE CADASTRO DE USUARIO


def tela_cadastro():
    global framelogin
    global framecadastro
    framelogin.destroy()
    framecadastro = ctk.CTkFrame(master=root, width=1000, height=1000)
    # IMAGEM DE FUNDO
    imagem_cadastro = PhotoImage(file='./img/desktop computer-bro.png')
    image_label = Label(framecadastro, image=imagem_cadastro,
                        width=655, height=400)
    image_label.place(x=0, y=0)
    framecadastro.imagem_cadastro = imagem_cadastro
    framecadastro.place(x=0, y=0)

# ------------------------------------------------------------------------
    global framecadastro1
# -------------------------------------------------------------------------
    # FRAME DE CADASTRO PRINCIPAL
    framecadastro1 = ctk.CTkLabel(
        master=root, width=350, height=700, bg_color='#fafafa', text='')
    framecadastro1.place(relx=0.637, rely=0.0)

    global username_cadastro
    global email_cadastro
    global rg_cadastro
    global password_cadastro

    # ------------------------------------------------------------------------

    username_cadastro = ctk.CTkEntry(framecadastro1, placeholder_text='Usuário', placeholder_text_color='#C0C0C0',
                                     text_color='white', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    username_cadastro.place(x=60, y=60)
    username_cadastro.focus()

    # ------------------------------------------------------------------------

    email_cadastro = ctk.CTkEntry(framecadastro1, placeholder_text='Email', placeholder_text_color='#C0C0C0',
                                  text_color='white', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    email_cadastro.place(x=60, y=100)

    # ------------------------------------------------------------------------

    rg_cadastro = ctk.CTkEntry(framecadastro1, placeholder_text='RG', placeholder_text_color='#C0C0C0', text_color='white',
                               fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    rg_cadastro.place(x=60, y=140)

    # ------------------------------------------------------------------------

    password_cadastro = ctk.CTkEntry(framecadastro1, show='*', placeholder_text='Senha', placeholder_text_color='#C0C0C0',
                                     text_color='white', fg_color='#F0F8FF', border_color='#000', border_width=2, bg_color='#fff', width=200)
    password_cadastro.place(x=60, y=180)

    # ------------------------------------------------------------------------

    # BOTÃO CADASTRAR-SE

    validar_cadastro = ctk.CTkButton(framecadastro1, command=validar_formulario, text_color='#fff', text='CADASTRAR-SE',
                                     fg_color='#778899', hover_color='#005180', bg_color='#fff', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    validar_cadastro.place(x=90, y=230)


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# BOTÃO AREA DE LOGIN
    voltar_cadastro = ctk.CTkButton(framecadastro1, text_color='#fff', text='ÁREA DE LOGIN', fg_color='#778899', hover_color='#005180',
                                    bg_color='#F0F8FF', cursor='hand2', corner_radius=5, width=350, anchor=CENTER, command=voltar_page)
    voltar_cadastro.place(x=0, y=360)


# ------------------------------------------------------------------------

# FRAME DE LOGIN PRINCIPAL
framelogin = ctk.CTkFrame(master=root, width=900, height=900)
framelogin.place(relx=0.0, rely=0.0)
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# IMAGEM LOGIN

imagem_login = PhotoImage(file='./img/Mobile login-rafiki.png')
image_lframe = Label(root, image=imagem_login, width=1480, height=400)
framelogin.imagem_imagem_login = imagem_login
image_lframe.place(x=0, y=0)
framelogin.place(x=0, y=0)

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
global username_entry
global password_entry
# ------------------------------------------------------------------------

# inputs área de login

username_entry = ctk.CTkEntry(
    master=root, placeholder_text='Digite seu usuário', border_color='black', width=300, height=50, fg_color=("#fff", "#d3d3d3"), text_color='#000', bg_color='#d3d3d3')
username_entry.place(relx=0.31, rely=0.39)
username_entry.focus()

password_entry = ctk.CTkEntry(
    master=root, show='*', placeholder_text='Digite sua senha', border_color='black', width=300, height=50, fg_color=("#fff", "#d3d3d3"), text_color="#000")
password_entry.place(relx=0.31, rely=0.55)

signup_button = ctk.CTkButton(master=root, command=login_account, text='CONECTAR', text_color='#fff',
                              width=130, cursor='hand2', fg_color='#d1d1d1', hover_color='#005180', corner_radius=10, bg_color='#d1d1d1')
signup_button.place(relx=0.39, rely=0.73)
# ------------------------------------------------------------------------
# botão para tela de cadastro

cadastro_button = ctk.CTkButton(root, command=tela_cadastro, text='CADASTRAR FUNCIONÁRIO',
                                fg_color='#808080', cursor='hand2', width=0, hover_color='#005180', bg_color='#d1d1d1')
cadastro_button.place(x=725, y=370)

# ------------------------------------------------------------------------


root.mainloop()
