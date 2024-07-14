from tkinter import *
from tkinter import ttk
from time import sleep

def start():
    for i in range(0,100):
        sleep(0.5)
        varbarra.set(i)
        app.update()

app=Tk()
app.geometry("700x500")

tela=ttk.Notebook(app)
tela.place(x=10,width=600,height=400)

aba1=Frame(tela,borderwidth=1,relief="solid")
aba1.pack()
aba2=Frame(tela,borderwidth=1,relief="solid")
aba2.pack()


tela.add(aba1,text="barra de progresso")
tela.add(aba2,text="sobre")

##Barra de progresso
varbarra=DoubleVar()
#varbarra.set(10)
barra=ttk.Progressbar(aba1,variable=varbarra,maximum=100)
barra.place(y=10,width=300)

btn=Button(text="iniciar",command=start)
btn.pack()



app.mainloop()