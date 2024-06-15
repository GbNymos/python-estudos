#testes numeros complexos
n1=2#calculou com o numero real
n2=2j # calculou com o numero imaginario
n_complexo=complex(4,1)
print(n1+n_complexo)
print(n2+n_complexo)
print(n_complexo.real)
print(n_complexo.imag)


## teste de string
nome="gabriele oli"

for i in range(0,len(nome)):
    print(nome[i])
    n="g"
  

print(nome)


## captura de nomes e sobre nomes


nome1=str(input("Digite seu nome completo"))
nom=nome1.split(" ")
primeiro_nome=nom[0];sobrenome=nom[1]
print(f"PRIMEIRO NOME:{primeiro_nome} SOBRENOME:{sobrenome}")



      