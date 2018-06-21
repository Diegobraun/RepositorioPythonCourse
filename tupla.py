tupla = ("Python","Java","Android",12,[1,2,3],(1,2))
tupla[0] #A saída disso será 'Python'
print(tupla)
dir(tupla)
tupla.append(15) #Retorna uma exception porque tupla é imutável
tupla.count("Python") #Quantas vezes python aparece na tupla
tupla[4].append(4) #Isso funciona porque está manipulado uma lista dentro de uma tupla