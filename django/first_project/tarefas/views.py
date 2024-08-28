from django.shortcuts import render


lista_tarefas=["estudar","ler","caminhar"]

def index(request):
    return render(request,"tarefas/index.html",{
        "lista":lista_tarefas
    })


def add(request):
    return render(request,"tarefas/add.html")