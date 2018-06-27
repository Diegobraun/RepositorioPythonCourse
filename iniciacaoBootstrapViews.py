from django.shortcuts import render #retornar uma http response
from django.http import HttpResponse #importando HttpResponse, para fazer requisitions http
# Create your views here.


def home(request): #criando o metodo, toda request http recebe como primeiro parametro o request
    return render(request,'base.html') #agora, estamos utilizando o 'render', ele que auxilia em requisitions http,
    #passando como primeiro parametro o request e segundo parametro o nome do html a ser chamado.
    #Poderia haver mais argumentos, como um dicionario, por exemplo. Onde poderiam ser passadas variáveis para a outra page

