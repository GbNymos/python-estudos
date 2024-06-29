import sqlite3
from sqlite3 import Error


def conexao_banco():
    conexao=None
    caminho="D:\\convite\\python-estudos\\project\\atividades\\banco_de _dados\\agenda" 
    try:
        conexao=sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    return conexao

conexao=conexao_banco()

## Inserir dados(valores) nas colunas da teabela
def inserir_valores(conexao,comando_sql,n,tele,email):
    try:
        c=conexao.cursor()
        c.execute(comando_sql,(n,tele,email))
        conexao.commit()
        print("Registro feito")
    except Error as erro:
        print(erro)


#comando_sql=""" INSERT INTO tb_contatos(t_nomeContatos,t_telefContato,t_emailContato)
#VALUES('teste_nome','test_telefone','test_email')
#"""

for i in range(0,1):
    n=str(input("Nome:"))
    tele=str(input("Telefone:"))
    email=str(input("Email:"))
#    comando_sql="INSERT INTO tb_contatos(t_nomeContatos,t_telefContato,t_emailContato)VALUES(?,?,?)"
#    inserir_valores(conexao,comando_sql,n,tele,email)


## Deletaando resgistro
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro removido")
    except Error as erro:
        print(erro)

#vsql="DELETE FROM tb_contatos WHERE n_idContatos=7"
#deletar(conexao,vsql)


## Atualizar registro
def atualizar(conexao,query):
    try:
        c=conexao.cursor()
        c.execute(query)
        conexao.commit()
        print("Registro atualizado")
    except Error as erro:
        print(erro)

####Formas de atualizar :
#query="UPDATE tb_contatos SET t_nomeContatos='gabriele' WHERE n_idContatos=2"
#query="UPDATE tb_contatos SET t_telefContato='99999999' WHERE t_nomeContatos='jao'"

#atualizar(conexao,query)


def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    result=c.fetchall()   #Retorna o resultado da consulta como uma tupla
    return result


sql="SELECT *FROM tb_contatos"

result=consultar(conexao,sql)
#passa por cada item da tupla result
for i in result:
    print(i)


conexao.close()


