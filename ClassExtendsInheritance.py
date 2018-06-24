from Inheritance import Pessoa #Inheritance é o nome da classe principal, cuja qual é realizado o import, ele navega pelo arquivo e importa
#a classe Pessoa
class PessoaFisica(Pessoa): #A herança é feita assim,é passado como parametro para pessoa fisica, parecido com o extends no java
    cpf = ''

    def __init__(self, cpf, **kwargs):#**kwargs é usado para botar no construtor todos os parametros da classe principal
        super(PessoaFisica,self).__init__(**kwargs) #super(nomeDaClasseAtual,self).__init__(comando que chama os demais parametros)
        self.cpf = cpf

    def aniversario(self):
        self.idade = self.idade + 1
        print("Agora a pessoa está com "+str(self.idade)+" anos") #str realiza o cast para poder concatenar inteiro com string

pf = PessoaFisica(nome = "Paulo",idade = 36,cpf = '123') #setando todos os valor
print(pf.nome)
print(pf.idade)
pf.aniversario()
pf.caminhar()
pf.dormir()
