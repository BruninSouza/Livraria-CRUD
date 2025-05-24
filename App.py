from Gui import *
import Backend as core
from tkinter import messagebox

app = None
selected = None

# Transforma valor de entrada em um inteiro, ou em None caso esteja vazio
def get_int_value(entry):
    value = entry.get().strip()
    if value == "":
        return None
    try:
        return int(value.lstrip("0") or "0")
    except:
        return None

# Limpa todos os campos da interface
def resetar_campos():
    app.ent_autor.delete(0, END)
    app.ent_titulo.delete(0, END)
    app.ent_idioma.delete(0, END)
    app.ent_editora.delete(0, END)
    app.ent_ano.delete(0, END)
    app.ent_preco_reais.delete(0, END)
    app.ent_preco_centavos.delete(0, END)

# Faz a requisição para exibir todos os itens do db
def view_command():
    rows = core.view()
    app.listBiblioteca.delete(0, END)
    for r in rows:
        app.listBiblioteca.insert(END, r)

# Faz uma requisoção de busca ao DB com base no parâmentro usado 
def search_command():
    app.listBiblioteca.delete(0, END)

    ano = get_int_value(app.txt_ano)
    reais = get_int_value(app.txt_reais)
    centavos = get_int_value(app.txt_centavos)

    rows = core.search(
        app.txt_autor.get(),
        app.txt_titulo.get(),
        app.txt_idioma.get(),
        app.txt_editora.get(),
        ano,
        reais,
        centavos
    )
    for r in rows:
        app.listBiblioteca.insert(END, r)

# Faz requisição ao DB para inserir um novo item ao banco de dados
def insert_command():
    
    try:

        reais = get_int_value(app.txt_reais)
        centavos = get_int_value(app.txt_centavos)
        ano = app.txt_ano.get()

        if centavos >= 100:
            reais += centavos // 100
            centavos %= 100
        elif centavos < 0 and centavos >= -100:
            reais -= 1
            centavos %= 100
        elif centavos < -100:
            reais += centavos // 100
            centavos %= 100
            
        def validar_ano(ano):
            return ano.isdigit() and len(ano) <= 4

        if not validar_ano(ano):
            messagebox.showerror("Erro", "Ano inválido. Verifique o campo e tente novamente.")
            return

        core.insert(
            app.txt_autor.get(),
            app.txt_titulo.get(),
            app.txt_idioma.get(),
            app.txt_editora.get(),
            ano,
            reais,
            centavos
        )

        app.ent_preco_reais.delete(0, END)
        app.ent_preco_reais.insert(END, reais)

        app.ent_preco_centavos.delete(0, END)
        app.ent_preco_centavos.insert(END, centavos)
        resetar_campos()
        view_command()

    except ValueError:
        messagebox.showerror("Erro de entrada", "Preço deve conter apenas números inteiros.")

# Faz requisição de atualizar um item selecionado do banco de dados
def update_command():
    try:

        if selected is None:
            raise NameError("Nenhum item selecionado")
        
        reais = get_int_value(app.txt_reais)
        centavos = get_int_value(app.txt_centavos)
        ano = app.txt_ano.get()

        if centavos >= 100:
            reais += centavos // 100
            centavos %= 100
        elif centavos < 0 and centavos >= -100:
            reais -= 1
            centavos %= 100
        elif centavos < -100:
            reais += centavos // 100
            centavos %= 100

        def validar_ano(ano):
            return ano.isdigit() and len(ano) <= 4

        if not validar_ano(ano):
            messagebox.showerror("Erro", "Ano inválido. Verifique o campo e tente novamente.")
            return

        core.update(
            selected[0],
            app.txt_autor.get(),
            app.txt_titulo.get(),
            app.txt_idioma.get(),
            app.txt_editora.get(),
            ano,
            reais,
            centavos
        )

        app.ent_preco_reais.delete(0, END)
        app.ent_preco_reais.insert(END, reais)

        app.ent_preco_centavos.delete(0, END)
        app.ent_preco_centavos.insert(END, centavos)

        view_command()

    except NameError:
        messagebox.showerror("Erro", "Nenhum item selecionado.")
    except ValueError:
        messagebox.showerror("Erro", "Verifique os valores numéricos nos campos.")

# Faz requisição de deletar item do banco de dados
def del_command():
    try:
        if selected is None:
            raise NameError

        id = selected[0]
        core.delete(id)
        view_command()

    except NameError:
        messagebox.showwarning("Aviso", "Nenhum item selecionado")

# Função que seleciona item do banco de dados e preenche os campos referentes à ele
def getSelectedRow(event):
    global selected

    try:
        index = app.listBiblioteca.curselection()
        if not index:
            return
        selected = app.listBiblioteca.get(index[0])

        app.ent_autor.delete(0, END)
        app.ent_autor.insert(END, selected[1])
        app.ent_titulo.delete(0, END)
        app.ent_titulo.insert(END, selected[2])
        app.ent_idioma.delete(0, END)
        app.ent_idioma.insert(END, selected[3])
        app.ent_editora.delete(0, END)
        app.ent_editora.insert(END, selected[4])
        app.ent_ano.delete(0, END)
        app.ent_ano.insert(END, selected[5])
        app.ent_preco_reais.delete(0, END)
        app.ent_preco_reais.insert(END, selected[6])
        app.ent_preco_centavos.delete(0, END)
        app.ent_preco_centavos.insert(END, selected[7])

    except Exception as e:
        print(f"Erro ao selecionar item: {e}")

# Limpa o campo selecionado anteriormente
def clear_selection_command():
    global selected
    selected = None
    app.listBiblioteca.selection_clear(0, END)
    app.ent_autor.delete(0, END)
    app.ent_titulo.delete(0, END)
    app.ent_idioma.delete(0, END)
    app.ent_editora.delete(0, END)
    app.ent_ano.delete(0, END)
    app.ent_preco_reais.delete(0, END)
    app.ent_preco_centavos.delete(0, END)

# Inicia a aplicação
if __name__ == "__main__":
    app = Gui()
    app.listBiblioteca.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.btnClear.configure(command=clear_selection_command)
    app.run()
