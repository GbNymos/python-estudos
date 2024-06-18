import datetime

data_e_hora_atual=datetime.datetime.now()
print(data_e_hora_atual)

nasc=datetime.datetime(2005,4,18)

dic_test={"ano_nasc":nasc.year}
print(dic_test["ano_nasc"])

##Retorna em texto o dia da semana
print(nasc.strftime("%A"))
if nasc.strftime("%A")=="Tuesday":
    print("Voce nasceu em uma terca feira")
