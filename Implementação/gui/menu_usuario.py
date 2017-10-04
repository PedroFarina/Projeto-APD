from logica import usuario

def pedir_cpf()
    cpf = ""
    print("O CPF DEVE SER APENAS NÚMEROS")
    while len(cpf) != 11:
        cpf = str(input("CPF .: "))
    cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[-2:]
    return cpf

def imprimir_usuario(usuario):
    print ("CPF .: ",  usuario[0])
    print ("Nome : ", usuario[1])
    print ("Email: ",  usuario[2])
    print ()

def menu_adicionar():
    print ("\nAdicionar Usuario \n")
    cpf = pedir_cpf()
    nome = str (input("Nome : "))
    email = str(input("Email: "))
    senha = str(input("Senha:"))
    usuario.adicionar_usuario(cpf, nome, email, senha)

def menu_listar():
    print ("\nListar Usuários \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)
    
def menu_buscar():
    print ("\nBuscar Usuario por CPF \n")
    cpf = pedir_cpf()
    u = usuario.buscar_usuario(cpf)
    if (u == None):
        print ("Usuário não encontrado")
    else:
        imprimir_usuario(p)

def menu_remover():
    print ("\nRemover Usuario \n")
    cpf = pedir_cpf()
    u = usuario.remover_usuario(cpf)
    if (p == False):
        print ("Usuário não encontrado")
    else:
        print ("Usuário removido")

def exibir_menu_usuario():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo usuário \n" +
             "(2) Listar usuários \n" +
             "(3) Buscar usuário por CPF \n" +
             "(4) Remover usuário \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while run_usuario:
        print(menu)
        op = input("Digite sua escolha:")
    
        if op == "0":
            run_usuario = False
        elif op == "1":
            menu_adicionar()
        elif op == "2":
            menu_listar()
        elif op == "3":
            menu_buscar()
        elif op == "4":
            menu_remover()
        else:
            print("Escolha inválida!")
