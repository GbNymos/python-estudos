import json

"""  string para json
person='{"naruto":19,"kurama":9,"kakashi":30,"sakura":8}'
person_json=json.loads(person)

print(person_json["naruto"])
for i in person_json.keys():
    print(i)
"""

##Formas de abrir o arquivo json externo no python
#with open("D:/convite/python-estudos/project/arquivos/pessoas.json") as pessoas:
    #test=json.load(pessoas)
#test=json.load(open("D:/convite/python-estudos/project/arquivos/pessoas.json"))
abrir_json=open("D:/convite/python-estudos/project/arquivos/pessoas.json")
test=json.load(abrir_json)

p=test["pessoas"]

lista_email=[]
for i in range(len(p)):
    clientes=p[i]
    lista_email.append(clientes["email"])
    if clientes["nome"]=="Bob":
        print("vc tem uma fatura pendente")
        clientes["idade"]=26

print(test)
print(lista_email )
