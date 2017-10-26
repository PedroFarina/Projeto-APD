from logica import usuario
from logica import filme

historicos = []

def registrar_filme_assistido (cod_filme, cpf):
    f = filme.buscar_filme(int(cod_filme))
    u = usuario.buscar_usuario(cpf)
    historico = [f, u]
    historicos.append(historico)
    
def listar_historicos():
    return historicos

def buscar_historico(cpf):
    hist = []
    for h in historicos:
        if h[1][0] == cpf:
            hist.append(h)
    return hist

def remover_historico_por_cpf(cpf):
    aretirar = []
    for h in historicos:
        if h[1][0] == cpf:
            aretirar.append(h)
    for h in aretirar:
        historicos.remove(h)
    return True

def remover_historico(cod_filme, cpf):
    cod_filme = int(cod_filme)
    for h in historicos:
        if h[0][0] == cod_filme and h[1][0] == cpf:
            historicos.remove(h)
            return True
    return False

def iniciar_historicos():
    registrar_filme_assistido(1, "455.879.638-29")
    registrar_filme_assistido(2, "455.879.638-29")