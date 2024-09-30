class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

Livro.livros = [
    Livro("A Estrada Torta", "Renato Choper", 2007),
    Livro("Python Cookbook", "Samuel Developer", 2019),
    Livro("Aprendendo Python", "John Doe", 2022),
    Livro("Data Science Fundamentals", "Jane Smith", 2020)
]