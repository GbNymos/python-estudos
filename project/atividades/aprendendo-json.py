import json

#criando dicionario json
time_7= {
    "Naruto Uzumaki": {
        "poder": ["Rasengan", "Kurama", "Modo Sábio"],
        "clã": "Uzumaki"
    },
    "Sasuke Uchiha": {
        "poder": ["Sharingan", "Rinnegan", "Chidori"],
        "cla": "Uchiha"
    },
    "Sakura Haruno": {
        "poder": ["Força sobre-humana","Jutsus médicos"],
        "cla": "Haruno"
    },
    "Kakashi Hatake": {
        "poder":["Sharingan", "Chidori", "Raikiri"] ,
        "cla": "Hatake"
    }
}




p1=time_7["Kakashi Hatake"]["poder"]
for p in range(len(p1)):
    print(p1[p])
    if p1[p]=="Chidori":
        p1[p]="espada trovao"


print(p1)


for i in time_7.keys():
    print(i)


##Transformando e salvando o arquivo em python
with open ("D:/convite/python-estudos/project/arquivos/time_7.json","w") as file:
    time7=json.dump(time_7,file,indent=4)





#adiciona o novo objeto no fim do arquivo
#with open ("D:/convite/python-estudos/project/arquivos/time_7.json","a") as file:
#   time7=json.dump(time_7,file,indent=4)

