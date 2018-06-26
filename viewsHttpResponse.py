from django.shortcuts import render
from django.http import HttpResponse #importando HttpResponse, para fazer requisitions http
# Create your views here.


def home(request): #criando o metodo, toda request http recebe como primeiro parametro o request
    return HttpResponse('<h1>Hello world</h1>') #retornando o http response 

