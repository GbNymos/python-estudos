from tkinter import *
from tkinter import ttk

def mostrar_valor():
    v=var.get()
    print(v)

def d_escala():
    valor=v.get()
    escala=Scale(app,from_=0,to=100,orient=HORIZONTAL)
    escala.set(valor)
    escala.pack()

def valor_listB():
    valor=boxAnime.get(ACTIVE) ##pegando a chave selecionada
    print(dict_anime[valor]) #mostrar o valor dessa chave



app=Tk()
app.geometry("500x400")

##Combo box e label frame
lbFrame=LabelFrame(app,text="Animes",borderwidth=2,relief="solid")
lbFrame.pack()
listaAnime=["naruto","jujutsu kaisen","pokemon"]
var=StringVar()
cb_anime=ttk.Combobox(lbFrame,values=listaAnime,textvariable=var)
cb_anime.set(listaAnime[0])
cb_anime.pack()
btn=Button(lbFrame,text="Aperte",command=mostrar_valor)
btn.pack()

##Escala
Label(app,text="Escala:").pack(pady=10)
v=IntVar()
resp=Entry(app,textvariable=v)
resp.pack()
btn=Button(text="Definir escala",command=d_escala)
btn.pack()

##listbox
dict_anime={"naruto":10}
Label(app,text="listbox:").pack(pady=10)
boxAnime=Listbox(app) 
for k,v in dict_anime.items():  ##Funciona com listas tambem
    boxAnime.insert(END,k)
boxAnime.pack()
btn=Button(text="mostrar valor",command=valor_listB)
btn.pack()




app.mainloop()


"""Funciona , fazer uma calculadora
for i in range(0,5):
    btn2=Button(text=i)
    btn2.pack()"""