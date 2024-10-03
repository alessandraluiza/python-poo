from pratica import Livro

livro_biblioteca = Livro("A Estrada Torta", "Renato Choper", 2007)
print(livro_biblioteca)
print(f'Antes de emprestar(biblioteca): Livro disponível? {livro_biblioteca.disponivel}')
livro_biblioteca.emprestar()
print(f'Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}')

ano_especifico = 2007
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {[str(livro) for livro in livros_disponiveis_ano]}")


