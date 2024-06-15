"""Crie uma classe chamada "Pessoa"
 com os atributos nome, idade e profissão. 
 Implemente métodos para definir e obter os valores dos atributos."""


"""obs:
era pra ter utlizaddo metodos get e set

"""




class pessoa :
    def __init__(self):
        self.nome=""
        self.idade=0
        self.profissao=""

    def nome_esc(self):
        n=str(input("nome"))
        self.nome=n
    
    def idad(self):
        n=str(input("idade"))
        self.idade=n
    
    def prof (self):
        n=str(input("prof"))
        self.profissao=n
        
        



        

p1=pessoa()

p1.idad()
p1.prof()
print(p1.profissao)
print(p1.nome)
print(p1.idade)


