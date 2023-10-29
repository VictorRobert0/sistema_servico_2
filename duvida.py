import customtkinter as ctk

app= ctk.CTk()

app.geometry('400x400')


botao = ctk.CTkSegmentedButton(master=app, values=['oi', 'teste'])
botao.place(x=50,y=50)


app.mainloop()