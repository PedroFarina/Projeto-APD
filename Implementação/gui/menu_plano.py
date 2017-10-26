from logica import plano

def pedir_cpf():
    cpf = ""
    print("O CPF DEVE SER APENAS NÚMEROS")
    while len(cpf) != 11:
        cpf = str(input("CPF .: "))
    cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[-2:]
    return cpf

def imprimir_plano(plano):
    print("Plano : ", plano[0])
    print("CPF  .: ", plano[1][0])
    print("Nome  : ", plano[1][1])
    print()

def menu_adicionar():
    print("\nAdicionar Plano\n")
    p = str(input("Plano: "))
    cpf = pedir_cpf()
    plano.registrar_plano(p, cpf)

def menu_listar():
    planos = plano.listar_planos()
    for p in planos:
        print("Plano :", p[0])
        print("CPF  .:", p[1][0])
        print("Nome .:", p[1][1])
        print()
    
def menu_buscar():
    print("\nBuscar Planos por CPF \n")
    cpf = pedir_cpf()
    p = plano.buscar_plano(cpf)
    if (p == None):
        print ("Plano não encontrado")
    else:
        imprimir_plano(p)

def menu_remover():
    print("\nRemover Plano \n")
    cpf = pedir_cpf()
    p = plano.deletar_plano(cpf)
    if (p == False):
        print ("Plano não encontrado")
    else:
        print("Plano removido")

def mostrar_menu():
    run_plano = True
    menu = ("\n-----------------\n"+
            "(1) Adicionar novo plano \n"+
            "(2) Listar Planos \n" +
            "(3) Buscar Plano \n"+
            "(4) Remover Plano \n"+
            "(0) Voltar \n"+
            "--------------------")
    while run_plano:
        print(menu)
        op = input("Digite a sua escolha:")
        print()
        if op == "0":
            run_plano = False
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

