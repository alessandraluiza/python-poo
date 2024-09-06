class Restaurante:

    def __init__(self, nome, categoria, especialidade, cidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.especialidade = especialidade
        self.cidade = cidade

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_praga = Restaurante(nome='Praga', categoria='Italiana', ativo=False, especialidade='Fettuccine', cidade='Asa Sul')