from tkinter import *
from tkinter import ttk


def inserir():
    if vid.get()=="" or vnome.get()=="" or vemail.get()=="" or vfone.get()=="":
        print("vazio,nada inserido")
    tv.insert("","end",values=(vid.get(),vnome.get() ,vemail.get() , vfone.get()))
    vid.delete(0,"end")
    vnome.delete(0,"end")
    vemail.delete(0,"end")
    vfone.delete(0,"end")
    vid.focus()

def deletar():
    try:
        item_selection=tv.selection()[0]
        tv.delete(item_selection)
    except:
        print("Erro,campo vazio")

def obter_valores():
    try:
        item_selection=tv.selection()[0]
        valores=tv.item(item_selection,"values")
        print(valores)
        print(valores[0])
    except:
        print("Erro,campo vazio")


app=Tk()
app.geometry("700x500")


tv=ttk.Treeview(app,columns=("id","nome","email","fone"),show="headings")

tv.column("id",minwidth=0,width=50)
tv.heading("id",text="ID")
tv.column("nome",minwidth=0,width=100)
tv.heading("nome",text="NOME")
tv.column("email",minwidth=0,width=150)
tv.heading("email",text="Email")
tv.column("fone",minwidth=0,width=150)
tv.heading("fone",text="Telefone")

vid=Entry(app)
vid.grid(column=0,row=0,sticky="w")
vnome=Entry(app)
vnome.grid(column=0,row=1,sticky="w")
vemail=Entry(app)
vemail.grid(column=0,row=2,sticky="w")
vfone=Entry(app)
vfone.grid(column=0,row=3,sticky="w")

tv.grid(column=0,row=4)

btn1=Button(app,text="inserir",command=inserir)
btn1.grid(column=0,row=10)

btn2=Button(app,text="deletar",command=deletar)
btn2.grid(column=0,row=11)

btn3=Button(app,text="obter",command=obter_valores)
btn3.grid(column=0,row=12)
app.mainloop()