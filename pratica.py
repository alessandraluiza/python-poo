class Restaurante:

    def __init__(self, nome, categoria, especialidade, cidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.especialidade = especialidade
        self.cidade = cidade

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Camilos', categoria='Brasileira')
