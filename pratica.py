class Restaurante:

    def __init__(self, nome, categoria, ativo=False, especialidade=any, cidade=any):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.especialidade = especialidade
        self.cidade = cidade
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
novo_restaurante = Restaurante(nome='Camilos', categoria='Brasileira')
print(novo_restaurante)
