import sqlite3
from sqlite3 import Error


####Forma simples de fazer conexao
#caminho="D:\\convite\\python-estudos\\project\\atividades\\banco_de _dados\\agenda" 
#conexao=sqlite3.connect(caminho)


##Fazer conexao ao banco de dados com funcao
def conexao_banco():
    conexao=None
    caminho="D:\\convite\\python-estudos\\project\\atividades\\banco_de _dados\\agenda" 
    try:
        conexao=sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    return conexao



## Craiar tabelas
def CriarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("tabela criada")
    except Error as erro:
        print(erro)


conexao=conexao_banco()

#comando sql para criar a tabela 
comando_sql=""" CREATE TABLE tb_contatosDois (
    n_idContatos INTEGER PRIMARY KEY AUTOINCREMENT,
    t_nomeContatos TEXT(30),
    t_telefContato TEXT(14),
    t_emailContato TEXT(30)
);
"""
CriarTabela(conexao,comando_sql)


conexao.close()

