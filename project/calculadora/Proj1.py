
import func



print ('\033[1;35m CALCULADORA.PY \033[m'.center (45))
print (""" 
[ + ] ADIÇÃO
[ - ] SUBTRAÇÃO
[ × ] MULTIPLICAÇÃO \n """)


mylist=[]
while True:
    mylist.append(func.leianum('>1°Numero: '))
    print (' ')
    e=func.sinal()
    mylist.append(func.leianum('>2° Numero: '))
    print(' ')
    while True:
        if e == '+' :
            print ( *mylist,sep=' + ',end=' ')
            print ('=' ,'\033[32m',func.somar(mylist),'\033[m')
          
            if func.sair('\nEncerrar a Adição:"0" / Continuar:"enter"') == False:
                mylist.clear()
                break 
            mylist.append(func.leianum('>Adicione mais valores '))
             
        elif e == '-':
            print (*mylist,sep=' - ',end=' ')
            print ('=' ,'\033[32m', func.subtrair (mylist),'\033[m' )
          
            if func.sair('\nEncerrar a Subtração:"0" / Continuar:"enter"') == False:
                mylist.clear()
                break 
            mylist.append(func.leianum('>Subtrair mais valores'))
       
        elif e == '×':
            print (*mylist,sep=' + ',end=' ')
            print ('=' ,'\033[32m',func.multiplica (mylist),'\033[m')
          
            if func.sair('\nEncerrar a multiplicação:"0" / Continuar:"enter"') == False:
                mylist.clear()
                break 
            mylist.append(func.leianum('>Multiplicar mais valore ')) 
   
    if func.sair('\n SAIR DO PROGRAMA:"0"\n Fazer outras operações:"enter" : ')==False:
       break

