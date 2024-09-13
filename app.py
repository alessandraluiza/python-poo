from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Alessandra', 8)
restaurante_praca.receber_avaliacao('Marcilio', 5)
restaurante_praca.receber_avaliacao('Ruana', 6)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()