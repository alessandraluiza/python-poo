class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print('Restaurante ativo')
else:
    print('Restaurante desativado')

categoria = Restaurante.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.categoria)

restaurante_pizza.ativo = True

print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')