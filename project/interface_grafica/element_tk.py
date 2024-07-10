from tkinter import *

def mudar_cor():
    opc=escolha.get()

    if opc=="azul":
        Label(text="cor",background="#0000FF").place(width=150,height=200)
    elif opc =="laranja":
        Label(text="cor",background="#FFA500").place(width=150,height=200)
    elif opc =="vermelho":
        Label(text="cor",background="#FF0000").place(width=150,height=200)
        

janela=Tk()
janela.geometry("500x400")
janela.title("RadioButton")



Label(text="cores").pack()

escolha=StringVar()

azul=Radiobutton(janela,text="Azul",value="azul",variable=escolha)
azul.pack()

laranja=Radiobutton(janela,text="Laranja",value="laranja",variable=escolha)
laranja.pack()

vermelho=Radiobutton(janela,text="Vermelho",value="vermelho",variable=escolha)
vermelho.pack()

botao=Button(text="cor de fundo",command=mudar_cor)
botao.pack()


janela.mainloop()