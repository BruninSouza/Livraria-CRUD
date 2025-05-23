from Gui import *
import Backend as core
from tkinter import messagebox

app = None
selected = None

def view_command():
    rows = core.view()
    app.listBiblioteca.delete(0, END)
    for r in rows:
        app.listBiblioteca.insert(END, r)

def search_command():
    app.listBiblioteca.delete(0, END)

    def get_int_value(entry):
        try:
            return int(entry.get())
        except ValueError:
            return None
        
    rows = core.search(app.txt_autor.get(), app.txt_titulo.get(), app.txt_idioma.get(), app.txt_editora.get(), \
                       get_int_value(app.txt_ano), get_int_value(app.txt_reais), get_int_value(app.txt_centavos))
    for r in rows:
        app.listBiblioteca.insert(END, r)

def insert_command():
    try:

        reais = int(app.txt_reais.get())
        centavos = int(app.txt_centavos.get())
    
        if centavos >= 100:
            reais += centavos // 100
            centavos = centavos % 100
        
        core.insert(app.txt_autor.get(), app.txt_titulo.get(), app.txt_idioma.get(), app.txt_editora.get(),\
                        app.txt_ano.get(), reais, centavos)

        app.txt_reais.set(reais)
        app.txt_centavos.set(centavos)

        view_command()

    except ValueError:
        messagebox.showerror("Erro de entrada", "Preço deve conter apenas números inteiros.")


def update_command():

    try:

        if selected is None:
            raise NameError

        reais = int(app.txt_reais.get())
        centavos = int(app.txt_centavos.get())
    
        if centavos >= 100:
            reais += centavos // 100
            centavos = centavos % 100
        
        core.update(selected[0],app.txt_autor.get(), app.txt_titulo.get(), app.txt_idioma.get(), app.txt_editora.get(),\
                        app.txt_ano.get(), reais, centavos)

        app.txt_reais.set(reais)
        app.txt_centavos.set(centavos)
        
        view_command()

    except (ValueError, NameError):
        messagebox.showerror("Erro", "Selecione um item e verifique os campos.")

def del_command():

    try:

        if selected is None:
            raise NameError
        
        id = selected[0]
        core.delete(id)
        view_command()

    except NameError:
        messagebox.showwarning("Aviso", "Nenhum item selecionado")

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
