import json

## ja e um arquivo json tranformado em dict
test={
  "pessoas": [
    {"nome": "Alice", 
     "idade": 30,
     "email": "alice@example.com"
    },
    {"nome": "Bob",
     "idade": 25,
     "email": "bob@example.com"
    },
    {"nome": "Carol",
     "idade": 27,
     "email": "carol@example.com"
    }
  ]
}


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