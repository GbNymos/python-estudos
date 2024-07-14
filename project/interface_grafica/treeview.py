from tkinter import *
from tkinter import ttk

app=Tk()
app.geometry("700x500")

lista=[["1","nome"],["2","test"],["3","saber"]]
tv=ttk.Treeview(app,columns=("id","nome"),show="headings")

tv.column("id",minwidth=0,width=50)
tv.heading("id",text="ID")

tv.column("nome",minwidth=0,width=200)
tv.heading("nome",text="NOME")

for (id,nome) in lista:
    tv.insert("","end",values=(id,nome))

tv.pack()

app.mainloop()


