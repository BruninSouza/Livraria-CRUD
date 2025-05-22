# Tkinter é um módulo usado para desenvolver interface gráfica em python
from tkinter import *

class Gui():
    """Classe de interface gráfica 
    (Graphical User interface ou GUI)"""

    # Pads são para simbolizar o "padding" (distânciamento) dos conteudos da interface em relação à borda
    x_pad = 5
    y_pad = 3

    # Width serve para definir a largura que a janela terá
    width_entry = 30

    # Para criar um janela 
    window = Tk() # Tk serve para utilizar a biblioteca tkinter
    window.wm_title("Cadastro") # O nome da aplicação é escrito dentro dos parenteses

    # Definição das variáveis que recebem os dados inseridos pelo user
    txtAutor = StringVar()
    txtTitulo = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar() 

    # Criando objetos que farão parte das janelas
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="email")
    lblCPF = Label(window, text="CPF")

    # Entradas
    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entSobrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

    # Lista de clientes e scroll para a mesma
    listClientes = Listbox(window, width=100)
    ScrollClientes = Scrollbar(window)

    # Botões
    btnViewAll = Button(window, text="Vê todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    # Associando objetos
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblCPF.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    ScrollClientes.grid(row=0, column=6, rowspan=10)

    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    # União de scrollbar com listbox
    listClientes.configure(yscrollcommand=ScrollClientes.set)
    ScrollClientes.configure(command=listClientes.yview)

    # Adicionando aparência à interface
    for child in window.winfo_children():
        Widget_class = child.__class__.__name__

        if Widget_class == "Button":
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='WE')
        elif Widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif Widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()