""" jogo de decisao
um joguinho que tera:
uma lista com respostas aleatorias para perguntas que o usuario vai fazer .
tera a opcao:
sair do jogo.
fazer uma nova pergunta
"""

import random 
from tkinter import*


lista_resp=["vai dormi e melhor pra voce","SIM","NAO","DETEBAYO","SE EU FOSSE VOCE EU NAO FARIA ISSO"]
def principal ():
    rep=random.choice(lista_resp)
    texto["text"]= f'''RESPOSTA:
    
        {rep}'''
    

#criar uma janela
janela=Tk()
janela.geometry("300x600")
#dar um titulo para minha janela
janela.title("gamezin")
janela.config(bg="black") # DEFINI A COR DO BACKGROUD


#tituli central q aparece na tela
text=Label(janela,text="JOGO DE DECISAO\nFACA UMA PERGUNTA\nE SE DIVIRTA COM A DECISAO DO JOGO.",bg="black",fg="red")
text.grid(column=0,row=5)
text1=Label(janela,text="Digite sua pergunta",bg="black",fg="red",font="Arial")
text1.grid(column=0,row=8,padx=30)
# widget de entrada de dados
entrada=Entry()
entrada.grid(column=0,row=9,padx=50)

#botao que recebe um comando que e uma funcao sem parenteses pois ela so sera executada no texto
botao=Button(text="aperte para saber a resposta ",font="Arial",command=principal)
botao.grid(column=0,row=12)
texto=Label(janela,text="")
texto.grid(column=0,row=19)

#deixa a janela sempre amostra
janela.mainloop()