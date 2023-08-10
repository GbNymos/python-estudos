"posso fazer assim ou com o construtor"
#class cliente:
#    def somar (self,a,b):
#        self.a=int()
#       self.b=int()
#        pass        
"posso fazer classes dessa forma tambem"
#class clientes:
#    idad=input("difite")
#    print(idad)
#p1=cliente 


class conta:
    def __init__(self,numero,nome,valor:int) :
        self._numero=numero
        self._nome=nome
        self._saldo=valor

    def deposita (self,valor:int):
        self._saldo += valor
        print("deposito realizado com sucesso!!")
    def saque(self,valor:int):
        if self._saldo<0:
            print("erro,saldo negativo")
        else:
            self._saldo-=valor
            print("dinheiro saindo...")
    def extrato(self):
        print(f"nome: {self._nome}   numero: {self._numero}    saldo: {self._saldo}.")
        print("obrigado pela preferencia ")


#programa principal

c1=conta(4444,"gabi",100)
c1.deposita(100)
c1.saque(10)
c1.extrato()


