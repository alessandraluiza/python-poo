class Cliente:
    def __init__(self, nome, sobrenome, telefone, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.endereco = endereco

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cadastro1 = Cliente(nome='Alice', sobrenome='Souza', telefone='62-96325654')
cadastro2 = Cliente(nome='Raul', sobrenome='Greg', telefone='83-84569711')
cadastro3 = Cliente(nome='Sofia', sobrenome='Matos', telefone='42-85541236')
