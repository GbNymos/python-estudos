import random
from time import sleep
import os
## criar dois personagens, escolhera o  lutador, a lutar vai comecar danos aleatorios 
class person_luta:
    dano_causado=0
    dano_recebido=0 
    def __init__(self,nome,profissao):
        self.nome=nome
        self.profissao=profissao

    def informacao(self):
        print(f"""
        Nome............{self.nome}
        Profissao.......{self.profissao}      
        """)

person=[person_luta("tyla","policia"),person_luta("gab","assasina"),person_luta("dan","boxeador"),person_luta("dylo","capoerista")]
        


def menu():
    print("PERSONAGENS:")
    for i in range(len(person)):
        person[i].informacao()

def contagem_regressiva(msg,segundos):
    for i in range(segundos, 0, -1):
        print(f"{msg}... {i}")
        sleep(2)
        os.system("cls")
        

def id_person():
    global person
    nome_person=str(input("Nome do lutador(a) que voce ira aposta? "))
    aposta=nome_person
    num=random.randint(0,len(person)-1)
    ven=person[num].nome
    if ven==nome_person:
        print("Voce venceu a aposta!")
    else:
        print("Voce perdeu a aposta!")
    return ven
        


while True:
    menu()
    vencedor=id_person()
    print(f"VENCEDOR FOI: {vencedor}")
    parada=str(input("Deseja continuar apostando:Para sai[0] para continuar[Enter]"))
    if parada==str(0):
        break


"""
Melhorias:
-> Colocar cores e melhorar a apresentacao no terminal
-> tratar alguns erros de entrada de dados
"""