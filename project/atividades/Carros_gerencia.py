import os
carros=list()


class carro:

    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velmax=pot*2
        self.ligado=False
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def info (self):
        print(f"nome....{self.nome}");print(f"potencia....{self.pot}")
        lig="sim" if self.ligado else "nao"
        print(f"Velocidade maxima....{self.velmax}");print(f"ligado....{lig}")

def menu():
    os.system("cls") or None
    print(f"""
    1-Novo carro
    2-informacoes do carro
    3-Excluir carro
    4-ligar carro
    5-desligar carro
    6-listar carros
    7 sair do programa
    -->Quantidade de carros {len(carros)}
""" 
)
    try:
        opc=int(input("Digite o numero da opcao desejada: "))
    except TypeError:
        print("Por favor, digite apenas numeros ")
    return opc

def Novo_carro():
    os.system("cls") or None
    n=str(input("Qual o nome do carro:"))
    p=int(input("Qual a potencia:"))
    car=carro(n,p)
    carros.append(car)
    os.system("pause") or None #aguarda ate q qualquer tecla seja apertada para continuar o programa

def informacoes():
    os.system("cls") or None
    n=int(input("Digite a posicao do carro em que deseja ver as informacoes"))
    try:
        carros[n].info()
    except:
        print("carro nao existe na lista")
    os.system("pause") or None

def excluir_carro():
    os.system("cls") or None
    n=int(input("Digite a posicao do carro em que deseja excluir"))
    try:
        del carros[n]
        print("Carro excluido")
    except:
        print("carro nao existe na lista")
    os.system("pause") or None

def ligar_carro():
    os.system("cls") or None
    n=int(input("Digite a posicao do carro em que deseja ligar"))
    try:
        carros[n].ligar()
        print("Carro ligado")
    except:
        print("carro nao existe na lista")
    os.system("pause") or None

def desligar_carro():
    os.system("cls") or None
    n=int(input("Digite a posicao do carro em que deseja ver as informacoes"))
    try:
        carros[n].desligar()
        print("carro desligado")
    except:
        print("carro nao existe na lista")
    os.system("pause") or None

def Listar_carros():
    os.system("cls") or None
    for posicao,c in enumerate(carros):
        print(f"Carro {c.nome} esta na posicao: {posicao}")
    os.system("pause") or None


main=menu()
while main<7:
    if main==1:
        Novo_carro()
    elif main==2:
        informacoes()
    elif main==3:
        excluir_carro()
    elif main==4:
        ligar_carro()
    elif main==5:
        desligar_carro()
    elif main==6:
        Listar_carros()
    main=menu()

os.system("cls") or None
print("programa finalizado!")