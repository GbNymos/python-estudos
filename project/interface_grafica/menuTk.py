from tkinter import *
import os
from agendaGui import nova_janela

app=Tk()
app.title("Agenda")
app.geometry("700x500")
app.configure(background="#4BE5EB",cursor="hand2")

def semcomando():
    pass

def novoContato():
    nova_janela()
    
  

barra_menu=Menu(app)## so a barra que vai ter o menu dentro
menuContatos=Menu(barra_menu,tearoff=0)# o tearoff determina se o menu pode ser "destacado" (tear off) da barra de menus e exibido como uma janela separada.

menuSobre=Menu(barra_menu)
menuSobre.add_command(label="Gabi",command=semcomando)

menuContatos.add_command(label="Novo",command=novoContato)
menuContatos.add_command(label="Deletar",command=semcomando)
menuContatos.add_command(label="pesquisar",command=semcomando)
menuContatos.add_separator()
menuContatos.add_command(label="Sair",command=app.quit)


barra_menu.add_cascade(label="contatos",menu=menuContatos)
barra_menu.add_cascade(label="Desenvolvedora",menu=menuSobre)

app.config(menu=barra_menu)

app.mainloop()