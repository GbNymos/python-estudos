from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect




class new_task(forms.Form):
    task=forms.CharField(label="Nova tarefa: ")


def index(request):
    # verifica se ja existe uma chave informada na sessao
    if "lista_tarefas" not in request.session:
        #se nao existe crie uma nova lista
        request.session["lista_tarefas"]=[]

    return render(request,"tarefas/index.html",{
        "lista":request.session["lista_tarefas"]
    })


def add(request):
    if request.method=="POST":
        form=new_task(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]

            request.session["lista_tarefas"]+=[task]

            return HttpResponseRedirect(reverse("lista:index"))
        else:
            return render(request,"tarefas/add.html",{
                "form":form
            })
    return render(request,"tarefas/add.html",{
        "form":new_task()
    })





    return render(request,"tarefas/add.html",{
        "form":new_task()
    })