import sqlite3
from functions.cadastro import *
conn = sqlite3.connect('biblioteca_db') 
c = conn.cursor()
import os

# Pagina inicial

opcao = 0
while(opcao != 3):
    print("--------Biblioteca----------")
    print("Opções")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair do Sistema")

    opcao = int(input("Digite a opção: "))
    os.system('cls||clear')
    if opcao == 1:
        print("Cadastro\n")
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input ("Digite sua senha: ")
        cadastrar(conn, nome, email, senha)
        print("Cadastrado com sucesso")
    elif opcao == 2:
        print("Login\n")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        usuario_autenticado = login(conn, email, senha)
        print(usuario_autenticado)
    elif opcao == 3:
        print("Até a próxima!")
    else:
        print("Digite uma opção válida")