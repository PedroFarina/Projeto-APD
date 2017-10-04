from logica import filme

def exibir_menu_filme():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo filme \n" +
             "(2) Listar filmes \n" +
             "(3) Buscar filme por código \n" +
             "(4) Buscar filme por gênero \n" +
             "(5) Remover filme \n" +
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
