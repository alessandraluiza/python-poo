class Pessoa:
    
    def __init__ (self, nome='', idade=0, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade} \nProfissão: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        return f'Olá, {self.nome}! Como está o trabalho como {self.profissao}?'

pessoa1 = Pessoa("Maria", 30, "engenheira")
pessoa2 = Pessoa("João", 27, "programador")
pessoa3 = Pessoa("Benjamin", 55, "advogado")

print('Informações Funcionários:')
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()


pessoa1.aniversario()
pessoa2.aniversario()

print('Informações seguinte aniversário:')
print(pessoa1)
print(pessoa2)
print()


print(pessoa3.saudacao)

