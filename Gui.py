from tkinter import *

class Gui():

    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk() 
    window.wm_title("Cadastro Livros")
    window.resizable(True, True)

    # Variáveis
    txt_autor = StringVar()
    txt_titulo = StringVar()
    txt_idioma = StringVar()
    txt_editora = StringVar() 
    txt_ano = StringVar() 
    txt_reais = StringVar()
    txt_centavos = StringVar()

    # Labels
    lbl_autor = Label(window, text="Autor")
    lbl_titulo = Label(window, text="Título")
    lbl_idioma = Label(window, text="Idioma")
    lbl_editora = Label(window, text="Editora")
    lbl_ano = Label(window, text="Ano de Lançamento")
    lbl_preco = Label(window, text="Preço (R$)")

    # Entradas
    ent_autor = Entry(window, textvariable=txt_autor, width=width_entry)
    ent_titulo = Entry(window, textvariable=txt_titulo, width=width_entry)
    ent_idioma = Entry(window, textvariable=txt_idioma, width=width_entry)
    ent_editora = Entry(window, textvariable=txt_editora, width=width_entry)
    ent_ano = Entry(window, textvariable=txt_ano, width=width_entry)

    # Entradas de preços com reais e centavos
    frame_preco = Frame(window)
    ent_preco_reais = Entry(frame_preco, textvariable=txt_reais, width=5)
    ent_preco_centavos = Entry(frame_preco, textvariable=txt_centavos, width=5)
    ent_preco_reais.pack(side=LEFT)
    Label(frame_preco, text=",").pack(side=LEFT)
    ent_preco_centavos.pack(side=LEFT)

    # Listbox e Scroll
    listBiblioteca = Listbox(window, width=100)
    ScrollBiblioteca = Scrollbar(window)

    # Grid de labels
    lbl_autor.grid(row=0, column=0, sticky='W')
    lbl_titulo.grid(row=1, column=0, sticky='W')
    lbl_idioma.grid(row=2, column=0, sticky='W')
    lbl_editora.grid(row=3, column=0, sticky='W')
    lbl_ano.grid(row=4, column=0, sticky='W')
    lbl_preco.grid(row=5, column=0, sticky='W')

    # Grid de entradas
    ent_autor.grid(row=0, column=1, sticky='WE')
    ent_titulo.grid(row=1, column=1, sticky='WE')
    ent_idioma.grid(row=2, column=1, sticky='WE')
    ent_editora.grid(row=3, column=1, sticky='WE')
    ent_ano.grid(row=4, column=1, sticky='WE') 
    frame_preco.grid(row=5, column=1, sticky="W", padx=x_pad, pady=y_pad)

    # Listbox e Scrollbar
    listBiblioteca.grid(row=0, column=2, rowspan=12, sticky='NSEW')
    ScrollBiblioteca.grid(row=0, column=6, rowspan=12,  sticky='NSE')

    listBiblioteca.configure(yscrollcommand=ScrollBiblioteca.set)
    ScrollBiblioteca.configure(command=listBiblioteca.yview)

    # Botões dentro do frame
    btnClear = Button(window, text="Limpar seleção")
    btnViewAll = Button(window, text="Vê todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    # Grid dos botões dentro do frame
    btnClear.grid(row=6, column=0, columnspan=2, sticky="W")
    btnViewAll.grid(row=7, column=0, columnspan=2, sticky='W')
    btnBuscar.grid(row=8, column=0, columnspan=2, sticky='W')
    btnInserir.grid(row=9, column=0, columnspan=2, sticky='W')
    btnUpdate.grid(row=10, column=0, columnspan=2, sticky='W')
    btnDel.grid(row=11, column=0, columnspan=2, sticky='W')
    btnClose.grid(row=12, column=0, columnspan=2, sticky='W')

    # Configura dimensionamento
    for child in window.winfo_children():

        Widget_class = child.__class__.__name__

        if Widget_class == "Button":
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='WE')

        elif Widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NSEW')

        elif Widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NSEW')

        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='W')
        
        for i in range(13):
            window.grid_rowconfigure(i, weight=1)

        for i in range(3):
            window.grid_columnconfigure(i, weight=1)

    # Faz a interface rodar em loop
    def run(self):
        Gui.window.mainloop()