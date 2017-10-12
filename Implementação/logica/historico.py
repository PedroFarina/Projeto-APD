historicos = []

def registrar_filme_assistido (cod_filme, cpf):
    historico = [cod_filme, cpf]
    historicos.append(historico)
    
def listar_historicos():
    return historicos

def buscar_historico(cpf):
    hist = []
    for h in historicos:
        if h[1] == cpf:
            hist.append(h)
    return hist

def remover_historico_por_cpf(cpf):
    aretirar = []
    for h in historicos:
        if h[1] == cpf:
            aretirar.append(h)
    for h in aretirar:
        historicos.remove(h)
    return True

def remover_historico(cod_filme, cpf):
    for h in historicos:
        if h[0] == cod_filme and h[1] == cpf:
            historicos.remove(h)
            return True
    return False

def iniciar_historicos():
    registrar_filme_asisstido("1", "455.879.638-29")
    registrar_filme_asisstido("2", "455.879.638-29")