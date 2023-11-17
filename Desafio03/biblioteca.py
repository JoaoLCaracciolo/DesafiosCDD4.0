import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
)


def create(opcao):
    meucursor = banco.cursor()
    match opcao:

        case "1":
            print("------ALUNOS------")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            comando = "INSERT INTO alunos (nome, cpf, telefone, endereco) VALUES (%s,%s,%s,%s)"
            dados = (nome, cpf, telefone, endereco)
            meucursor.execute(comando, dados)
            banco.commit()
            userid = meucursor.lastrowid
            print("O dado foi inserido")

        case "2":
            print("------FUNCIONÁRIOS------")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            departamento = input("Departamento: ")
            salario = input(float("Salario: "))
            email = input("Email: ")
            comando = ("INSERT INTO funcionarios (nome, cpf, departamento, salario, email) VALUES(%s,%s,%s,%s,%s)")
            dados = (nome, cpf, departamento, salario, email)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi inserido")

        case "3":
            print("------MODALIDADES------")
            nome_modalidade = input("Nome: ")
            duracao = input("Duração: ")
            meucursor = banco.cursor()
            comando = ("INSERT INTO modalidades (nome_modalidade, duracao) VALUES (%s,%s)")
            dados = (nome_modalidade, duracao)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi inserido")
        case "4":
            print("------PERSONAL------")
            cref = input("CREF: ")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            comando = ("INSERT INTO personal (cref, nome, telefone, email, cpf, endereco) VALUES (%s,%s,%s,%s,%s,%s)")
            dados = (cref, nome, telefone, email, cpf, endereco)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi inserido")
        case _:
            print("Ta errado amigao👎")


def read(opcao):
    global tabela
    match opcao:

        case "1":
            tabela = "alunos"
        case "2":
            tabela = "funcionarios"
        case "3":
            tabela = "modalidades"
        case "4":
            tabela = "personal"
        case _:
            print("Ta errado amigao")

    meucursor = banco.cursor()
    pesquisa = f'SELECT * FROM {tabela};'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for x in resultado:
        print(x)


def update(opcao):
    match opcao:

        case "1":
            print("------ALUNOS------")
            matricula = int(input("Matricula: "))
            nome = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            telefone = input("Novo Telefone: ")
            endereco = input("Novo Endereço: ")
            meucursor = banco.cursor()
            comando = f"UPDATE alunos SET nome=%s,cpf=%s,telefone=%s,endereco=%s WHERE matricula = {matricula};"
            dados = (nome, cpf, telefone, endereco)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi mudado")

        case "2":
            print("------FUNCIONÁRIOS------")
            id_funcionarios = int(input("ID: "))
            nome = input("Novo Nome: ")
            cpf = input("Novo CPF: ")
            departamento = input("Novo Departamento: ")
            salario = float(input("Novo Salario: "))
            email = input("Novo Email: ")
            meucursor = banco.cursor()
            comando = f"UPDATE funcionarios SET nome=%s,cpf=%s,departamento=%s,salario=%s,email=%s WHERE id_funcionarios = {id_funcionarios};"
            dados = (nome, cpf, departamento, salario, email)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi mudado")
        case "3":
            print("------MODALIDADES------")
            cod_modalidade = int(input("COD: "))
            nome_modalidade = input("Nome: ")
            duracao = input("Duração: ")
            meucursor = banco.cursor()
            comando = f"UPDATE modalidades SET nome_modalidade=%s,duracao=%s WHERE cod_modalidade = {cod_modalidade};"
            dados = (nome_modalidade, duracao)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi mudado")
        case "4":
            print("------PERSONAL------")
            id_personal = int(input("ID: "))
            cref = input("Novo CREF: ")
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo Email: ")
            cpf = input("Novo CPF: ")
            endereco = input("Novo Endereço: ")
            meucursor = banco.cursor()
            comando = f"UPDATE personal SET cref=%s,nome=%s,telefone=%s,email=%s,cpf=%s,endereco=%s WHERE id_personal = {id_personal};"
            dados = (cref, nome, telefone, email, cpf, endereco)
            meucursor.execute(comando, dados)
            banco.commit()
            print("O dado foi mudado")
        case _:
            print("Ta errado amigao👎")


def delete(opcao):
    match opcao:

        case "1":
            print("------ALUNOS------")
            matricula = int(input("Matricula: "))
            meucursor = banco.cursor()
            comando = f"DELETE FROM alunos WHERE matricula = {matricula};"
            meucursor.execute(comando)
            banco.commit()
            print("O dado foi deletado")
        case "2":
            print("------FUNCIONÁRIOS------")
            id_funcionarios = int(input("ID: "))
            meucursor = banco.cursor()
            comando = f"DELETE FROM funcionarios WHERE id_funcionarios = {id_funcionarios};"
            meucursor.execute(comando)
            banco.commit()
            print("O dado foi deletado")
        case "3":
            print("------MODALIDADES------")
            cod_modalidade = int(input("COD: "))
            meucursor = banco.cursor()
            comando = f"DELETE FROM modalidades WHERE cod_modalidade = {cod_modalidade};"
            meucursor.execute(comando)
            banco.commit()
            print("O dado foi deletado")
        case "4":
            print("------PERSONAL------")
            id_personal = int(input("ID: "))
            meucursor = banco.cursor()
            comando = f"DELETE FROM personal WHERE id_personal = {id_personal};"
            meucursor.execute(comando)
            banco.commit()
            print("O dado foi deletado")
        case _:
            print("Ta errado amigao👎")
