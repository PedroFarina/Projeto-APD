import planos

def pedir_cpf():
    cpf = ""
    print("O CPF DEVE SER APENAS NÚMEROS")
    while len(cpf) != 11:
        cpf = str(input("CPF .: "))
    cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[-2:]
    return cpf

def imprimir_plano(plano):
    print("Plano : ", plano[0])
    print("CPF .: ", plano[1])
    print("Nome : ", plano[2])
    print()

def menu_adicionar():
    print("\Adicionar Plano\n")
    cpf = pedir_cpf()
    nome = str(input("Nome : "))
    plano = str(input("Plano: "))
    planos.registrar_plano(plano, cpf, nome)

def menu_buscar():
    print("\nBuscar Planos por CPF \n")
    cpf = pedir_cpf()
    p = planos.buscar_plano(cpf)
    if (p == None):
        print ("Plano não encontrado")
    else:
        imprimir_plano(p)

def menu_remover():
    print("\nRemover Plano \n")
    cpf = pedir_cpf()
    p = planos.deletar_plano(cpf)
    if (p == False):
        print ("Plano não encontrado")
    else:
        print("Plano removido")

def mostrar_menu():
    run_plano = True
    menu = ("\n-----------------\n"+
            "(1) Adicionar novo plano \n"+
            "(2) Buscar Plano \n"+
            "(3) Remover Plano \n"+
            "(0) Voltar \n"+
            "--------------------")
    while run_usuario:
        print(menu)
        op = input("Digite a sua escolha:")
        if op == "0":
            run_usuario = False
        elif op == "1":
            menu_adicionar()
        elif op == "2":
            menu_buscar()
        elif op == "3":
            menu_remover()
        else:
            print("Escolha inválida!")

