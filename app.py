import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

root = ctk.CTk()
root.title('SISTEMA LOGISTICA - LOGIN')
root.resizable(False, False)
root.geometry('900x600')
root.config(bg='#FAF0E6')
root._set_appearance_mode('Dark')

# ------------------------------------------------------------------------








# Conexão com banco de dados sqLITE3


#Tabela de servicos

conn = sqlite3.connect('./database/database.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS servicos (
                   servico TEXT NOT NULL
                   )''')


#-------------------------------------------------------------------------
#Tabela de Users

conn = sqlite3.connect('./database/database.db')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users (
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   rg TEXT NOT NULL,
                   password TEXT NOT NULL )''')
# ------------------------------------------------------------------------



def validar_servico():
    service = services_input.get()
    

    if service != '':
        cursor.execute(
            'SELECT  servico FROM servicos WHERE servico=?', [service])
        if cursor.fetchone() is not None:
            messagebox.showerror('Erro', 'Serviço já existe.')
        else:

            cursor.execute('INSERT INTO servicos VALUES (?)', [
                           service])
            conn.commit()
            messagebox.showinfo('Sucesso', 'Serviço criado com sucesso ;)')

    else:
        messagebox.showerror('Erro', 'Por favor, preencha os dados.') 
     
    
# ------------------------------------------------------------------------

#INTERFACE DO SISTEMA
def sistema_on():
    
    sistema = ctk.CTk()
    sistema.geometry('900x600')
    sistema.title('SISTEMA DE LOGISTICA')
    
    sistema.resizable(False, False)
    
    titulo = ctk.CTkLabel(
        master=sistema, text="Área de cadastro de serviços", text_color='#fff')
    titulo.place(relx=0.5, rely=0.03, anchor=CENTER)
    button_tela3 = ctk.CTkButton(master= sistema , text='CADASTRAR SERVIÇO', fg_color='#109010', hover_color='#245b3b', command=validar_servico)
    button_tela3.place(relx=0.5, rely=0.9)

# selecionar os serviços

    select_services = ctk.CTkComboBox(master=sistema, values=[
                                      "Orçamento", "Revisão completa", "Troca de pastilhas"], width=180)
    select_services.place(relx=0.5, rely=0.5, anchor=CENTER)
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
    global services_input
# Inputs e posicionamento

    select_users = ctk.CTkComboBox(master=sistema, values=[username], width=500)
    
    
    select_users.place(relx=0.5, rely=0.2, anchor=CENTER)

    services_input = ctk.CTkEntry(master=sistema,width=600, height=100)
    services_input.place(relx=0.5, rely=0.7, anchor=CENTER)

# Labels e posicionamento
    label_users = ctk.CTkLabel(
        master=sistema, text="Selecione o cliente").place(relx=0.5, rely=0.13, anchor= CENTER)
    
    

    
    
    
    
    
    
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
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def voltar_page():
    print('Não consegui fazer funcionar ainda ')

# TELA DE CADASTRO DE USUARIO


def tela_cadastro():
    global framecadastro
    framelogin.destroy()
    framecadastro = ctk.CTkFrame(master=root, width=1000, height=1000)
    # IMAGEM DE FUNDO
    imagem_cadastro = PhotoImage(file='./img/fundo-cadastro.png')
    image_label = Label(framecadastro, image=imagem_cadastro)
    image_label.place(x=0, y=0)
    framecadastro.imagem_cadastro = imagem_cadastro
    framecadastro.place(x=0, y=0)

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

    username_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='Usuário', placeholder_text_color='#fff',
                                     text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    username_cadastro.place(x=60, y=60)
    username_cadastro.focus()

    # ------------------------------------------------------------------------

    email_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='Email', placeholder_text_color='#fff',
                                  text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    email_cadastro.place(x=60, y=100)

    # ------------------------------------------------------------------------

    rg_cadastro = ctk.CTkEntry(framecadastro, placeholder_text='RG', placeholder_text_color='#fff', text_color='white',
                               fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    rg_cadastro.place(x=60, y=140)

    # ------------------------------------------------------------------------

    password_cadastro = ctk.CTkEntry(framecadastro, show='*', placeholder_text='Senha', placeholder_text_color='#fff',
                                     text_color='white', fg_color='#12abb3', border_color='#fff', border_width=2, bg_color='#12abb3', width=200)
    password_cadastro.place(x=60, y=180)

    # ------------------------------------------------------------------------
    
    
    
    # BOTÃO CADASTRAR-SE

    validar_cadastro = ctk.CTkButton(framecadastro, command=validar_formulario, text_color='#fff', text='CADASTRAR-SE',
                                     fg_color='#00965d', hover_color='#006e44', bg_color='#12abb3', cursor='hand2', corner_radius=5, width=120, anchor=CENTER)
    validar_cadastro.place(x=90, y=230)
    
    
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# BOTÃO AREA DE LOGIN
    voltar_cadastro = ctk.CTkButton(framecadastro, text_color='#fff', text='ÁREA DE LOGIN', fg_color='#B0E0E6', hover_color='#87CEFA',
                                    bg_color='#12abb3', cursor='hand2', corner_radius=5, width=350, anchor=CENTER, command=voltar_page)
    voltar_cadastro.place(x=1, y=500)


# ------------------------------------------------------------------------

# FRAME DE LOGIN PRINCIPAL
framelogin = ctk.CTkFrame(master=root, width=1000, height=1000)
framelogin.place(relx=0.0, rely=0.0)


global username_entry
global password_entry
# ------------------------------------------------------------------------

# inputs área de login

username_entry = ctk.CTkEntry(
    master=root, placeholder_text='Digite seu usuário', border_color='white', width=300, height=50)
username_entry.place(relx=0.31, rely=0.39)
username_entry.focus()

password_entry = ctk.CTkEntry(
    master=root, show='*', placeholder_text='Digite sua senha', border_color='white', width=300, height=50)
password_entry.place(relx=0.31, rely=0.5)

signup_button = ctk.CTkButton(master=root, command=login_account, text='CONECTAR', text_color='#fff',
                              width=130, cursor='hand2', fg_color='#808080', hover_color='#858a80')
signup_button.place(relx=0.39, rely=0.63)
# ------------------------------------------------------------------------
# botão para tela de cadastro

cadastro_button = ctk.CTkButton(framelogin, command=tela_cadastro, text='CADASTRAR FUNCIONÁRIO',
                                fg_color='#808080', cursor='hand2', width=40, hover_color='#858a80')
cadastro_button.place(x=725, y=570)

# ------------------------------------------------------------------------


root.mainloop()

