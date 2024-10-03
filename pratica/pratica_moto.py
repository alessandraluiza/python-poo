from pratica_veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, categoria):
        super().__init__(marca, modelo)
        self._categoria = False

    def __str__(self):
        categoria = 'esportiva' if self._categoria else 'casual'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Categoria: {categoria}'