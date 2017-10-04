usuarios = []

def adicionar_usuario (cpf, nome, email, senha):
    usuario = []
    usuario.append(cpf)
    usuario.append(nome)
    usuario.append(email)
    usuario.append(senha)
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios
    
def buscar_usuario (cpf):
    user = None
    for u in usuarios:
        if u[0] == cpf:
            user = u
    return user

def remover_usuario(cpf):
    user = buscar_usuario(cpf)
    if user in usuarios:
        usuarios.remove(user)
        return True
    else:
        return False
    
def iniciar_usuarios():
    adicionar_usuario("455.879.638-29", "Pedro", "pedrogfarina@gmail.com", "p1e2p3o4")
    adicionar_usuario("433.494.898-77", "Juan", "jnvictor@outlook.com.br", "juan1234")
    adicionar_usuario("441.910.418-00", "Leonardo", "leonardolongato@gmail.com", "futebol123")