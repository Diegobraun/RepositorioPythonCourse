import random #gera numeros random
number = random.randint(1,10) #atribui a uma variavel um numero random de 1 a 10
print(number) #printa o  numero

lista = [1,2,3,4,5,6,7,8,9,10] #criando uma list de numeros
print(lista)#printando a lista
varRand = random.choice(lista) #a função percorre a lista e escolhe 1 numero aleatoriamente
print(varRand) #printa a var com o numero random
random.shuffle(lista) #embaralha toda a lista
print(lista) #printa a lista
randRand = random.random() #retorna um numero aleatorio entre 0.0 e 1.0
print(randRand) #printando o numero rand 
