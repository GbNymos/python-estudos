"""prograama que  organizar nomes (recebera uma lista)
-organizar nomes 
-filtra nomes
-cadastra e retirar nomes
"""

class organizador :
    ## construtor, o que deve ter no inicio da classe 
    def __init__(self) :
        self.lista=[]
        with open("nomes.txt", "r") as arquivo:
            for linha in arquivo:
                self.lista.append(linha.strip())
             

    ## cadastra nomes de novos usuarios
    def cadastra(self):
        n=str(input("Digite um nome que deseja cadastra:"))
        if n in self.lista:
            print("esse nome ja existe na lista ")
        else:
            self.lista.append(n)
    
    def remover(self):
        n= str(input("Digite o nome que deseja remover "))
        self.lista.remove(n)
    
    def ordem_alfabetica(self):
        ## sorted nao modifica a lista original mas organizar em ordem alfabetica , ja o sort modifica a lista original
        self.lista.sort()

    
    def filtra(self):
        n=str(input("Digite o nome que deseja encontra:")).strip()
        for i,v in enumerate(self.lista):
            if v==n :
                p=i+1
                resultado=True
                break
            else:
                resultado=False
        if resultado== True:
            print(f"nome encontrado, esta localizado na posicao{p}")
        if resultado==False:
            print("nome nao emcontrado, verifique se escreveu corretamente.")

nomes = []

##resolver isso aqui depois
def sistema ():
    print("""bem vindo ao organizador ....
          primeiro de tudo adicione um aqrquivo.txt""")
       
    




arquivo=organizador()

arquivo.filtra()