filmes = []

codigo_geral = 0

def adicionar_filme (titulo, genero, ano):
    filme = []
    filme.append(_gerar_codigo())
    filme.append(titulo)
    filme.append(genero)
    filme.append(ano)
    filmes.append(filme)
    
def listar_filmes ():
    return filmes

def buscar_filme(cod_filme):
    film = None
    for f in filmes:
        if f[0] == cod_filme:
            film = f
    return film
        
def buscar_filmes_por_genero(genero):
    film = None
    for f in filmes:
        if f[2] == genero:
            film = f
    return film
    
def remover_filme(cod_filme):
    filme = buscar_filme(cod_filme)
    if filme != None:
        filmes.remove(filme)
    else:
        print("Filme não encontrado.")
    
def _gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral
    
    
def iniciar_filmes():
    adicionar_filme("A volta dos que não foram", "Comédia", "2018")
    adicionar_filme("A lagoa azul", "Drama", "1700")
    adicionar_filme("Velozes e Furiosos 1", "Ação", "2001")