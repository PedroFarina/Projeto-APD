planos = []

def registrar_plano(plano, cpf, nome):
    plano = [plano, cpf, nome]
    planos.append(plano)

def buscar_plano(cpf):
    plano = []
    for p in planos:
        if p[1] == cpf:
            plano.append(p)
    return plano

def alterar_plano(plano,cpf):
    for p in planos:
        if p[1] == cpf:
            plano == p[0]
    return plano

def deletar_plano(cpf):
    for p in planos:
        if p[1] == cpf:
            del planos[p]
    return planos



def iniciar_planos():
    registrar_plano("Moderador", "455.879.638-29", "Pedro")
    registrar_plano("Moderador", "433.494.898-77", "Juan")
    registrar_plano("Moderador", "441.910.418-00", "Leonardo")
    
    
