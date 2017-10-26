from logica import historico

def pedir_cpf():
    cpf = ""
    print("O CPF DEVE SER APENAS NÚMEROS")
    while len(cpf) != 11:
        cpf = str(input("CPF .: "))
    cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[-2:]
    return cpf

def imprimir_historico(historico):
    print ("Cod Filme  .:", historico[0][0])
    print ("Titulo Filme:", historico[0][1])
    print ("CPF       ..:",  historico[1][0])
    print ("Nome      ..:", historico[1][1])
    print ()

def menu_adicionar():
    print ("\nAdicionar Histórico \n")
    cpf = pedir_cpf()
    cod_filme = str(input("Código filme :"))
    historico.registrar_filme_assistido(cod_filme, cpf)

def menu_listar():
    print ("\nListar Histórico \n")
    historicos = historico.listar_historicos()
    for h in historicos:
        imprimir_historico(h)
    
def menu_buscar():
    print ("\nBuscar Histórico por CPF \n")
    cpf = pedir_cpf()
    h = historico.buscar_historico(cpf)
    if (h == None):
        print ("Histórico não encontrado")
    else:
        for h2 in h:
            imprimir_historico(h2)

def menu_remover_cpf():
    print ("\nRemover Histórico por CPF \n")
    cpf = pedir_cpf()
    h = historico.remover_historico_por_cpf(cpf)
    if (h == False):
        print ("Histórico não encontrado")
    else:
        print ("Histórico removido")
        
def menu_remover():
    print ("\nRemover Histórico por CPF e Codigo Filme \n")
    cpf = pedir_cpf()
    cod_filme = str(input("Código Filme :"))
    h = historico.remover_historico(cod_filme, cpf)
    if (h == False):
        print ("Histórico não encontrado")
    else:
        print ("Histórico removido")


def mostrar_menu():
    run_historico = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo histórico \n" +
             "(2) Listar histórico \n" +
             "(3) Buscar histórico por CPF \n" +
             "(4) Remover histórico por CPF \n" +
             "(5) Remover histórico por CPF e Codigo Filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while run_historico:
        print(menu)
        op = input("Digite sua escolha:")
    
        if op == "0":
            run_historico = False
        elif op == "1":
            menu_adicionar()
        elif op == "2":
            menu_listar()
        elif op == "3":
            menu_buscar()
        elif op == "4":
            menu_remover_cpf()
        elif op == "5":
            menu_remover()
        else:
            print("Escolha inválida!")