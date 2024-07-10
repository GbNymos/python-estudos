from tkinter import *
import banco_dados

#caminho=os.path.dirname(__file__) ->outra forma de acessar o diretorio atual.sem precisar mudar as barras como tive que fazer na forma debaixo ao copiar e colar
caminho="project/interface_grafica/nome.txt"
def gravar_dados():
    if nome.get()!="":
        vnome=nome.get()
        vemail=email.get()
        vtelef=telef.get()
        vobs=obs.get("1.0",END)
        sql="INSERT INTO tb_contatos(t_nomeContatos,t_telefContato,t_emailContato,obs) VALUES ('"+vnome+"','"+vtelef+"','"+vemail+"','"+vobs+"')"
        banco_dados.query(sql)
        print("Tudo ok")
        nome.delete(0,END)
        email.delete(0,END)
        telef.delete(0,END)
        obs.delete("1.0",END)


app=Tk()
app.title("Agenda")
app.geometry("700x500")
app.configure(background="#4BE5EB",cursor="hand2")

Label(text="Nome:",background="#4BE5EB",fg="#000",anchor=W).place(x=5,y=10,width=100,height=25)
nome=Entry(app)
nome.place(x=10,y=30,width=190,height=20)

Label(text="E-mail:",background="#4BE5EB",fg="#000",anchor=W).place(x=5,y=50,width=100,height=25)
email=Entry(app)
email.place(x=10,y=70,width=190,height=20)

Label(text="Telefone:",background="#4BE5EB",fg="#000",anchor=W).place(x=5,y=100,width=100,height=25)
telef=Entry(app)
telef.place(x=10,y=120,width=150,height=20)

Label(text="Anote sua observacao:",background="#4BE5EB",fg="#000",anchor=W).place(x=5,y=150,width=100,height=45)
obs=Text(app)
obs.place(x=10,y=180,width=200,height=110)

Button(app,text="Salvar",justify="center",background="#FFC0CB",command=gravar_dados).place(x=10,y=310,width=120,height=30)



mainloop()