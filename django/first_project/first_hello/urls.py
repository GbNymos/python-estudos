from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("gabi",views.gabi,name="gabi"),
    #path("<str:name>",views.greet,name="greet"),
    path("novoano",views.newyear,name="novoano")

]


