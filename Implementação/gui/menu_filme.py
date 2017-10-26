from logica import filme

def pedir_cpf():
    cpf = ""
    print("O CPF DEVE SER APENAS NÚMEROS")
    while len(cpf) != 11:
        cpf = str(input("CPF .: "))
    cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[-2:]
    return cpf

def imprimir_filme(filme):
    print ("Codigo: ", filme[0])
    print ("Titulo: ", filme[1])
    for g in filme[2]:
        print("Genero: ", g)
    print ("Ano  .: ", filme[3])
    print ()

def menu_adicionar():
    print ("\nAdicionar filme \n")
    titulo = str(input("Titulo: "))
    print ("Favor separar os generos por \";\"")
    genero = str(input("Genero: "))
    generos = []
    for g in genero.split(";"):
        generos.append(g)
    ano = int(input("Ano  .: "))
    filme.adicionar_filme(titulo, generos, ano)

def menu_listar():
    print ("\nListar filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)
    
def menu_buscar():
    print ("\nBuscar filme por código \n")
    cod = int(input("Cod: "))
    f = filme.buscar_filme(cod)
    if (f == None):
        print ("Filme não encontrado")
    else:
        imprimir_filme(f)
        
def menu_buscar_por_genero():
    print ("\nBuscar filme por genero \n")
    genero = str(input("Genero: "))
    f = filme.buscar_filmes_por_genero(genero)
    if (f == None):
        print ("Filme não encontrado")
    else:
        for f2 in f:
            imprimir_filme(f2)

def menu_remover():
    print ("\nRemover Filme \n")
    cod = int(input("Cod: "))
    f = filme.remover_filme(cod)
    if (f == False):
        print ("Filme não encontrado")
    else:
        print ("Filme removido")

def menu_reproduzir():
    cod = int(input("Digite o código do filme."))
    cpf = pedir_cpf()
    filme.reproduzir(cod, cpf)
    print("O filme foi reproduzido.")
    
def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo filme \n" +
             "(2) Listar filmes \n" +
             "(3) Buscar filme por código \n" +
             "(4) Buscar filme por gênero \n" +
             "(5) Remover filme \n" +
             "(6) Assistir filme \n"
             "(0) Voltar\n"+
            "----------------")
    
    while run_filme:
        print(menu)
        op = input("Digite sua escolha:")
    
        if op == "0":
            run_filme = False
        elif op == "1":
            menu_adicionar()
        elif op == "2":
            menu_listar()
        elif op == "3":
            menu_buscar()
        elif op == "4":
            menu_buscar_por_genero()
        elif op == "5":
            menu_remover()
        elif op == "6":
            menu_reproduzir()
        else:
            print("Escolha inválida!")
