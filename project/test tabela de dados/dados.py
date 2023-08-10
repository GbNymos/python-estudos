"""
1. criar uma lista de produtos
2. da lista se pode escolher um produto pra colocar no carrinho/outra lissta
3. outra lista que vai conter todos os produtos escolhidos pelo usuario
isso sera tarves de escolhas tabelA DE ESCOLHAS
4. o usuario pode tirar produtos de carrinho
5. o usuario pode limpat/apagar o carrinho completamente

6. o usuario pode ver o valor total das suas compras
7. criar outra lista que contenha codigos de desconto ex: descnto10pc
8. o ususario tem direito a disconto se tiver um cupom/code especial
desejar parar de adicionar[aperte:0,continuar: ENTER. \n ->

obs: PRAZO DE VALIDADE ACABOU , A UNICO ERRO A FUNCAO DE SOMAR AS COMPRAS NAO PARECE ESTA FUNCIONANDO MUITO BEM E A FUNCAO
DE DESCONTO TAMBEM NAO .
- REFAZER ESSE CODIGO NOVAMENTO DEPOIS DE UM TEMPO SO QUE EM POO
"""



def exibir():
    global lista_produtos
    print(" TABELA DE PRODUTOS")
    for v ,k in lista_produtos.items():
        print(v,"->" ,k)



def carrinho(escolha):
    global my_carrinho
    opcao=False
    while True:
        ## adicionar produtos
        if escolha==2:
            opcao=str(input("digite o nome do produto:")).lower().strip()
            global lista_produtos
            if opcao in lista_produtos:
                my_carrinho.append(opcao) 
                print("produto adicionado")
                opcao=True
            else:
                print("nao temos esse produto. ou por favor verifique se escreveu o nome corretamente")
         ## tirar algum produto do carrinho
        elif escolha==3 :
            opcao=str(input("digite o nome do produto que desejar apagar: ")).lower().strip()
            if len(my_carrinho)==0:
                print("CARRINHO VAZIO!")
                opcao=True
            elif opcao in my_carrinho :
                my_carrinho.remove(opcao)
                print("produto removido")
                opcao=True
            else :
                print("Esse produto nao estar no carrinho.ou por favor verifique se escreveu o nome corretamente")
        elif escolha ==5:
            opcao=True
            return print(my_carrinho)
            
        elif escolha==4:
            my_carrinho.clear()
            opcao=True
        if opcao == True:
            break
        
        
   

def desc_aleat():
    from random import choice
    global desc
    v= choice(list(desc.keys()))
    print(f"seu codigo especial e {v}")
    escolha=str(input("digite o codigo de desconto,se nao aperte (enter)")).strip().lower()
    if escolha in desc:
        valor=desc[escolha]
        porcento=valor
        valordesconto=(valor / 100) * s
        valorf=valor - valordesconto
        print(valorf)
    else:
        print("codigo invalido.")
    
    

def compras():
    global s 
    s=0
    print("selecione apenas os produtos que deseja do carrinho, para fazer as compras aperte(ENTER) ")
    global comprar
    global my_carrinho
    global lista_produtos
    while True:
        p=str(input("nome do produto: ")).strip().lower()
        if p=="":
            break
        elif p in my_carrinho:
            comprar.append(p)
            print("o que mais deseja ...")
        elif len(my_carrinho)==0:
            print("carrinho esta vazio, que tal adicionar produtos")
        else:
            print("voce nao adicionou esse produto no carrinho")
    ## SOMAR AS CHAVES ESPECIFICo
    for chave in comprar:
        if chave in lista_produtos:
            s += lista_produtos[chave]
            print(F"valor:{s}")
  
   

lista_produtos ={"shampoo":10,"sabonete":3.0}
my_carrinho=[]
comprar=[]
desc={"des10":10,"des20":20,"des30":30,"des50":50}


print("""O QUE DESEJA FAZER
OPCOES
Digite 
 [0] para fechar o programa
 [1] ver tabelas de produtos novamente
 [2] para adicionar produtos para o carrinho
 [3] tirar algum produto do carrinho
 [4] limpar todo o carrinho
 [5] exibir carrinho
 [6] tirar a sorte de desconto
 [7] fazer a comprar

""")

exibir()

while True:
    try:
        opcao=int(input("digite sua opcao: "))
        if opcao < 0 or opcao > 7:
            print("digite um dos numeros das opcoes acima")
        elif opcao ==1:
            exibir()
        elif opcao == 6:
            desc_aleat()
        elif opcao ==7:
            compras()
            
        elif opcao ==0:
            break
        else : 
            carrinho(opcao)
        
    except (ValueError,NameError):
        print("digite apenas os numeros das opcoes acima.irei voltar para ultima funcao" )
        continue
    

print("PROGRAMA ENCERRADO. OBRIGADO PELA PREFERENCIA:)")

    