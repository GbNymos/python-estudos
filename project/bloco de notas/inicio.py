print("""
incluir tarefas [1]
exibir tarefas  [2]
sair do programa [0]
""")

mylist=[]

def inluir():
    mylist.append(input("Digite sua tarefa:"))
    mylist.append(',')
    arquivo=open("..tarefas.txt","a")
    arquivo.writelines(mylist)
    

def exibir():
    arquivo=open("tarefas.txt","r")
    myCurrentList = arquivo.read().split(',')
    print('\n'.join(map(str, myCurrentList)))
    



b=""
while b!=0:
    while True:
        try:
            a=int(input("digite uma opcao:"))
        except ValueError:
            print("Por favor digite um numero valido(numero inteiro)")    
        if a >3:
            print("digite um numero existente na tabela acima.")
        if a <4 :
           break
    if a==0:
        b=0
        break
    elif a==1:
        inluir()
        print("tarefa salva")
    elif a == 2:
        exibir()
        print("Essas sao suas tarefas salvas.")
        
print("PROGRAMA ENCERRADO")        

    
        