#Tela de seleção de opções do usuário
import sqlite3
from functions.livro import *
import os
conn = sqlite3.connect('biblioteca_db') 
c = conn.cursor()

def opc_usuario():
    opcao = 0
    while opcao != 8:
        print("------Biblioteca------")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livro")
        print("3 - Editar Livros")
        print("4 - Excluir Livro")
        print("5 - Locar Livro")
        print("6 - Devolução do Livro")        
        print("7 - Buscar Livro")
        print("8 - Sair")
    
        opcao = int(input ("Digite a opção desejada: "))
        os.system('cls||clear')
        if opcao == 1:
            print ("---Cadastro de Livro---")
            nome = input("Digite o nome do Livro: ")
            autor = input("Digite o nome do autor: ")
            cadastrar_livro(conn, nome, autor)
            print ("Cadastrado com Sucesso!")
        elif opcao == 2:
            livros = listar_livros(conn)
            print(livros)
        elif opcao == 3:
            nome = input("Digite o nome do livro que voçê deseja editar: ")
            nome_novo = input ("Digite o nome novo: ")
            autor_novo = input("Digite o autor: ")
            editar = editar_livro(conn, nome, nome_novo, autor_novo)
            print(editar)
        elif opcao == 4:
            nome = input('Digite o ID do Livro')
            excluir = excluir_livro(conn, id)
            print (excluir)
        elif opcao == 5:
            id = input("Digite o ID do livro: ")
            alugar = alugar_livro(conn, id)
            print(alugar)
        elif opcao == 6:
            id = input("Digite o ID do livro: ")
            devolver = devolver_livro(conn, id)
            print(devolver)
        elif opcao == 7:
            buscar_nome = input("Digite o nome para busca: ")
            buscar = buscar_livro(conn, buscar_nome)
            print(buscar)
        elif opcao == 8:
            print("Deslogado")
        else:
            print("Digite uma opção válida")