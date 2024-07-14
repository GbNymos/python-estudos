from tkinter import *
from tkinter import messagebox 


def mudar_cor():
    opc=escolha.get()

    if opc=="azul":
        Label(text="Azul",background="#0000FF").place(width=150,height=200)
        messagebox.showinfo("Cor escolhida","A cor que vc escolheu foi azul.")
    elif opc =="laranja":
        Label(text="Laranja",background="#FFA500").place(width=150,height=200)
    elif opc =="vermelho":
        Label(text="Vermelho",background="#FF0000").place(width=150,height=200)
        

janela=Tk()
janela.geometry("500x400")
janela.title("RadioButton")






quadro1=Frame(janela,borderwidth=1,relief="solid")
quadro1.place(width=300,height=200)
Label(quadro1,text="cores",font=("Arial",15)).place(x=40,y=50)  ## esta dentro do frame

escolha=StringVar()

azul=Radiobutton(janela,text="Azul",value="azul",variable=escolha) ## esta fora do frame
azul.pack()

laranja=Radiobutton(janela,text="Laranja",value="laranja",variable=escolha)
laranja.pack()

vermelho=Radiobutton(janela,text="Vermelho",value="vermelho",variable=escolha)
vermelho.pack()

botao=Button(text="cor de fundo",command=mudar_cor)
botao.pack()


img=PhotoImage(file="project\\interface_grafica\\tripulacao-zoro.png")
Label(janela,image=img).place(x=10,y=250)

janela.mainloop()