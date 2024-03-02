class Anime:
    def __init__(self,imagem_anime,imagem_fundo_anime,nome_anime,generos,descricao,quantidade_capitulos):
        self.imagem_anime =imagem_anime
        self.imagem_fundo_anime =imagem_fundo_anime
        self.nome_anime =nome_anime
        self.generos =generos
        self.descricao =descricao
        self.quantidade_capitulos =quantidade_capitulos



class Capitulo:
    def __init__(self,anime_do_capitulo,nome_capitulo,video_capitulo,thumbnail):
        self.anime_do_capitulo =anime_do_capitulo
        self.nome_capitulo =nome_capitulo
        self.video_capitulo =video_capitulo
        self.thumbnail =thumbnail



overLord = Anime()
capitulo_1_overLord = Capitulo()