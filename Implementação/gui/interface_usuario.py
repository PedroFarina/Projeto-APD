from gui import menu_usuario
from logica import usuario

from gui import menu_filme
from logica import filme

def iniciar_modulos():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()

def mostrar_menu():    
    iniciar_modulos()
    
    rodando = True
    
    menu = ("\n----------------\n"+
             "(1) Menu Filme \n" +
             "(2) Menu Usuario \n" +
             "(0) Sair\n"+
            "----------------")
    while rodando:
        print(menu)
        op = input("Digite sua escolha:")
        
        if op == "0":
            rodando = False
        elif op == "1":
            menu_filme.mostrar_menu()
        elif op == "2":
            menu_usuario.mostrar_menu()
        else:
            print("Escolha inválida!")
        