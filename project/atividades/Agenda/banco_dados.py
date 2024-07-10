import sqlite3
from sqlite3 import Error

caminho="project\\atividades\\banco_de_dados\\agenda.db"
def con():
    con=None
    try:
        con=sqlite3.connect(caminho)

    except Error as erro:
        print(erro)

    return con


    
def query(query):  #Executa as query atualizar,deletar e inserir
    conexao=con()
    try:
        c=conexao.cursor()
        c.execute(query)
        conexao.commit()
        print("query sucesso.")
    except Error as erro:
        print(erro)
    finally:
        conexao.close()