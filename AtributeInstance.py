class Pessoa:
    nome = ""
    idade = 0
    mae = ""
p = Pessoa()
print(type(p))
p.nome = 'Diego' # alterando o atributo nome do objeto 'p'
p.idade = 18# alterando o atributo idade do objeto 'p'
p.mae = 'Mae' # alterando o atributo mae do objeto 'p'
print(p.nome) #printando o atributo nome do objeto p
p2 = Pessoa() #criando outra instancia de objeto pessoa
p2.nome = 'Alex' # alterando o atributo nome do objeto 'p2'
p2.idade = 22 # alterando o atributo nome do objeto 'p2'
p2.mae = 'seila' # alterando o atributo nome do objeto 'p2'
