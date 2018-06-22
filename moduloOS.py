import os #importa o os
os.system("clear") #limpa a tela do terminal
os.getcwd() #informa o diretório que estou
os.mkdir("NomeDaPasta") #cria um diretório
os.chdir("NomeDaPasta") #dá um checkout pra pasta
from urllib.request import urlopen #procura no os e importa urlopen
html = urlopen("https://google.com") #atribui a url a uma var
print(html.read()) #printa html, de um modo feio
#INICIA MELHOR MÉTODO
from bs4 import BeautifulSoup #melhora a exibição
bsbObj = BeautifulSoup(html.read()) #utiliza o metodo e le o html
print(bsbObj) #imprime o html