pessoas = [
    {
        "id": 1,
        "name":"grazi",
        "email": "gurweue@gmil.com",
        "idade":16,
        "sobrenome":"oliveira"
    }, {
        "id": 2,
        "name":"gabi",
        "email": "fdfdjfhj@gmail.com",
        "idade":19,
        "sobrenome":"oliveira"
    },
]

emails_index = {
    "fdfdjfhj@gmail.com": 1,
    "gurweue@gmil.com": 2
}

id_index = {
    "2": 1,
}

pessoa_index = emails_index["fdfdjfhj@gmail.com"]
usuario = pessoas[pessoa_index]

print(usuario)
