import customtkinter as ctk
from tkinter import *


janela = ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
janela.title('Área de serviço')
janela.geometry('500x500')
janela.resizable(False, False)

# -------------------------------------------------------------------------------------
# IMAGENS

img = PhotoImage(file="background.png")
label_img = ctk.CTkLabel(master=janela, image=img, text="").place(x=0, y=0)

# Funções


def cadastrar_servico():
    return print('Cadastro de serviços chegou')


# TEMA---------------------------------------------------------------------------
def appearance(self):
    self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=[
                               '#000', "#fff"]).place(x=50, y=150)
    self.opt_apm = ctk.CTkOptionMenu(
        self, values=["Dark", "Light"], command=self.change_apm).place(x=50, y=200)


def change_theme(self, nova_aparencia):
    ctk.set_appearance_mode(nova_aparencia)

# ---------------------------------------------------------------------------


def cadastrar_cliente():
    return print('Cadastro de clientes chegou')


# --------------------------------------------------------------------------------
# Tela 3 | Serviço

def abrir_janela_servico():

    janela3 = ctk.CTkToplevel()
    janela3.resizable(False, False)
    janela3.geometry('800x500')
    janela3.title("Cadastro de serviços")
    titulo = ctk.CTkLabel(
        master=janela3, text="Área de cadastro de serviços", text_color='#fff')
    titulo.place(relx=0.5, rely=0.03, anchor=CENTER)
    button_tela3 = ctk.CTkButton(master= janela3 , text='CADASTRAR SERVIÇO', fg_color='#109010', hover_color='#245b3b', command=cadastrar_servico).place(relx=0.5, rely=0.9, anchor= CENTER)

# selecionar os serviços

    select_services = ctk.CTkComboBox(master=janela3, values=[
                                      "Orçamento", "Revisão completa", "Troca de pastilhas"], width=180)
    select_services.place(relx=0.5, rely=0.5, anchor=CENTER)
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# Inputs e posicionamento

    select_users = ctk.CTkComboBox(master=janela3, values=[
                                   "Victor", "Lucas", "Marcelo"], width=500)
    select_users.place(relx=0.5, rely=0.2, anchor=CENTER)

    services_input = ctk.CTkTextbox(master=janela3, width=600, height=100)
    services_input.place(relx=0.5, rely=0.7, anchor=CENTER)

# Labels e posicionamento
    label_users = ctk.CTkLabel(
        master=janela3, text="Selecione o cliente").place(relx=0.5, rely=0.13, anchor= CENTER)
    
#--------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# Botão - abrir janela serviço
button_tela3 = ctk.CTkButton(
    janela, text='Cadastrar serviço', command=abrir_janela_servico).place(x=50, y=200)

# --------------------------------------------------------------------------------

# TELA 2 | Cadastro


def abrir_janela():

    janela2 = ctk.CTkToplevel()
    janela2.resizable(width=False, height=False)
    janela2.geometry('500x500')
    janela2.title('Cadastro de clientes')

    place_nome = ctk.CTkLabel(janela2, text='Nome').place(x=50, y=20)
    input_nome = ctk.CTkEntry(
        janela2, placeholder_text='Digite o nome do cliente').place(x=50, y=50)

    place_rg = ctk.CTkLabel(janela2, text='RG').place(x=300, y=20)
    input_rg = ctk.CTkEntry(
        janela2, placeholder_text='Digite o RG do cliente').place(x=300, y=50)

    place_cpf = ctk.CTkLabel(janela2, text='CPF').place(x=50, y=100)
    input_cpf = ctk.CTkEntry(
        janela2, placeholder_text='Digite o CPF do cliente').place(x=50, y=130)

    place_endereco = ctk.CTkLabel(janela2, text='Endereço').place(x=210, y=195)
    input_endereco = ctk.CTkTextbox(
        janela2, width=380, height=50).place(x=70, y=225)

    place_observation = ctk.CTkLabel(
        janela2, text='Observação').place(x=210, y=295)
    input_observation = ctk.CTkTextbox(
        janela2, width=380, height=50).place(x=70, y=325)

    place_data = ctk.CTkLabel(janela2, text='Data').place(x=300, y=100)
    input_data = ctk.CTkEntry(
        janela2, placeholder_text='Digite a data').place(x=300, y=130)

    button_tela2 = ctk.CTkButton(
        janela2, text='CADASTRAR', fg_color='#109010', hover_color='#245b3b', command=cadastrar_cliente).place(x=170, y=400)

# -----------------------------------------------------------------------------------
# Botão abrir| Cadastro de cliente
button_tela1 = ctk.CTkButton(
    janela, text='Cadastrar cliente', command=abrir_janela).place(x=50, y=300)


# -----------------------------------------------------------------------------------


janela.mainloop()
