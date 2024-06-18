import os
from random import randint

## nao terminei, falta: verificar vitoria , e estou tendo problema em exibir o numero das colunas na tela.

jogarDnovo="s"
jogadas=0
jogador=2 #cpu -1 jogador-2
max_jogadas=9
vit="n"
cont=0
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],]


def tela():
    global velha # e obrigatorio utilizar o global pela questao de q vou usar dentro de um loop
    global cont
    print("    0    1    2  ")
    for l in range(0,3):
        for c in range(len(velha)):
            print(f"{velha[l][c]} | ",end=" " )
        cont+=1
        print(f"  :{cont} \n")
    print(f"JOGADAS:{jogadas}")
    cont=0

def jogador_jogar():
    global jogador; global jogadas; global max_jogadas
    if jogador==2 and jogadas<max_jogadas:
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
            while velha[l][c] != " " :
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c]="x"
            jogador=1
            jogadas+=1
        except:
            print("Linha ou coluna invalida! ")


def cpu_jogar():
    global jogador; global jogadas; global max_jogadas
    if jogador==1 and jogadas<max_jogadas:
        l=randint(0,3)
        c=randint(0,3)
        while velha[l][c] != " " :
            l=randint(0,3)
            c=randint(0,3)
        velha[l][c]="o"
        jogador=2
        jogadas+=1


while True:
    tela()
    jogador_jogar()
    cpu_jogar()