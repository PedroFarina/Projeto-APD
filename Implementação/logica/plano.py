from logica import usuario

planos = []

def registrar_plano(plano, cpf):
    global planos
    u = usuario.buscar_usuario(cpf)
    p = [plano, u]
    planos.append(p)

def listar_planos():
    global planos
    return planos

def buscar_plano(cpf):
    global planos
    plano = None
    for p in planos:
        if p[1][0] == cpf:
            plano = p
    return plano

def alterar_plano(plano,cpf):
    global planos
    p = buscar_plano(cpf)
    if p != None:
        p[0] = plano
        return True
    return False

def deletar_plano(cpf):
    global planos
    p = buscar_plano(cpf)
    if p != None:
        planos.remove(p)
        return True
    else:
        return False



def iniciar_planos():
    registrar_plano("Moderador", "433.494.898-77")
    registrar_plano("Moderador", "441.910.418-00")