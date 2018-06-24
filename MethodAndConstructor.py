class Pessoa:
    nome = ''
    idade = 0
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def caminhar(self):
        print('Caminhando')

    def dormir(self):
        print('Dormindo')

p = Pessoa("Diego",18)
print(p.nome)
print(p.idade)
p.caminhar()
p.dormir()
