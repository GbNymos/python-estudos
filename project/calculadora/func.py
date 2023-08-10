def somar(num):
    c=0
    for i in num:
      c+=i
    return c


def subtrair (num):
    c=num[0]
    for i in num[1:]:
        c-=i
        
    return c
    

def multiplica (num):
    c=1
    for i in num:
        c*=i
    return c


def leianum(msg):
    while True:
        try:
            print('\033[1;37m')
            n=float (input (msg))
        except (ValueError, TypeError):
            print ('\033[m','\033[31m Erro! Digite um número inteiro válido! \033[m ')
            continue 
        else:
            return n
   
       
def sair (msg=' '):
    print('\033[33m')
    n=str(input (msg)).strip ()
    print('\033[m')
    while n != ' ' or n != '0':
        if n == '0':
            print ('\033[31m OPERAÇÃO ENCERRADA. \033[m '.center(40))
            return False
        if n == '':
            print('\033[1;34m Continue ... \033[m '.center(40))
            return True
        else:
            n=str(input ('\033[31m Digite;"0" pra sair ou "Enter" pra continuar \033[m  ')). strip ()
            
            
def sinal():
    n=str(input ('\033[1m Sinal da operaçao: \033m '))
    while  n not in '+-×':
        n=str(input('\033[31m Digite um sinal valido da tabela acima  \033[m '))
    return n
