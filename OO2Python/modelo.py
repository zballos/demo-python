class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Duracao: {self.duracao} - Likes: {self._likes}"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


marvel = Filme("vingadores - fim do jogo", 2018, 160)
marvel.dar_like()
marvel.dar_like()
marvel.dar_like()
miranha = Filme("Homem aranha - sem volta pra casa", 2022, 180)
miranha.dar_like()


serie = Serie("Rick and Morty", 2013, 6)
serie.dar_like()
serie.dar_like()
serie.dar_like()
aneis = Serie("Senhor dos anéis - os Anéis do poder", 2022, 1)
aneis.dar_like()
aneis.dar_like()

filmes_e_series = [marvel, miranha, serie, aneis]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho}')
for programa in playlist_fim_de_semana:
    print(programa)
