class Musica:
    musicas = []

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


musica1 = Musica(nome='Beija-flor', artista='Victor e Vinicius', duracao=245)

musica2 = Musica(nome='Estilado', artista='Marcinho', duracao=326)

musica3 = Musica(nome='Mulher ingrata', artista='Roberto', duracao=298)

Musica.listar_musicas()