filmes = []

codigo_geral = 0

def reproduzir(cod_filme, cpf):
    from logica import historico
    historico.registrar_filme_assistido(cod_filme, cpf)
    
def adicionar_filme (titulo, generos, ano):
    filme = []
    filme.append(_gerar_codigo())
    filme.append(titulo)
    filme.append(generos)
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
    film = []
    for f in filmes:
        for g in f[2]:
            if g.upper() == genero.upper():
                film.append(f)
    if len(film) == 0:
        film = None
    return film
    
def remover_filme(cod_filme):
    filme = buscar_filme(cod_filme)
    if filme != None:
        filmes.remove(filme)
        return True
    else:
        return False
    
def _gerar_codigo():
    global codigo_geral
    codigo_geral += 1
    return codigo_geral
    
    
def iniciar_filmes():
    adicionar_filme("A volta dos que não foram", ["Comédia"], 2018)
    adicionar_filme("A lagoa azul", ["Drama", "Romance"], 1700)
    adicionar_filme("Velozes e Furiosos 1", ["Ação"], 2001)
    adicionar_filme("Hora do Rush", ["Ação", "Comédia"], 2000)