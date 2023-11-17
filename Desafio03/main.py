from biblioteca import *

import mysql.connector

while True:
    opcao = input("-----Menu-----\n1-Create\n2-Read\n3-Update\n4-Delete\nS-Sair\nEscolha uma opção: ").lower()
    match opcao:
        case "1":
            op = input("\n-----Tabelas-----\n1-Alunos \n2-funcionarios \n3-modalidade \n4-personal\n\nEscolha uma opção: ")
            create(op)
        case "2":
            op = input("\n-----Tabelas-----\n1-Alunos \n2-funcionarios \n3-modalidade \n4-personal\n\nEscolha uma opção: ")
            read(op)
        case "3":
            op = input("\n-----Tabelas-----\n1-Alunos \n2-funcionarios \n3-modalidade \n4-personal\n\nEscolha uma opção: ")
            update(op)
        case "4":
            op = input("\n-----Tabelas-----\n1-Alunos \n2-funcionarios \n3-modalidade \n4-personal\n\nEscolha uma opção: ")
            delete(op)
        case "s":
            break
        case _:
            print("\nTa errado amigao👎")
