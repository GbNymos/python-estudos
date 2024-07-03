import os
import sqlite3
from sqlite3 import Error


def conexaoBanco():
    caminho="D:\\convite\\python-estudos\\project\\atividades\\banco_de _dados\\agenda" 
    conexao=None

    try:
        conexao=sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    return  conexao


def query(conexao,sql):  #Executa as query atualizar,deletar e inserir
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("query sucesso.")
    except Error as erro:
        print(erro)
    finally:
        conexao.close()

def consultar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        res=c.fetchall()
    except Error as erro:
        print(erro)
    return res

def menu():
    os.system("cls") or None
    print("""
    1-Inserir novo registro
    2-Deletar registro
    3-Atualizar registro
    4-consultar registros
    5-Consultar registro por nome
    6-Sair """)

def inserir_registro():
    os.system("cls")

    nome=str(input("Nome:"))
    telef=str(input("telefone:"))
    email=str(input("Email:"))
    sql=f"""INSERT INTO tb_contatos (t_nomeContatos, t_telefContato, t_emailContato) 
             VALUES ('{nome}', '{telef}', '{email}')"""
    query(conexao,sql)
    
def deletar_registro():
    id=int(input("Digite o ID para ser deletado:"))
    sql=f"DELETE FROM tb_contatos WHERE n_idContatos={id}"
    query(conexao,sql)

def atualizar_registro():
    id=int(input("Digite o ID para ser alterado:"))

    sql=f"SELECT * FROM tb_contatos WHERE n_idContatos={id}"
    r=consultar(conexao,sql)
    rnome=r[0][1] #nome  ##interando a lista um por um e guardadando cada valor em uma variavel
    rtelef=r[0][2]#telefone
    remail=r[0][3]#email

    nome=str(input("Nome:"))
    telef=str(input("telefone:"))
    email=str(input("Email:"))  

    if len(nome)==0:
        nome=rnome
    if len(telef)==0:
        telef=rtelef
    if len(email)==0:
        email=remail

    sql=f"""UPDATE tb_contatos 
              SET t_nomeContatos='{nome}', t_telefContato='{telef}', t_emailContato='{email}' 
              WHERE n_idContatos={id}"""
    query(conexao,sql)


def consultar_registros():
    sql="SELECT * FROM tb_contatos"
    res=consultar(conexao,sql)
    limite=10
    cont=0

    for i in res:
        print("ID:{:_<3} Nome:{:<30} Telefone:{:<14} E-mail:{:<30}".format(i[0],i[1],i[2],i[3]))
        cont+=1
        if cont>=limite:
            cont=0
            os.system("pause") or None
            os.system("cls") or None  

    print("Fim da lista")
    os.system("pause") or None

def consultar_registroNome():
    nome=str(input("Nome:"))
    sql="SELECT * FROM tb_contatos WHERE t_nomeContatos LIKE '%"+nome+"%' "
    res=consultar(conexao,sql)
    limite=10
    cont=0

    for i in res:
        print("ID:{:_<3} Nome:{:<30} Telefone:{:<14} E-mail:{:<30}".format(i[0],i[1],i[2],i[3]))
        cont+=1
        if cont>=limite:
            cont=0
            os.system("pause") or None
            os.system("cls") or None  

    print("Fim da lista")
    os.system("pause") or None



conexao=conexaoBanco()
opc=0

while opc!=6:
    menu()
    opc=int(input("Digite uma opcao: "))
    if opc==1:
        inserir_registro()
    elif opc==2:
        deletar_registro()
    elif opc==3:
        atualizar_registro()
    elif opc==4:
        consultar_registros()
    elif opc==5:
        consultar_registroNome()
    elif opc==6:
        print("Saiu do programa...")
    else:
        os.system("cls") or None
        print("Opcao invalida")
        os.system("pause") or None


os.system("cls") or None;print("Obrigado(a) por utilizar o programa")